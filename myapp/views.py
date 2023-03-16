from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'myapp/index.html', data)

def about(request):
    return render(request, 'myapp/about.html')
