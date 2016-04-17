"""divorces URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.models import User
from django.views.generic import RedirectView
from django.views.generic import TemplateView
import django.template.loader
# Rules 
import rules_light
import restless
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers, serializers, viewsets
from rest_framework import generics
from rest_framework import viewsets, routers
from rest_framework.authtoken import views as drf_views

#from custom.users.views import ProfileViewSet

router = routers.DefaultRouter()

#router.register(r'profiles',ProfileViewSet,base_name='profiles')

admin.autodiscover()
urlpatterns = [
#    url(r'^', include(router.urls)),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#    url(r'^django-rq/', include('django_rq.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
 #   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
 #   url(r'^accounts_api/', include('registration_api.urls')),
 #   url(r'^api/',include('rest_framework.urls', namespace='rest_framework')),
 #   url(r'api/accounts/', include('rest_framework.urls', namespace='rest_framework')), 
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^home/$', 'custom.gui.views.home'),
    url(r'^aboutus/$', 'custom.gui.views.aboutus'),
    url(r'^about/$', 'custom.gui.views.about'),
    url(r'^divorce/$', 'custom.gui.views.divorce'),
    url(r'^pricing/$', 'custom.gui.views.pricing'),
    url(r'^services/$', 'custom.gui.views.services'),
    url(r'^contacts/$', 'custom.gui.views.contacts'),
    url(r'^blog/$', 'custom.gui.views.blog'),
    url(r'^ask/$', 'custom.gui.views.ask'),
    url(r'^', 'custom.gui.views.home'),
]

