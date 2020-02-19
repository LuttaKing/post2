from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="main-home"),
    path('page2/',views.post_data,name='page2'),
    
]