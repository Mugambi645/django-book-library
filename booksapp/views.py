from django.shortcuts import render,redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
@login_required
def addbook(request):
    """
    addbook function
    """
    if request.method=="POST":
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return redirect('home:index')  
    else:
        form=BookForm()
    return render(request, "books/add_book.html", {'form':form})


class BookDetailView(LoginRequiredMixin,DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'object'



def deletebook(request, id):
    book = get_object_or_404(Book, id=id) 
    book.delete()
    return redirect('home:index')


def category(request):
    return render(request, "books/category.html")