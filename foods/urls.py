from django.urls import path
from .views import GetFoodsView

urlpatterns = [
  path('all', GetFoodsView.as_view(), name='all-foods'),
]