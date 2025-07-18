from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        user = self.model(
            email = email,
            username = username,
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.is_active = True
        user.save(using =self._db)
        return user
    
    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            email = email,
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password
        )
        user.is_admin = True
        user.is_staff =True
        user.is_active = True
        user.save(using =self._db)
        return user




class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =['username','first_name', 'last_name']

    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin