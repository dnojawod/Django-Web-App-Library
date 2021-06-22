from django.contrib import admin
from .models import Customer, Book, Borrower

admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Borrower)
