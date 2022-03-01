"""from django.contrib.admin import options
from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import Model"""
from django.db import models
from django.core.validators import MinValueValidator


# Создаём модель товара
class Post(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,  # названия товаров не должны повторяться
    )
    description = models.TextField()

    time = models.DateTimeField(auto_now=True, auto_now_add=False)
    #time = models.TimeField(auto_now=False, auto_now_add=False)
    """quantity = models.IntegerField(
       validators=[MinValueValidator(0)],
    )"""
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news',  # все продукты в категории будут доступны через поле products
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'


#  создаём категорию, к которой будет привязываться товар
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # названия категорий тоже не должны повторяться

    def __str__(self):
        return f'{self.name.title()}'
