from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('users.urls')),
]