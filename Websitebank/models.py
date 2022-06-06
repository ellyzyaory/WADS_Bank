from string import digits
from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank = False)
    last_name = models.CharField(max_length= 100,blank = False)
    pin = models.CharField(max_length=6,blank = False)
    card_no = models.CharField(primary_key = True,max_length=16, blank = False, unique=True)
    balance = models.DecimalField(max_digits=15, decimal_places=3,blank= False)
    
# class profilepic(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default = None, upload_to = "profile_pics")

#     def str(self):
#         return f'{self.user.username} Profile'

# class photos(models.Model):
#     id = models.AutoField(primary_key=True)
#     image = models.ImageField(upload_to='nodeflux_photos/')


class payments(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id = models.UUIDField(default=uuid.uuid4, editable=False , primary_key= True)
    receiver_no = models.CharField(max_length=16, blank = False)
    amount = models.DecimalField(max_digits=15, decimal_places=3,blank= False)
    notes = models.CharField(max_length = 100, blank = False)
