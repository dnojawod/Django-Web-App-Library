from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book-create/', views.BookCreateView.as_view(), name='create_book'),
    path('book-display/<int:pk>/', views.BookDetailView.as_view(), name='detail_book'),
    path('book-display/<int:pk>/update/', views.BookUpdateView.as_view(), name='update_book'),
    path('book-display/<int:pk>/delete/', views.BookDeleteView.as_view(), name='delete_book'),
    path('book-display/', views.BookListView.as_view(), name='display_book'),
    path('customer-create/', views.CustomerCreateView.as_view(), name='create_customer'),
    path('customer-display/', views.CustomerListView.as_view(), name='display_customer'),
    path('customer-display/<int:pk>/', views.CustomerDetailView.as_view(), name='detail_customer'),
    path('customer-display/<int:pk>/update/', views.CustomerUpdateView.as_view(), name='update_customer'),
    path('customer-display/<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='delete_customer'),
    path('borrow/', views.BorrowerCreateView.as_view(), name='create_borrower'),
    path('borrow-status/', views.BorrowerListView.as_view(), name='display_borrower'),
    path('borrow-status/<int:pk>/', views.BorrowerDetailView.as_view(), name='detail_borrower'),
    path('borrow-status/<int:pk>/update/', views.BorrowerUpdateView.as_view(), name='update_borrower'),
    path('borrow-status/<int:pk>/delete/', views.BorrowerDeleteView.as_view(), name='delete_borrower'),
]