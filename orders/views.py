import stripe
from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import TemplateView

class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def ChargeView(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount = 3900,
            currency = 'usd',
            description = 'purchase all books',
            source = request.POST['stripeToken']

        )
        return render(request, 'orders/charge.html')

     
"""def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['number'] = random.randrange(1, 100)
    return context"""

