from django.shortcuts import render
from .models import ItemDetail, ItemDescription, ItemOwner, OwnerContact

# Create your views here.
def home(request):
    """Renders the home.html file"""
    return render(request, 'home.html')

def item_details(request):
    """Renders all Item detail objects from the database on the html item file."""
    item_names = ItemDetail.objects.order_by('item_name')
    context = {'item_name': item_names}
    return render(request,'item.html', context)

def item_description(request):
    """Renders all item description objects from the database on the html descriptions file."""
    item_descriptions = ItemDescription.objects.order_by('item_name')
    context = {'item_description': item_descriptions}
    return render(request, 'descriptions.html', context)

def item_owner(request):
    """Renders all item owner objects from the database on the html owner file."""
    owners = ItemOwner.objects.order_by('item_name')
    context = {'item_owner': owners}
    return render(request, 'owner.html', context)

def owner_contact(request):
    """Renders all owner contact objects from the database on the html contact file."""
    item_contacts = OwnerContact.objects.order_by('item_name')
    context = {'owner_contact': item_contacts}
    return render(request, 'contact.html', context)