from . import views
from django.urls import path

urlpatterns = [
  path('register/', views.RegisterView.as_view(),name='register' ),
  path('login/', views.LoginView.as_view(),name='login' ),
  path('currentuser/', views.CurrentUserView.as_view(),name='currentuser' ),
  path('logout/', views.LogoutView.as_view(),name='logout'),
]