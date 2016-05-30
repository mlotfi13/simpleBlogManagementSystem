from django.conf.urls import url
from django.contrib.auth.views import logout

from . import views

urlpatterns = [
				url(r'^$', views.Adminlogin, name='Adminlogin'),
				url(r'^list/$', views.UserList.as_view(), name='List'),
				url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
				url(r'^edit/(?P<pk>[0-9]+)/$', views.UserUpdate.as_view(), name='edit_user'),
    			url(r'^delete/(?P<pk>[0-9]+)/$', views.Delete.as_view(), name='delete_user'),
    			url(r'^new/$', views.Create.as_view(), name='new_user'),	
]