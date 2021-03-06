from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class UserAccounts(AbstractUser):
    id = models.BigAutoField(primary_key = True)
    username = None
    shortname=models.CharField('name', max_length=12, null=False)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=12, null=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    def __str__(self):
        return self.shortname


class ProfilePicture(models.Model):
    id = models.BigAutoField(primary_key = True)
    user = models.OneToOneField(UserAccounts, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='profile', default='avatar.jpg')


class Address(models.Model):
    id = models.BigAutoField(primary_key = True)
    user = models.ForeignKey(UserAccounts, on_delete = models.CASCADE)
    address = models.TextField()
    country = models.CharField(max_length = 60)
    state = models.CharField(max_length = 60)
    city = models.CharField(max_length = 60)
    phone = models.IntegerField()
    pincode = models.IntegerField()
    
