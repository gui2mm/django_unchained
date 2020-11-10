from django.shortcuts import render


def index(request):
    context = {"nome": "Guilherme"}
    return render(request, 'content.html', context)
