from django.shortcuts import render,redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
import operator
import itertools
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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




@login_required
def lsearch(request):
    query = request.GET['query']
    print(type(query))


    #data = query.split()
    data = query
    print(len(data))
    if( len(data) == 0):
        return redirect('home:index')
    else:
                a = data

                # Searching for It
                qs5 =models.Book.objects.filter(id__iexact=a).distinct()
                qs6 =models.Book.objects.filter(id__exact=a).distinct()

                qs7 =models.Book.objects.all().filter(id__contains=a)
                qs8 =models.Book.objects.select_related().filter(id__contains=a).distinct()
                qs9 =models.Book.objects.filter(id__startswith=a).distinct()
                qs10 =models.Book.objects.filter(id__endswith=a).distinct()
                qs11 =models.Book.objects.filter(id__istartswith=a).distinct()
                qs12 =models.Book.objects.all().filter(id__icontains=a)
                qs13 =models.Book.objects.filter(id__iendswith=a).distinct()




                files = itertools.chain(qs5, qs6, qs7, qs8, qs9, qs10, qs11, qs12, qs13)

                res = []
                for i in files:
                    if i not in res:
                        res.append(i)


                # word variable will be shown in html when user click on search button
                word="Searched Result :"
                print("Result")

                print(res)
                files = res




                page = request.GET.get('page', 1)
                paginator = Paginator(files, 10)
                try:
                    files = paginator.page(page)
                except PageNotAnInteger:
                    files = paginator.page(1)
                except EmptyPage:
                    files = paginator.page(paginator.num_pages)
   


                if files:
                    return render(request,'books/results.html',{'files':files,'word':word})
                return render(request,'books/results.html',{'files':files,'word':word})


	
class LEditView(LoginRequiredMixin,UpdateView):
	model = Book
	form_class = BookForm
	template_name = 'books/editbook.html'
	success_url = reverse_lazy('home:index')
	success_message = 'Data was updated successfully'

