from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.middleware.csrf import get_token
from django.conf import settings
import json
from .forms import ScoreQueryForm
from .models import Student, FoodManagement, FashionDesign, StylingDesign

@ensure_csrf_cookie
@csrf_protect
def index(request):
    """主頁視圖函數"""
    form = ScoreQueryForm()
    
    # 無論是否為調試模式，都提供必要的上下文
    context = {
        'form': form,
        'show_result': False,
        'debug': settings.DEBUG,
        'csrf_token': get_token(request)  # 確保 CSRF 令牌可用
    }
    
    # 添加請求信息到上下文方便調試
    context['debug_info'] = {
        'method': request.method,
        'headers': {k: v for k, v in request.headers.items()},
        'path': request.path,
        'is_ajax': request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    }
    
    if request.method == 'POST':
        # 檢查是否是 AJAX 請求
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        
        # 處理表單數據
        form = ScoreQueryForm(request.POST)
        if form.is_valid():
            admit_number = form.cleaned_data['admit_number']
            id_last_4_digits = form.cleaned_data['id_last_4_digits']
            
            # 確保身分證末四碼格式一致 (補足前導零)
            id_last_4_digits = id_last_4_digits.zfill(4)
            
            # 查詢對應的學生
            student = Student.objects.filter(
                admit_number=admit_number,
                id_last_4_digits=id_last_4_digits
            ).first()
            
            if student:
                # 嘗試查找學生在各科的成績
                dept_type = None
                dept_data = None
                dept_name = None
                subjects = []
                
                # 檢查餐飲管理科
                try:
                    dept_data = FoodManagement.objects.get(student=student)
                    dept_type = 'food'
                    dept_name = '餐飲管理科'
                    subjects = [
                        {'name': '食材辨識', 'score': dept_data.food_identification},
                        {'name': '餐飲器具辨識', 'score': dept_data.utensil_identification}
                    ]
                except FoodManagement.DoesNotExist:
                    # 檢查流行服飾科
                    try:
                        dept_data = FashionDesign.objects.get(student=student)
                        dept_type = 'fashion'
                        dept_name = '流行服飾科'
                        subjects = [
                            {'name': '基礎設計手縫', 'score': dept_data.basic_sewing},
                            {'name': '創意繪圖', 'score': dept_data.creative_drawing}
                        ]
                    except FashionDesign.DoesNotExist:
                        # 檢查整體造型特色班
                        try:
                            dept_data = StylingDesign.objects.get(student=student)
                            dept_type = 'styling'
                            dept_name = '整體造型特色班'
                            subjects = [
                                {'name': '基礎設計手縫', 'score': dept_data.basic_sewing},
                                {'name': '整體造型色彩繪圖', 'score': dept_data.color_drawing}
                            ]
                        except StylingDesign.DoesNotExist:
                            pass
                
                if dept_data:
                    context.update({
                        'show_result': True,
                        'student': student,
                        'dept_type': dept_type,
                        'dept_name': dept_name,
                        'subjects': subjects,
                        'total_score': dept_data.total_score
                    })
                else:
                    context['error'] = '查無此考生相關術科成績資料'
            else:
                context['error'] = '查無此考生資料，請確認准考證號與身份證末四碼是否正確'
                
        context['form'] = form
        
        # 如果是 AJAX 請求，返回 JSON 格式的響應
        if is_ajax:
            return JsonResponse({
                'success': 'error' not in context,
                'error': context.get('error', None),
                'html': render(request, 'score/index.html', context).content.decode('utf-8') if 'error' not in context else None
            })
    
    return render(request, 'score/index.html', context)

def debug_csrf(request):
    """CSRF 調試視圖"""
    return JsonResponse({
        'csrf_cookie': request.COOKIES.get('csrftoken', 'Not Found'),
        'csrf_middleware_token': request.META.get('CSRF_COOKIE', 'Not Found'),
        'csrf_header': request.META.get('HTTP_X_CSRFTOKEN', 'Not Found'),
        'csrf_header_alt': request.META.get('HTTP_X_CSRF_TOKEN', 'Not Found'),
        'trusted_origins': settings.CSRF_TRUSTED_ORIGINS,
        'allowed_hosts': settings.ALLOWED_HOSTS,
        'debug': settings.DEBUG,
        'method': request.method,
        'is_secure': request.is_secure(),
        'host': request.get_host(),
        'all_headers': dict(request.headers),
        'all_cookies': request.COOKIES,
    })

def get_csrf_token(request):
    """獲取 CSRF 令牌的視圖"""
    # 強制生成一個新的 CSRF 令牌
    token = get_token(request)
    return HttpResponse(
        json.dumps({'csrfToken': token}),
        content_type='application/json'
    )
