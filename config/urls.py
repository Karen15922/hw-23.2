# config/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Импортируйте модуль admin
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),  # URL-маршрут для административной панели Django
    path('', include('catalog.urls', namespace='catalog')),  # URL-маршруты для приложения catalog
    path('blog/', include('blog.urls', namespace='blog')),  # URL-маршруты для приложения blog
    path('users/', include('users.urls', namespace='users'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
