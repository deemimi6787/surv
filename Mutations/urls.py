from django.urls import path
from . import views


urlpatterns = [
    path('index/',views.index,name='index'),
    path('dashboard/',views.user_dashboard,name='dashboard'),
    path('sign/',views.sign_up, name='user_sign'),
    path('home/',views.home,name='home'),
    path('', views.sign_in, name='login_user'),
    path('report/',views.report,name='report'),
    path('entry/',views.entry,name='entry'),
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    path('c2b/register', views.register_urls, name="register_mpesa_validation"),
    path('c2b/confirmation', views.confirmation, name="confirmation"),
    path('c2b/validation', views.validation, name="validation"),
    path('c2b/callback', views.call_back, name="call_back"),
]