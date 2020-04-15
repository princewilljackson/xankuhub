from django.contrib import admin
from .models import ProductDetail, ProductDescription, ProductOwner, OwnerContact

# Register your models here.
admin.site.register(ProductDetail)
admin.site.register(ProductDescription)
admin.site.register(ProductOwner)
admin.site.register(OwnerContact)