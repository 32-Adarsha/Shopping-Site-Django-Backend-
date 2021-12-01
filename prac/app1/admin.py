from django.contrib import admin
from .models import UserProfile,ItemListed ,Comment ,cart

admin.site.register(UserProfile)
admin.site.register(ItemListed)
admin.site.register(Comment)
admin.site.register(cart)
# Register your models here.
