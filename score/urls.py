from django.urls import path
from . import views
from django.conf import settings

app_name = 'score'

urlpatterns = [
    path('', views.index, name='index'),
]

# 僅在調試模式下添加調試路由
if settings.DEBUG:
    urlpatterns.append(path('debug/csrf/', views.debug_csrf, name='debug_csrf'))