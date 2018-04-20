from django.conf.urls import url
from . import views

urlpatterns = [
        #url(r'^', views.index_template, name='index_template'),
        #url(r'^', views.index_template, name='index_template'),
        url(r'^', views.settingWindow, name='settingWindow')
        #url(r'^templates/', views.index_template, name='index_template'),
]
