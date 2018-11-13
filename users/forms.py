from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import OutLet, Adminstrator,User


class OutLetCreationForm(UserCreationForm):
    """ form for creatin oulets"""
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_outlet = True
        user.save()
        oulet = OutLet.objects.create(user=user)
        return user


class AdminstratorCreationForm(UserCreationForm):
    """ form for creating admins"""
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_adminstrator = True
        user.save()
        adminstrator = Adminstrator.objects.create(user=user)
        return user
