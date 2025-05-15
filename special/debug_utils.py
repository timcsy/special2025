"""
調試工具函數集
用於在開發階段提供更多的調試資訊
"""

import os
from django.conf import settings

def debug_info(request):
    """
    返回關於請求和環境的調試資訊
    
    參數:
        request: HttpRequest 對象
    返回:
        dict: 包含調試資訊的字典
    """
    info = {
        'DEBUG': settings.DEBUG,
        'ALLOWED_HOSTS': settings.ALLOWED_HOSTS,
        'REQUEST_METHOD': request.method,
        'REQUEST_PATH': request.path,
        'REQUEST_SCHEME': request.scheme,
        'REQUEST_HEADERS': dict(request.headers),
        'CSRF_COOKIE': request.COOKIES.get('csrftoken', None),
        'ENV': {k: v for k, v in os.environ.items() if not k.startswith('_') and not k.startswith('PYTHON')}
    }
    return info
