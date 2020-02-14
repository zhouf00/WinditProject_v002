import xadmin

from users.models import Structure


class StructureAdmin(object):
    list_display = ['title', 'type', 'parent']
    list_filter = ['title', 'type', 'parent']


xadmin.site.register(Structure, StructureAdmin)