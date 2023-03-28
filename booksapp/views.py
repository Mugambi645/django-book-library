from django.shortcuts import render,redirect
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

