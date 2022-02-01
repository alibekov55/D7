from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('products/', include('simple_app.urls')),  # делаем так, чтобы все адреса из нашего приложения (simple_app/urls.py) сами автоматически подключались, когда мы их добавим.
    path('news/', include('news.urls')),
]