"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from my_app import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "my_app"

urlpatterns = [
    url('admin/', admin.site.urls),
    url('my_app/', include("my_app.urls")),
    url(r'^home/(?P<pk>\d+)/$', views.home, name="home"),
    url(r'^register/$', views.register_user, name="register"),
    url(r'^logout_user/$', views.logout_user, name="logout_user"),
    url(r'^add_patients/$', views.add_patients, name="add_patients"),
    url(r'^add_prescription/$', views.add_prescription, name="add_prescription"),
    url(r'^add_scan_report/$', views.add_scan_report, name="add_scan"),
    url(r'^add_x_ray/$', views.add_x_ray, name="add_x_ray"),
    url(r'^my_account/(?P<pk>\d+)/$', views.my_account, name="my_account"),
    url(r'^search_patients/$', views.search_patients, name="search_patients"),
    ##########CRUD#########
    url(r'^update_patients/(?P<pk>\d+)/$', views.update_patients, name="update_patients"),
    url(r'^delete_patients/(?P<pk>\d+)/$', views.delete_patients, name="delete_patients"),
    url(r'^update_prescription/(?P<pk>\d+)/$', views.update_prescription, name="update_prescription"),
    url(r'^delete_prescription/(?P<pk>\d+)/$', views.delete_prescription, name="delete_prescription"),
    url(r'^update_x_ray/(?P<pk>\d+)/$', views.update_x_ray, name="update_x_ray"),
    url(r'^delete_x_ray/(?P<pk>\d+)/$', views.delete_x_ray, name="delete_x_ray"),
    url(r'^update_scan/(?P<pk>\d+)/$', views.update_scan, name="update_scan"),
    url(r'^delete_scan/(?P<pk>\d+)/$', views.delete_scan, name="delete_scan"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
