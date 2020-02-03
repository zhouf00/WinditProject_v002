"""WinditProject_v002 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.views.static import serve
from WinditProject_v002.settings import MEDIA_ROOT

import xadmin

from APPS.users.views_user import IndexView, LoginView, LogoutView
from APPS.system.views import SystemView
from APPS.personal import views as personal_views

urlpatterns = [
    url(r'^xamdin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
    url(r'^$', IndexView.as_view(), name='index'),

    # 用户登陆
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    # 系统设置
    url(r'^system/$', SystemView.as_view(), name='system'),
    url(r'^system/basic/', include(('users.urls', 'system-basic'), namespace='system-basic')),
    url(r'^system/rbac/', include(('rbac.urls','system-rbac'), namespace='system-rbac')),

    url(r'^personal/$', personal_views.PersonalView.as_view() , name='personal'),
    url(r'^personal/userinfo', personal_views.UserInfoView.as_view(), name='personal-user_info')
]
