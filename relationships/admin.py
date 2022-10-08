from django.contrib import admin

# Register your models here.

from relationships.models import *


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Roll_no', 'Address',
                    'upload_image', 'created_date', 'modified_date']


admin.site.register(Student, StudentAdmin)


class MarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'mark',
                    'student', 'created_by', 'modified_by']
    exclude = ('created_by',  'modified_by')
    readonly_fields = ("created_date", "modified_date")


admin.site.register(Mark, MarkAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name']


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'Book_Name']


admin.site.register(Book, BookAdmin)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'Title', 'Date_of_Publish']


admin.site.register(Publisher, PublisherAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Email', 'Mobile']


admin.site.register(Person, PersonAdmin)


class AadharAdmin(admin.ModelAdmin):
    list_display = ['id', 'Aadhar_no']


admin.site.register(Aadhar, AadharAdmin)
