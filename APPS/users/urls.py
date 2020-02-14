from django.conf.urls import url

from APPS.users import views_user

app_name = 'system'

urlpatterns = [
    url(r'^user/$', views_user.UserView.as_view(), name='user'),
    url(r'^user/list$', views_user.UserListView.as_view(), name='user_list'),
    url(r'^user/detail$', views_user.UserDetailView.as_view(), name='user_detail'),
    url(r'^user/create$', views_user.UserCreateView.as_view(), name='user_create'),
    url(r'^user/updata$', views_user.UserUpdateView.as_view(), name='user_updata'),
    url(r'^user/delete$', views_user.UserDeleteView.as_view(), name='user_delete'),
    url(r'^user/adminpasswdchange$', views_user.AdminPasswdChangeView.as_view(), name='user_adminpasswdchange')
]