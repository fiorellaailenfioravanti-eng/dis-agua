from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    imagen_perfil = models.ImageField(upload_to='perfiles/', null=True, blank=True,default='usuarios/default.jpg')
    def get_absolute_url(self):

        return reverse('inicio')
    