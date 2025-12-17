from django import forms
from .models import Student

class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'registration_number', 'phone_number']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Weka jina lako kamili'}),
            'registration_number': forms.TextInput(attrs={'placeholder': '24/AAA/000'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+255xxxxxxxxxx'}),
        }

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['phone_number']