from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True , verbose_name='электронная почта')
    avatar = models.ImageField(upload_to='user/', verbose_name= 'аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name= 'страна', **NULLABLE)
    token = models.CharField(max_length=100, verbose_name='token', **NULLABLE) 
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        
    def __str__(self):
        return self.email
    
    
    