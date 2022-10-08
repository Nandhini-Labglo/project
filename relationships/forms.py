from django import forms
from .models import Student, Mark


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        


class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = "__all__"
        exclude = ['created_by','modified_by']

