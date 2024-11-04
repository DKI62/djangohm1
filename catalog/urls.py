from django.urls import path
from catalog import views
from catalog.views import index

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('contacts/', views.contacts, name='contacts'),  # Страница контактов
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('menu/', index, name='menu'),
]
