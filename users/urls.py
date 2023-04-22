from .views import RegisterView, LoginView, CurrentUserView, LogoutView
from django.urls import path

urlpatterns = [
  path('register/', RegisterView.as_view(),name='register' ),
  path('login/', LoginView.as_view(),name='login' ),
  path('currentuser/', CurrentUserView.as_view(),name='currentuser' ),
  path('logout/', LogoutView.as_view(),name='logout'),
]