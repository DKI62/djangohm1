from django.shortcuts import render, get_object_or_404
from .models import Product


def index(request):
    products = Product.objects.all()  # Получаем все товары
    context = {'object_list': products}  # Формируем контекст для шаблона
    return render(request, 'catalog/index.html', context)  # Возвращаем шаблон с контекстом


def contacts(request):
    """Представление для страницы контактов."""

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name}, ({email}): {message}')
    return render(request, 'catalog/contacts.html')


def product_detail(request, pk):
    # Получаем товар по его первичному ключу (pk)
    product = get_object_or_404(Product, pk=pk)

    # Передаем информацию о товаре в шаблон через контекст
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)