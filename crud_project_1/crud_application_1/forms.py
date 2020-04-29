from django import forms
from crud_application_1.models import Student

class Student_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
