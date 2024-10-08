from django.urls import path
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('contacts/', views.contacts, name='contacts'),  # Страница контактов
]
