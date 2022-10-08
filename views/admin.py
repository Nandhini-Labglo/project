from django.contrib import admin

# Register your models here.

from views.models import studentModel


class studentAdmin(admin.ModelAdmin):
	list_display = ['id','Name','Roll_no','Address']
admin.site.register(studentModel,studentAdmin)
