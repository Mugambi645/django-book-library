from django.shortcuts import render
from booksapp.models import Book
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
# Create your views here.
def index(request):

    books = Book.objects.all()
    return render(request, "index.html", {"books": books})