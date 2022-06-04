import profile
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.homepage, name = "bank-transactions"),
    path('login/',auth_views.LoginView.as_view(template_name = "login.html"), name = "bank-login"),
    #path('login/',auth_views.LoginView.as_view(template_name = "login.html"), name = "bank-login"),
    path('signup/', views.signup,name = "bank-signup" ),
    path('payments/', views.payments, name= "bank-payments"),
    # path('logout/', views.logout, name = 'bank-logout'),
    path('logout/', auth_views.LogoutView.as_view(template_name = "logout.html"),name= "bank-logout"),
    path('profile/', views.profile, name = 'bank-profile'),
]
