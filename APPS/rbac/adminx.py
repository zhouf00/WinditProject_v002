import xadmin
from xadmin import views

from rbac.models import Menu, Role


class GlobalSettings(object):
    site_title = "周凡自制协同办公平台后台管理系统"
    site_footer = "Copyright © 2019-2020 周凡科技. Version1.0.1"
    menu_style = "accordion"  # 导航菜单折叠


class MenuAdmin(object):
    list_display = ['id', 'title', 'is_top', 'icon', 'code', 'url', 'parent']
    list_filter = ['id', 'title', 'is_top', 'icon', 'code', 'parent']
    list_editable = ['is_top', 'url']


class RoleAdmin(object):
    list_display = ['id', 'title', 'permissions']


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Menu, MenuAdmin)
xadmin.site.register(Role, RoleAdmin)