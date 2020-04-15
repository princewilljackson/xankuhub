from django.shortcuts import render
from .models import ProductDetail, ProductDescription, ProductOwner, OwnerContact

# Create your views here.
def products(request):
    """Renders the product html file."""
    return render(request, 'products.html')

def product_detail(request):
    """Renders all product detail objects from the database on the html product list file."""
    product_list = ProductDetail.objects.order_by('product_name')
    context = {'products': product_list}
    return render(request, 'product_list.html', context)

def product_description(request):
    """Renders all product description objects from the database on the html product description file."""
    description_list = ProductDescription.objects.order_by('product_name')
    context = {'descriptions': description_list}
    return render(request, 'product_descriptions.html', context)

def product_owner(request):
    """Renders all product owner objects from the database on the html product owner."""
    owner_list = ProductOwner.objects.order_by('product_name')
    context = {'owners': owner_list}
    return render(request, 'product_owner.html', context)

def owner_contact(request):
    """Renders all owner contact objects from the database on the html owner detail file."""
    owner_detail = OwnerContact.objects.order_by('product_name')
    context = {'details': owner_detail}
    return render(request, 'owner_detail.html', context)