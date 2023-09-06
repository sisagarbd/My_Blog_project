from django.urls import path
from App_Blog import views

app_name = "App_Blog"

urlpatterns=[
    path('', views.blog_list, name='blog_list' )
]