from django.conf.urls import url

from APPS.rbac import views_role, views_menu

urlpatterns = [

    # 组织架构的改删查操作
    url(r'^role/$', views_role.RoleView.as_view(), name="role"),
    url(r'^role/list$', views_role.RoleListView.as_view(), name="role-list"),
]