from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer, Borrower, Book
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils import timezone
from .forms import BorrowerForm

@login_required
def home(request):
    return render(request, 'library/home.html')

class BookCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'description']
    success_url = reverse_lazy('display_book')
    success_message = "%(title)s book successfully created!"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    ordering = ['id']

    def get_queryset(self):
        # result = super().get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Book.objects.filter(title__contains=query)
            if not postresult:
                postresult = Book.objects.filter(author__contains=query)
                if not postresult:
                    if query.isdecimal():
                        postresult = Book.objects.filter(id=query)
                    else:
                        postresult = Book.objects.filter(id=None)
            result = postresult
        else:
            result = Book.objects.all()
        return result
class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book

class BookUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'description']
    success_url = reverse_lazy('display_book')
    success_message = "%(title)s book successfully updated!"

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )

class BookDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('display_book')
    success_message = "Book successfully deleted!"

class CustomerCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Customer
    fields = ['first_name', 'last_name', 'address']
    success_url = reverse_lazy('display_customer')
    success_message = "%(first_name)s %(last_name)s customer successfully created!"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            first_name=self.object.first_name,
            last_name=self.object.last_name,
        )

class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    ordering = ['id']

    def get_queryset(self):
        # result = super().get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Customer.objects.filter(first_name__contains=query)
            if not postresult:
                postresult = Customer.objects.filter(last_name__contains=query)
                if not postresult:
                    if query.isdecimal():
                        postresult = Customer.objects.filter(id=query)
                    else:
                        postresult = Customer.objects.filter(id=None)
            result = postresult
        else:
            result = Customer.objects.all()
        return result

class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer

class CustomerUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ['first_name', 'last_name', 'address']
    success_url = reverse_lazy('display_customer')
    success_message = "%(first_name)s %(last_name)s customer successfully updated!"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            first_name=self.object.first_name,
            last_name=self.object.last_name,
        )

class CustomerDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('display_customer')
    success_message = "Customer successfully deleted!"

class BorrowerCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Borrower
    form_class = BorrowerForm
    success_url = reverse_lazy('display_borrower')
    success_message = "%(customer)s successfully borrowed %(book)s!"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            customer=self.object.customer,
            book=self.object.book,
        )

class BorrowerListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        query = self.request.GET.get('search')
        sort = self.request.GET.get('returned')
        if query:
            postresult = Borrower.objects.filter(customer__first_name__contains=query)
            if not postresult:
                postresult = Borrower.objects.filter(customer__last_name__contains=query)
                if not postresult:
                    postresult = Borrower.objects.filter(book__title__contains=query)
                    if not postresult:
                        if query.isdecimal():
                            postresult = Borrower.objects.filter(id=query)
                        else:
                            postresult = Borrower.objects.filter(id=None)
            result = postresult
        else:
            if sort:
                result = Borrower.objects.filter(returned=sort)
            else:
                result = Borrower.objects.filter(returned=False)
        return result

class BorrowerDetailView(LoginRequiredMixin, DetailView):
    model = Borrower

class BorrowerUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Borrower
    fields = ['customer', 'book', 'returned']
    success_url = reverse_lazy('display_borrower')
    success_message = "Status for %(customer)s - %(book)s successfully updated!"


    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            customer=self.object.customer,
            book=self.object.book,
        )

    def form_valid(self, form):
        if self.object.returned == True:
            form.instance.return_date = timezone.now()
        else:
            form.instance.return_date = None
        return super().form_valid(form)

class BorrowerDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Borrower
    success_url = reverse_lazy('display_borrower')
    success_message = "Borrow data successfully deleted!"