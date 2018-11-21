from django.urls import path
from devices.views import HomeView, DeviceDetailView, DeviceBuyView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("devices/<slug:slug>",    DeviceDetailView.as_view(), name="detail"),
    path("devices/<slug:slug>/buy", DeviceBuyView.as_view(), name="buy")
]