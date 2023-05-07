from django.shortcuts import render


def index(request):
    context = {
        'title': 'Webpage Title',
        'description': 'Webpage Description',
        'content': 'Hello World!',
    }

    return render(request, 'web/index.html', context)
