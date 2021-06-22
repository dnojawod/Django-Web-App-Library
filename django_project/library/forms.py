from django import forms
from .models import Book, Borrower
from django.db.models import Q

class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['customer', 'book']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        borrowed = Borrower.objects.filter(returned=False)
        borrowed = borrowed.values_list('book', flat=True)
        books = Book.objects.filter(~Q(id__in=borrowed))
        self.fields['book'].queryset = books