from django import forms

class VoucherForm(forms.Form):
    n= forms.IntegerField()
    amount= forms.FloatField()
    startTime = forms.DateTimeField()
    endTime = forms.DateTimeField()

class VoucherAssignForm(forms.Form):
    mobile=forms.CharField(max_length=10)
    code=forms.CharField(max_length=10)

class MerchantForm(forms.Form):
    code=forms.CharField(max_length=10)
    
class Consumer_Mobile(forms.Form):
    mobile=forms.CharField(max_length=10)

