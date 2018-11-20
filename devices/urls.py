from django.urls import path
from devices.views import HomeView, ProductDetailView, ProductBuyView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("devices/<slug:slug>", ProductDetailView.as_view(), name="detail"),
    path("devices/<slug:slug>/buy", ProductBuyView.as_view(), name="buy")
]