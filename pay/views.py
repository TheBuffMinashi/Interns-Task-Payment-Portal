from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import stripe

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from pay.models import Payments,User
from pay.serializers import PaymentSerializer

# Create your views here.


def index(request):
    if request.user.id:
        return render(request, "pay/index.html",{
                "user": request.user
            })
    else:
        return HttpResponseRedirect(reverse('api:login'))


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
                success_url=domain_url + 'success/?session_id={CHECKOUT_SESSION_ID}',
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
            userCreate  = request.user
            newpayment = Payments(Amount=checkout_session['amount_total'],UserPay=userCreate,Transaction=checkout_session['id'])
            newpayment.save()
            return JsonResponse({'sessionId': checkout_session['id']})
            return JsonResponse({'sessionId': userCreate})
        except Exception as e:
            return JsonResponse({'error': str(e)})

def success(request):
    sessionId = request.GET.get('session_id', None)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session_info =stripe.checkout.Session.retrieve(sessionId,)
    amount_total =session_info['amount_total']
    payment_status =session_info['payment_status']
    status =session_info['status']
    payment_intent =session_info['payment_intent']
    if payment_status == "paid" and status=="complete":
        try:
            Pid = Payments.objects.get(Transaction=sessionId)
            Pid.Transaction = payment_intent
            Pid.Status = True
            Pid.save(update_fields=["Transaction", "Status"])
            return render(request, "pay/success.html",{
                "PaymentOK": "Payment Confirmed.",
                "amount_total": amount_total
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})    
    else:
        return render(request, "pay/success.html",{
            "PaymentNOK": "Payment not confirmed!"
        })
    # chesession =stripe.checkout.Session.retrieve("cs_test_a1e1dXpHs2upyHcc5hrhQnMGmiqXbac60KbmPk7ko6TDMzIwc3lWzAenCx",)
    # return render(request, "pay/success.html")

def cancel(request):
 return render(request, "pay/cancel.html")


 #########API Payments ############

# GET /api/v1/get-all-pay/
class GetAllPay(APIView):
    def get(self, request):
        query = Payments.objects.all()
        serializers = PaymentSerializer(query, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

# GET /api/v1/search-pay/?user=admin
class SearchPay(APIView):
    def get(self, request):
        user_get = request.GET['user']
        try:
            userinfo = User.objects.get(username=user_get)
            Uid = userinfo.id
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        query = Payments.objects.filter(UserPay=Uid)
        if query:
            serializers = PaymentSerializer(query, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)