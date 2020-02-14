from django.conf.urls import url

from rbac import views_role, views_menu

urlpatterns = [

    # 菜单管理
    url(r'^menu/$', views_menu.MenuView.as_view(), name="menu"),
    url(r'^menu/list$', views_menu.MenuListView.as_view(), name='menu_list'),
    url(r'^menu/detail$', views_menu.MenuListDetailView.as_view(), name='menu_detail'),

    # 组织架构的改删查操作
    url(r'^role/$', views_role.RoleView.as_view(), name="role"),
    url(r'^role/list$', views_role.RoleListView.as_view(), name="role_list"),
    url(r'^role/detail$', views_role.RoleDetailView.as_view(), name="role_detail"),
    url(r'^role/delete$', views_role.RoleDeleteView.as_view(), name="role_delete"),
    url(r'^role/role_user$', views_role.RoleUserView.as_view(), name="role_user"),
    url(r'^role/role_menu$', views_role.RoleMenuView.as_view(), name="role_menu"),
    url(r'^role/role_menu_list', views_role.RoleMenuListView.as_view(), name='role_menu_list'),

]