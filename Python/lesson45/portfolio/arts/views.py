from django.shortcuts import render
from .models import Art


def main(request):
    arts = Art.objects.all()
    return render(request, 'arts/home.html', {'arts': arts})
