from django.db import models
from django.contrib.auth.models import User
from django.utils import tree


class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    pic = models.ImageField(upload_to = 'images' , default = 'Z:/Django/usercreationform/prac/image/images/default.png')
    company_name = models.CharField(max_length=100 , blank=True )
    valid_seller = models.BooleanField(default=False)
    bio          = models.TextField(max_length=500 , blank=True)

    def __str__(self):
        return self.user.username
    
class ItemListed(models.Model):
    Gender_Choice =[
        ('Male' , 'Male'),
        ('Female' , 'Female'),
        ('Unisex','Unisex'),
    ]
    user = models.ForeignKey(UserProfile , on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50 , blank=True)
    pic =  models.ImageField(upload_to='itemImages' , blank=False )
    item_detail =models.TextField(max_length=255 , blank=True , null=True )
    likes = models.IntegerField(verbose_name='likes')
    discount_ammount = models.IntegerField(blank=True , null=True)
    price = models.IntegerField(default=0)
    gender = models.CharField(max_length=6,choices=Gender_Choice, default='Unisex')

    def __str__(self):
        return self.item_name
    
class Comment(models.Model):
    ItemListed = models.ForeignKey(ItemListed , on_delete=models.CASCADE)
    user_iden = models.CharField(max_length=150)
    comments = models.CharField(max_length=150)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user_iden

class cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    item = models.ForeignKey(ItemListed , on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True , default=0)
    
    def __str__(self):
        return str(self.item)