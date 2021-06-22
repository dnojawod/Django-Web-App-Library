from django.db import models
from django.utils import timezone
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(default='Not Provided')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('book_main')

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField(default='Not Provided')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Borrower(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)
    returned = models.BooleanField(default=False)

    class Meta:
        ordering = ["-issue_date"]

    def __str__(self):
        return f'{self.customer} borrowed {self.book}'