from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):

    Name = models.CharField(max_length=30, null=True)
    Roll_no = models.IntegerField(null=True)
    Address = models.TextField(null=True)
    upload_image = models.ImageField(upload_to='images/', null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "{} {}".format(self.id, self.Name)


class Mark(models.Model):

    subject = models.CharField(max_length=30, null=True)
    mark = models.IntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)
    created_by = models.CharField(max_length=30, null=True)
    modified_by = models.CharField(max_length=30, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {} {}".format(self.id, self.subject, self.mark, self.student)


class Author(models.Model):

    Name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return "{} {}".format(self.id, self.Name)


class Book(models.Model):

    Book_Name = models.CharField(max_length=30, null=True)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return "{} {}".format(self.id, self.Book_Name)


class Publisher(models.Model):

    Title = models.CharField(max_length=30, null=True)
    Date_of_Publish = models.DateField()
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.id, self.Title, self.Date_of_Publish)


class Person(models.Model):
    Name = models.TextField(max_length=100, null=True)
    Email = models.EmailField(null=True)
    Mobile = models.TextField(max_length=100, null=True)

    def __str__(self):
        return "{} {} {} {}".format(self.id, self.Name, self.Email, self.Mobile)


class Aadhar(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    Aadhar_no = models.TextField(max_length=100)

    def __str__(self):
        return "{} {} {}".format(self.id, self.Person, self.Aadhar_no)


class Meta:
    unique_together = ['Person', 'Aadhar']
