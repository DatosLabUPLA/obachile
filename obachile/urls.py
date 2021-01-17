from django.contrib import admin
from django.urls import path, re_path
from scholar import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
urlpatterns = [

    path('admin/', admin.site.urls),
    re_path(r'^.*\.html', views.pages, name='pages'),

    #path('', views.index, name='home'),
   
    url('chart/', views.charts, name='chart'),
    path('', views.charts, name='home'),
    
    #url('tables/', views.table, name='tables'),
    url(r'^tables$', views.table, name='tables'),
     url(r'^tables2$', views.table2, name='tables2'),
    url(r'^perfil/(?P<id>\d+)$', views.perfil, name='perfil'),
     url(r'^perfil2/(?P<a_id>\d+)$', views.perfil2, name='perfil2'),
    url(r'^perfil$', views.chartsperfiles, name='perfil'),


]
urlpatterns += staticfiles_urlpatterns()
