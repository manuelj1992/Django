from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from devices.models import Device
from comments.forms import CommentForm
import stripe
from django.conf import settings


class HomeView(TemplateView):
    template_name = 'devices/home.html'

    def get_context_data(self, **kwargs):
        devices = Device.objects.all()
        return {'devices': devices}


class DeviceDetailView(DetailView):
    model = Device

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        return context


class DeviceBuyView(DetailView):
    model = Device
    template_name = 'devices/buy.html'

    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_API_KEY
        token = request.POST['stripeToken']
        device = self.get_object()

        charge = stripe.Charge.create(
            amount=device.price,
            currency='usd',
            description="cobro por {}".format(device.name),
            statement_descriptor="cobro",
            source=token
        )
        return render(request, 'devices/succes.html', {'debug_info': charge, 'product': device})