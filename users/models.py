from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_outlet = models.BooleanField(default=False)
    is_adminstrator = models.BooleanField(default=False)


class OutLet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    

class Adminstrator(models.Model):
	user =models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    