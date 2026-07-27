from django import forms
from .models import Student, Course, Enrollment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'major']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email Address'}),
            'major': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Major'}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'description', 'credits']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Course Name'}),
            'code': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Course Code'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Course Description', 'rows': 4}),
            'credits': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Credits'}),
        }
