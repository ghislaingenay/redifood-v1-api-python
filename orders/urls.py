from django.urls import path

from orders.views import TestView

urlpatterns = [
  path('test', TestView.as_view(), name='test-view'),
]