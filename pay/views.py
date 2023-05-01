from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import stripe


# Create your views here.

def index(request):
    return render(request, "pay/index.html")


@csrf_exempt
def pay_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def pay_request(request):
    if request.method == 'GET':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        domain_url = 'http://localhost:8000/'
        try:
            checkout_session = stripe.checkout.Session.create(
                # success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                success_url=domain_url + 'success/',
                cancel_url=domain_url + 'cancelled/',
                line_items=[
                    {
                        'price': 'price_1Mx8KpHQIdOmxz7tKbL8WJnu',
                        'quantity': 1,
                    },
                ],
                payment_method_types=['card'],
                mode="payment",
            )
            # return JsonResponse(checkout_session, safe=False)
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

def success(request):
 return render(request, "pay/success.html")

def cancel(request):
 return render(request, "pay/cancel.html")
