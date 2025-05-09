from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models


# Create your models here.

class BaseManager(models.Manager):
    """
    The base manager class
    """

    def get_queryset(self):
        """
        Won't show objects while is_delete is True
        """
        return super().get_queryset().filter(is_delete=False)

    def get_all(self):
        """
        Will get all objects
        """
        return super().get_queryset()


class BaseModel(models.Model):
    """
    The BaseModel class for interacting
    """
    objects = BaseManager()
    create_datetime = models.DateTimeField(auto_now_add=True, editable=False)
    modify_datetime = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True, editable=False)
    is_delete = models.BooleanField(default=False, editable=False)

    class Meta:
        """
        Won't save on database
        """
        abstract = True

    def delete(self, using=None, keep_parents=False):
        """
        Instead of completely deleting it will only set is_delete True
        :param keep_parents: Will not keep parents upon deletion
        :param using:
        """
        self.is_delete = True
        self.save()

    def undelete(self):
        """
        Restoring deleted data by setting is_delete False
        :return:
        """
        self.is_delete = False
        self.save()

    def active(self):
        """
        Setting is_active True to activating the data
        :return:
        """
        self.is_active = True
        self.save()

    def deactivate(self):
        """
        Setting is_active False to deactivating the data
        :return:
        """
        self.is_active = False
        self.save()


class BaseDiscount(models.Model):
    """
    Base Model for discounts.
    """
    amount = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=70)
    type = models.CharField(max_length=5, choices=[('cent', 'percent'), ('val', 'value')], null=False)

    class Meta:
        """
        Won't save on database
        """
        abstract = True


class MyUserManager(UserManager):
    """
    Creating a new user manager for our custom django user.
    """

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        """
        Override this method to create customizing django superuser.
        :param username: Allow none
        :param email:
        :param password:
        :param extra_fields:
        :return:
        """
        username = extra_fields['phone']
        return super().create_superuser(username, email, password, **extra_fields)

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        """
        Override this method to create customizing django user.
        :param username: Allow none
        :param email:
        :param password:
        :param extra_fields:
        :return:
        """
        username = extra_fields['phone']
        return super().create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    """
    Customized django user and takes phone number instead of username
    """
    USERNAME_FIELD = 'phone'
    phone = models.CharField(max_length=15, unique=True)
    objects = MyUserManager()

    def save(self, *args, **kwargs):
        """
        Use phone number instead of username
        :return:
        """
        self.username = self.phone
        # if User.objects.filter(id=self.id):
        #     self.set_password(self.password)
        super().save(*args, **kwargs)
