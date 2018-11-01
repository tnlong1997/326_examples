from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.BookListView.as_view(), name="books"),
    path("book/<int:pk>", views.BookDetailView.as_view(), name="book-detail"),
]

urlpatterns += [
    # NEW 14
    path("mybooks/", views.LoanedBooksByUserListView.as_view(), name="my-borrowed"),
    path("allbooks/", views.AllBorrowedBooks.as_view(), name="all-borrowed"),
]
