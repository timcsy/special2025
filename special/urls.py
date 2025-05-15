"""
URL configuration for special project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from score.views import debug_csrf, get_csrf_token  # 導入調試視圖和令牌視圖
# 只有在調試模式下才導入調試工具
if settings.DEBUG:
    from .debug_utils import debug_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('score/', include('score.urls')),
    path('', RedirectView.as_view(url='score/')),  # 將根路徑重定向到 score 應用
]

# 添加調試和 CSRF 相關路由
if settings.DEBUG:
    urlpatterns.append(path('debug/csrf/', debug_csrf, name='debug_csrf'))

# 總是添加獲取 CSRF 令牌的路由
urlpatterns.append(path('csrf/token/', get_csrf_token, name='get_csrf_token'))
