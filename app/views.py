from django.shortcuts import render
from django.views.generic import TemplateView
from app.forms import VoucherForm,VoucherAssignForm,MerchantForm,Consumer_Mobile
from app.models import Voucher,VoucherAssign
from random import choice
from string import ascii_uppercase
from django.utils import timezone
class VoucherCreation(TemplateView):
    def get(self,request):
        form=VoucherForm()
        return render(request,'index.html',{'form':form})
    def post(self,request):
        form=VoucherForm(request.POST)
        if form.is_valid():
            n=form.cleaned_data['n']
            price=form.cleaned_data['amount']
            startTime=form.cleaned_data['startTime']
            endTime=form.cleaned_data['endTime']
            for i in range(0,n):
                s=''.join(choice(ascii_uppercase) for i in range(10))
                u=Voucher(code=s,amount=price,startTime=startTime,endTime=endTime,redeemed=False,assigned=False)
                u.save()
            form=VoucherForm()
        args={'form':form,'text':"Vouchers Generated"}
        return render(request,'index.html',args)

class MerchantView(TemplateView):
    def get(self,request):
        form=MerchantForm()
        return render(request,'merchant.html',{'form':form})
    def post(self,request):
        form=MerchantForm(request.POST)
        if form.is_valid():
            code=form.cleaned_data['code']
           # t=tuple(code)
            #l=list(Voucher.objects.values_list('code'))
           # if t not in l:
             #   return render(request,'merchant.html',{'form':form,'text':"Voucher code is invalid"})
            u=Voucher.objects.get(code=code)
            if u.redeemed==True:
                return render(request,'merchant.html',{'form':form,'text':"Voucher Already Redeemed"})
            if u.assigned==False:
                return render(request,'merchant.html',{'form':form,'text':"Voucher Not Assigned yet"})
            u.redeemed=True
            u.save()
            u=VoucherAssign.objects.get(code=code)
            u.delete()
            return render(request,'merchant.html',{'form':form,'text':"Voucher redeemed succesfully"})


class ConsumerView(TemplateView):
    def get(self,request):
        form= Consumer_Mobile()
        return render(request,'login.html',{'form':form})
    def post(self,request):
        form=Consumer_Mobile(request.POST)
        if form.is_valid():
            mobile=form.cleaned_data['mobile']
        u=VoucherAssign.objects.get(mobile=mobile)
    
        return render(request,'login.html',{'text':u})


class consumer_with_codes(TemplateView):
    def get(self,request):
        form=VoucherAssignForm()
        return render(request,'index.html',{'form':form})
    def post(self,request):
        form=VoucherAssignForm(request.POST)
        if form.is_valid():
            mobile=form.cleaned_data['mobile']
            code=form.cleaned_data['code']
            u=Voucher.objects.get(code=code)
            if u.assigned==True:
                return render(request,'index.html',{'form':form,'text':"Voucher already Assigned"})
            u.assigned=True
            u.save()
            x=VoucherAssign(mobile=mobile,code=code)
            x.save()
            form=VoucherAssignForm()
        args={'form':form,'text':"Voucher Assigned"}
        return render(request,'index.html',args)
        




def get_voucher(request):
    data=Voucher.objects.all()
    x = timezone.now()
    d={'code':[],'amount':[],'startTime':[],'endTime':[],'redeemed':[]}
    for i in data:
        if i.startTime<=x and i.endTime>=x:
            d['code'].append(i.code)
            d['amount'].append(i.amount)
            d['startTime'].append(i.startTime)
            d['endTime'].append(i.endTime)
            d['redeemed'].append(i.redeemed)
    return render(request,"get_voucher.html",{'text':d})

        



