from django.forms import ModelForm, BooleanField  # Импортируем true-false поле
from .models import Products


class ProductForm(ModelForm):
    check_box = BooleanField(label='Ало, Галочка!')  # добавляем галочку, или же true-false поле

    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'category', 'quantity', 'check_box']  # не забываем включить галочку в поля, иначе она не будет показываться на странице!