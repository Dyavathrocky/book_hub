from django.urls import path

from .views import OrdersPageView

# Create your views here.

urlpatterns = [
    path('', OrdersPageView.as_view(),name='orders')
]