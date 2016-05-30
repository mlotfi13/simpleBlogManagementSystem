from django.conf.urls import include, url
from django.contrib import admin
from BMS import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'weblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include('BMS.urls')),
    url(r'^$', views.homepage, name='HomePage'),
]
