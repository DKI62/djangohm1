from django.shortcuts import render


def index(request):
    """Представление для главной страницы."""
    return render(request, 'index.html')


def contacts(request):
    """Представление для страницы контактов."""

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name}, ({email}): {message}')
    return render(request, 'contacts.html')
