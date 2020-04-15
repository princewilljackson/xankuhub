from django.db import models

# Create your models here.
class ItemDetail(models.Model):
    """Student details."""
    item_name = models.CharField(max_length=50)
    Item_photo = models.ImageField(upload_to='static/images')
    item_price = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = "Item Details"

    def __str__(self):
        """Returns a string representation."""
        return self.item_name



class ItemDescription(models.Model):
    """Simple represention of course choices."""
    item_name = models.ForeignKey(ItemDetail, models.CASCADE)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Item Description"

    def __str__(self):
        """Returns a string representation."""
        return self.description



class ItemOwner(models.Model):
    """Simple representationn of books for selection course"""
    item_name = models.ForeignKey(ItemDetail, models.CASCADE)
    owner_name = models.CharField(max_length=20)
    owner_email = models.EmailField()


    class Meta:
        verbose_name_plural = "Owner Detail"


    def __str__(self):
        """Returns a string representation."""
        return self.owner_name


class OwnerContact(models.Model):
    """Simple representation for exam date."""
    item_name= models.ForeignKey(ItemDetail, models.CASCADE)
    owner_name = models.ForeignKey(ItemOwner, models.CASCADE)
    owner_country = models.CharField(max_length=10)


    class Meta:
        verbose_name_plural = "Owner Contact"


    def __str__(self):
        """Returns a string representation."""
        return self.owner_country

