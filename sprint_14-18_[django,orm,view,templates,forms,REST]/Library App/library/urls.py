from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('books/', include('book.urls')),
    path('authors/', include('author.urls')),
    path('orders/', include('order.urls')),
    path('api/v1/', include('api.urls')),
]
