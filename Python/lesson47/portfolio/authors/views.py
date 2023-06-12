from django.shortcuts import render
from .models import Author


def other_authors(request):
    authors = Author.objects.all()
    return render(request, 'authors/authors.html', {'authors': authors})
