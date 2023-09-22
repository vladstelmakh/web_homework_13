from django.shortcuts import render, get_object_or_404
from .models import Author, Quote
def index(request):
    return render(request, 'quotes/index.html')
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'quotes/author_list.html', {'authors': authors})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    quotes = Quote.objects.filter(author=author)
    return render(request, 'quotes/author_detail.html', {'author': author, 'quotes': quotes})

def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/quote_list.html', {'quotes': quotes})