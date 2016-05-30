from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')
        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        account = self.model(email=self.normalize_email(email), username=kwargs.get('username'))
        account.set_password(password)
        account.save()
        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)
        account.is_admin = True
        account.save()
        return account

class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    is_admin = models.BooleanField(default=False)
    #Creation Date of user
    created_at = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)

    objects = AccountManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

class Post(models.Model):
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	creationDate = models.DateTimeField(auto_now=True,auto_now_add = False)
	updateDate = models.DateTimeField(auto_now=False,auto_now_add = True)

class Comment(models.Model):
	user = models.ForeignKey(Account, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	text = models.TextField()

