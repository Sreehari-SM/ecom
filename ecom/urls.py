
from django.contrib import admin
from django.urls import path, include, re_path
from django.urls import path

admin.site.site_header = "Ecom Accounts Admin"
admin.site.site_title = "Ecom Accounts Admin"
admin.site.index_title = "Welcome to Ecom Admin Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users', include('api.v1.users.urls', namespace='api_v1_users')),
    path('api/v1/products', include('api.v1.products.urls', namespace='api_v1_products')),
]
