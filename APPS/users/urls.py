from django.conf.urls import url

from APPS.users import views_user

app_name = 'system'

urlpatterns = [
    url(r'^user/$', views_user.UserView.as_view(), name='user'),
    url(r'^user/list$', views_user.UserListView.as_view(), name='user-list'),
]