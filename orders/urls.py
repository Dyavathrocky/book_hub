from django.urls import path

from .views import OrdersPageView , ChargeView

# Create your views here.

urlpatterns = [
    path('charge/', ChargeView, name='charge'),
    path('', OrdersPageView.as_view(),name='orders'),
]