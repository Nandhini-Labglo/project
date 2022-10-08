from django.shortcuts import render

# Create your views here.

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
import os
from .models import studentModel
# Today update
class StudentList(ListView):

	model = studentModel
	template_name = 'listview.html'

class StudentDetail(DetailView):

	model = studentModel
	template_name = 'detailview.html'
	

class StudentCreate(CreateView):

	model = studentModel
	fields = '__all__'
	template_name = 'create_form.html'
	success_url = 'http://127.0.0.1:8000/views/create/'
	
class StudentUpdate(UpdateView):

	model = studentModel
	fields = '__all__'
	template_name = 'update_form.html'
	success_url = ('http://127.0.0.1:8000/views/update/')
	
class StudentDelete(DeleteView):

	model = studentModel
	template_name = 'delete_form.html'
	success_url = 'http://127.0.0.1:8000/views/'
	

