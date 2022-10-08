from django.shortcuts import render,redirect

# Create your views here.
from django.http import *
from relationships.models import *
from relationships.forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
import json


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('list_table')
            else:
                form = AuthenticationForm()
                messages.info(request, "Invalid username or password.")
                return render(request, 'registration/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required(redirect_field_name='login',login_url='login')
def logout_request(request):
	logout(request)
	return redirect('login')

@login_required(redirect_field_name='list_table',login_url='login')
def list_table(request):
    stu_obj = Student.objects.all()
    return render(request, 'list_table.html', {'form': stu_obj})

def send_jsons(request):
	results = Student.objects.values()
	json_res = []
	for result in results:
		json_res.append(result)
		output = json.dumps(json_res, sort_keys=True, indent=4, default=str)
	return HttpResponse(output, content_type="application/json")

def add_table(request):
    Student = StudentForm(request.POST or None, request.FILES or None)
    if Student.is_valid():
        Student.save()
    return render(request, 'add_table.html', {'form': Student})

def update_table(request, id):
    stu_obj = Student.objects.get(id=id)
    form = StudentForm(request.POST or None,
                       request.FILES or None, instance=stu_obj)
    if form.is_valid():
        form.save()
    return render(request, 'update_table.html', {'form': form})

def delete_table(request, id):
    stu_obj = Student.objects.get(id=id)
    stu_obj.delete()
    return HttpResponse('<h1> One data deleted <h1>')
    return HttpResponseRedirect('http://127.0.0.1:8000/relationships/list')

#@login_required(redirect_field_name='next',login_url='login')
def list_mark(request, id):
    marks_obj = Mark.objects.filter(student_id=id).values()
    return render(request, 'list_marks.html', {'form1': marks_obj})

def add_marktable(request):
    Mark = MarkForm(request.POST or None, request.FILES or None)
    if Mark.is_valid():
        Mark = Mark.save(commit=True)
        Mark.created_by = (request.user).username
        Mark.save()
        return redirect('/')
    return render(request, 'add_marktable.html', {'form': Mark})

def update_marktable(request, id):
    mark_obj = Mark.objects.get(id=id)
    form = MarkForm(request.POST or None,
                    request.FILES or None, instance=mark_obj)

    if form.is_valid():
        form = form.save(commit=True)
        form.modified_by = (request.user).username
        form.save()
        return redirect('/')
    return render(request, 'update_marktable.html', {'form': form})


def delete_marktable(request, id):
    mark_obj = Mark.objects.get(id=id)
    mark_obj.delete()
    return HttpResponse('<h1> One data deleted <h1>')

def send_json(request, id):
	results = Mark.objects.filter(id=id).values()
	json_res = []
	for result in results:
		json_res.append(result)
	output = json.dumps(json_res, sort_keys=True, indent=4, default=str)
	return HttpResponse(output, content_type="application/json")
'''
def add_marks(request):
	Marks = request.POST.get('marks')
	student_id = request.POST.get('student')
	student = Student.objects.get(id=student_id)
	Mark.objects.create(
		Marks=Marks,
		student=student
	)
	return render(request,'add-marks.html',{ 'students': Student.objects.all(),'msg':'Marks added!'})

def add_students(request):

	Name = request.POST.get('name')
	Roll_no = request.POST.get('roll_no')
	Address = request.POST.get('address')
	Student.objects.create( 
		Name=Name,
		Roll_no=Roll_no,
		Address=Address
	)
	return render(request,'add-students.html',{'msg':'Students added!'})

def add_persons(request):

	Name = request.POST.get('name')
	Email = request.POST.get('Email')
	Mobile = request.POST.get('Mobile')
	Person.objects.create( 
		Name=Name,
		Email=Email,
		Mobile=Mobile
	)
	return render(request,'add-persons.html',{'msg':'Persons added!'})

def add_aadhars(request):
	Aadhar_no = request.POST.get('Aadhar_no')
	person_id = request.POST.get('person')
	person = Person.objects.filter(id=person_id).values()
	Aadhar.objects.create(
		Aadhar_no=Aadhar_no,
		person=person
	)
	return render(request,'add-aadhars.html',{ 'persons':Person.objects.all(),'msg':'Aadhars added!'})
'''
