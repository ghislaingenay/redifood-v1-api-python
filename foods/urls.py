from django.urls import path
from .views import GetFoodsView

urlpatterns = [
  path('all', GetFoodsView.as_view(), name='all-foods'),
  path('<int:food_id>', GetFoodsView.as_view(), name='food-id'),
]