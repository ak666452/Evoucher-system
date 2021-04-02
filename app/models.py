from django.db import models

class Voucher(models.Model):
	code=models.CharField(max_length=10)
	amount= models.FloatField()
	startTime = models.DateTimeField()
	endTime = models.DateTimeField()
	redeemed = models.BooleanField(default=False)
	assigned =models.BooleanField(default=False)

class VoucherAssign(models.Model):
	mobile=models.CharField(max_length=10)
	code= models.CharField(max_length=10)
