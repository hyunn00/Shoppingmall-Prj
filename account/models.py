from typing import Reversible
from django.db import models

# Create your models here.
class Member(models.Model) :
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=128)
    address = models.CharField(max_length=200)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'member'
        verbose_name_plural = "members"

    def __str__(self):
        return self.username