from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [path('news', views.post_list, name='post_list'),
                path('', views.index, name='index'),
                url(r'^send/', views.send),
                path('sight', views.sight, name="sight"),
               ]
