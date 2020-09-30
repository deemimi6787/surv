from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('report/',views.report,name='report'),
    path('entry/',views.entry,name='entry')
]