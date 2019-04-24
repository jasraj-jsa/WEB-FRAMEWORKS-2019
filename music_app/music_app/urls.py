
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index1.html'), name='index1'),
    path('', include('django.contrib.auth.urls') ),
    path('home/',TemplateView.as_view(template_name='home_index.html'), name='home_index'),
    path('signup/',views.SignUp.as_view(), name='signup_index'),
    path('albums/',TemplateView.as_view(template_name='albums_index.html'), name='albums_index'),
    path('artists/',TemplateView.as_view(template_name='artists_index.html'), name='artists_index'),
    path('about/',TemplateView.as_view(template_name='about_index.html'), name='about_index'),
    path('features/',TemplateView.as_view(template_name='features_index.html'), name='features_index'),
    path('premium/',TemplateView.as_view(template_name='premium_index.html'), name='premium_index'),
    #path('api/', include(router.urls)),
    #path('album/', TemplateView.as_view(template_name='models_index.html')),
]
