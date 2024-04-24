from django.db import models
from django.utils.timezone import now
from django.db.models import CharField


# Create your models here.
class Registermodel(models.Model):
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=200)
    userid = models.CharField(max_length=200)
    password = models.IntegerField()
    mblenum = models.BigIntegerField()
    email = models.EmailField(max_length=400, null=True)

class AddressDetails(models.Model):
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100)
    pincode = models.IntegerField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    created_by = models.IntegerField(null=False, blank=False)
    created_date = models.DateField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateField(null=True, blank=True)

class ContactDetails(models.Model):
    mobno = models.BigIntegerField()
    emailid = models.EmailField(max_length=400, null=True)
    accountno = models.IntegerField()
    beneficiaryname = models.CharField(max_length=300)
    created_by = models.IntegerField(null=False, blank=False)
    created_date = models.DateField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateField(null=True, blank=True)


class VendorDtails(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    gst = models.CharField(max_length=200)
    pan = models.CharField(max_length=200)
    branch = models.CharField(max_length=300)
    Address_Details = models.ForeignKey(AddressDetails, on_delete=models.SET_NULL, null=True)
    Contact_Details = models.ForeignKey(ContactDetails, on_delete=models.SET_NULL, null=True)
    created_by = models.IntegerField(null=False, blank=False)
    created_date = models.DateField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateField(null=True, blank=True)