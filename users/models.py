from django.db import models
from django.contrib.auth.models import AbstractUser
from goods.models import NULLABLE


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', **NULLABLE, verbose_name='Аватар')

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
