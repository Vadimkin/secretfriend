from django.conf.urls import patterns, url
from users import views

urlpatterns = [
    url(r'^$', views.IndexRedirectView.as_view(), name='index'),
    url(r'^register/$', views.RegisterTemplateView.as_view(), name='register'),
    url(r'^profile/$', views.ProfileTemplateView.as_view(), name='profile'),
    url(r'^profile/ajax$', views.ProfileAjaxView.as_view(), name='profile_ajax'),

]