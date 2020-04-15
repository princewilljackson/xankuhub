from django.db import models

# Create your models here.
class ProductDetail(models.Model):
    """Student details."""
    product_name = models.CharField(max_length=50)
    product_type = models.CharField(max_length=20)
    product_price = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = "Product Details"

    def __str__(self):
        """Returns a string representation."""
        return self.product_name



class ProductDescription(models.Model):
    """Simple represention of course choices."""
    product_name = models.ForeignKey(ProductDetail, models.CASCADE)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Description"

    def __str__(self):
        """Returns a string representation."""
        return self.description



class ProductOwner(models.Model):
    """Simple representationn of books for selection course"""
    product_name = models.ForeignKey(ProductDetail, models.CASCADE)
    product_owner = models.CharField(max_length=20)
    owner_email = models.EmailField()


    class Meta:
        verbose_name_plural = "Owner Detail"


    def __str__(self):
        """Returns a string representation."""
        return self.product_owner


class OwnerContact(models.Model):
    """Simple representation for exam date."""
    product_name= models.ForeignKey(ProductDetail, models.CASCADE)
    product_owner = models.ForeignKey(ProductOwner, models.CASCADE)
    owner_country = models.CharField(max_length=10)


    class Meta:
        verbose_name_plural = "Owner Contact"


    def __str__(self):
        """Returns a string representation."""
        return self.owner_country

