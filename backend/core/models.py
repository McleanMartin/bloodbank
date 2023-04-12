from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self,email,date_of_birth,phone_number,national_ID,password=None):
        if not email:
            raise ValueError('user must have an email address')
        
        user = self.model(
            email = self.normalize_email(email),
            date_of_birth = date_of_birth,
            phone_number = phone_number,
            national_ID = national_ID,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,phone_number,national_ID,date_of_birth,password=None):
        user  = self.create_user(
            email,
            password=password,
            phone_number=phone_number,
            national_ID = national_ID,
            date_of_birth = date_of_birth,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=254)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=50)
    national_ID = models.CharField(unique=True,max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'date_of_birth',
        'phone_number',
        'national_ID'
    ]

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin

class Location(models.Model):
    center = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("location")
        verbose_name_plural = ("locations")

    def __str__(self):
        return self.center


class Donor_Card(models.Model):
    id = models.AutoField(primary_key=True)
    card_num = models.CharField(max_length=50)
    qr_code = models.FileField(upload_to="assets/QR", max_length=100)
    holder = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.card_num
    

class Alerts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    center = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    
