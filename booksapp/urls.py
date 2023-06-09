from django.urls import path
from . import views
app_name = "booksapp"
urlpatterns = [
    path('addbook/', views.addbook, name='addbook'),
    path('detail/<int:pk>', views.BookDetailView.as_view(), name='detail'),
    path('deletebook/<int:pk>/', views.deletebook, name='deletebook'),
    path("category",views.category, name="category" ),
    path('search/', views.lsearch, name='search'),
    path('updatebook/<int:pk>', views.LEditView.as_view(), name='updatebook'),
]