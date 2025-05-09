from django.db import models
from django.db.models import PROTECT
from django.utils.text import slugify

from core.models import BaseModel, BaseDiscount


class Discount(BaseDiscount):
    """
    The model for discount, this will not have any extra fields.
    """

    def discounted_price(self, price: int) -> int:
        """
        Calculate the price after discount
        :param price: product price
        :return: discounted price
        """
        if self.type == 'val':
            if price < self.amount:
                # More discount than price
                return price
            return int(price - int(self.amount))
        elif self.type == "cent":
            return price - int((self.amount / 100) * price)

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'

    def __str__(self):
        return f"Discount type: {self.type} Amount: {self.amount}"


class Brand(BaseModel):
    """
    The model for brands.
    """
    discount = models.OneToOneField(to=Discount, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=50, default='', help_text="Name of brand")
    image = models.FileField(null=True, default=None, upload_to='brand/', blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Brand: {self.name}"


class Category(BaseModel):
    """
    The model for Categories.
    """
    discount = models.OneToOneField(to=Discount, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=50, default='', help_text="Name of Category")
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Parent Category', null=True, blank=True)
    image = models.FileField(null=True, default=None, upload_to='category/', blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Category: {self.name}"

    class Meta:
        verbose_name_plural = 'Categories'


class Product(BaseModel):
    """
    The model for products.
    """
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)
    brand = models.ForeignKey(to=Brand, on_delete=models.PROTECT)
    discount = models.OneToOneField(to=Discount, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=50, default='', help_text="Name of product")
    image = models.FileField(null=True, default=None, upload_to='product/', blank=True)
    price = models.PositiveIntegerField(default=0, null=False, help_text="Price of product")
    description = models.CharField(max_length=250, help_text="Product description", default="description")
    count = models.PositiveIntegerField(default=1, null=False, help_text="Count of product")
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.brand.name} {self.name} with price of {self.price}"

    @property
    def calc_discounted(self):
        if self.discount is not None:
            return self.discount.discounted_price(int(self.price))
        else:
            return self.price


class Comment(BaseModel):
    """
    The model for comments.
    """
    content = models.CharField(max_length=250, null=True, default='So far so good', help_text="Comment text")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"Comment: {self.content[:20]}"
