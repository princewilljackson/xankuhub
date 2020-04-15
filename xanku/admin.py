from django.contrib import admin
from .models import ItemDetail, ItemDescription, ItemOwner, OwnerContact

# Register your models here.
admin.site.register(ItemDetail)
admin.site.register(ItemDescription)
admin.site.register(ItemOwner)
admin.site.register(OwnerContact)