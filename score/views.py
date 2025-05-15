from django.shortcuts import render
from django.db.models import Q
from .forms import ScoreQueryForm
from .models import Student, FoodManagement, FashionDesign, StylingDesign

def index(request):
    """主頁視圖函數"""
    form = ScoreQueryForm()
    context = {
        'form': form,
        'show_result': False
    }
    
    if request.method == 'POST':
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
    
    return render(request, 'score/index.html', context)
