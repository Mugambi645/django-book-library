from django.urls import path
from . import views
app_name = "booksapp"
urlpatterns = [
    path('addbook/', views.addbook, name='addbook'),
    path('detail/<int:pk>', views.BookDetailView.as_view(), name='detail'),
]