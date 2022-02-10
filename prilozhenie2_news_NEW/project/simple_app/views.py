from django.shortcuts import render
from django.views.generic import View, DetailView  # импортируем уже знакомый generic
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from .models import Product
from .filters import ProductFilter  # импортируем недавно написанный фильтр


# Create your views here.
class Products(View):
    def get(self, request):
        products = Product.objects.order_by('-price')
        p = Paginator(products, 1)  # создаём объект класса пагинатор, передаём ему список наших товаров и их количество для одной страницы
        products = p.get_page(request.GET.get('page', 1))  # берём номер страницы из get-запроса. Если ничего не передали, будем показывать первую страницу.
        # теперь вместо всех объектов в списке товаров хранится только нужная нам страница с товарами
        data = {
            'products': products,
                }
        return render(request, 'products.html', data)


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'

"""class Products(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1  # поставим постраничный вывод в один элемент

    def get_context_data(self,**kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET,queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context"""


"""from django.shortcuts import render
from django.views import View # импортируем простую вьюшку
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from .models import Product

from django.views.generic import ListView, DetailView
from datetime import datetime


class ProductsList(ListView):
    model = Product  # указываем модель, объекты которой мы будем выводить
    template_name = 'products.html'  # указываем имя шаблона, где будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'products'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Product.objects.order_by('-id')  # настроили пораметр отображения более новый продукт

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словаря и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context

class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


# В отличие от дженериков, которые мы уже знаем, код здесь надо писать самому, переопределяя типы запросов (например гет или пост, вспоминаем реквесты из модуля C5)
class Products(View):

    def get(self, request):
        products = Product.objects.order_by('-price')
        p = Paginator(products, 1)  # создаём объект класса пагинатор, передаём ему список наших товаров и их количество для одной страницы

        products = p.get_page(request.GET.get('page', 1))  # берём номер страницы из get-запроса. Если ничего не передали, будем показывать первую страницу.
        # теперь вместо всех объектов в списке товаров хранится только нужная нам страница с товарами

        data = {
            'products': products,
        }
        return render(request, 'product_list.html', data)"""