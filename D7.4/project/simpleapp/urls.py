from django.urls import path
from .views import Products, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView  # импортируем наше представление

from django.views.decorators.cache import cache_page

urlpatterns = [# path означает "путь". В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', Products.as_view()), # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', cache_page(100)(ProductDetailView.as_view()), name='product_detail'), # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]

"""from django.urls import path
from .views import ProductList, ProductDetail  # импортируем наше представление

urlpatterns = [# path означает "путь". В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', ProductList.as_view()),# т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', ProductDetail.as_view()), # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
]"""