from django.urls import path,include
from app import views
from app.views import VoucherCreation,consumer_with_codes,MerchantView, ConsumerView
urlpatterns = [
    path('voucher/',VoucherCreation.as_view(),name="storing data" ),
    path('Codes/',views.get_voucher,name="getting all codes" ),
    path('voucher_assign/',consumer_with_codes.as_view(),name="assigning codes" ),
    path('Merchant/',MerchantView.as_view(),name="merchant view" ),
    path('Consumer/',ConsumerView.as_view(),name="Consumer view" ),


]