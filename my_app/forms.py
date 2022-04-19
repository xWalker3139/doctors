from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Prescription, Patients, X_Ray_Reports, Scan_Report

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
        }

class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'
        widgets = {
            'user':forms.TextInput(attrs={'value': '', 'id':'user1', 'type':'hidden'}),
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'year_of_birth':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Year of birth'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'state':forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}),
            'city':forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),
        }

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('drugs', 'refill', 'void_after', 'user')
        widgets = {
            'user':forms.TextInput(attrs={'value':'', 'id':'user1', 'type':'hidden'}),
            'drugs':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Drugs'}),
            'refill':forms.Select(attrs={'class':'form-control'}),
            'void_after':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Void after'}),
        }

class X_Ray_ReportsForm(forms.ModelForm):
    class Meta:
        model = X_Ray_Reports
        fields = ('type_x_ray', 'ref_doctors', 'code_ID', 'date', 'description', 'user')
        widgets = {
            'user':forms.TextInput(attrs={'value': '', 'id':'user1', 'type':'hidden'}),
            'type_x_ray':forms.Select(attrs={'class':'form-control'}),
            'ref_doctors':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ref Doctors'}),
            'code_ID':forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'ID Code'}),
            'date':forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'Date'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description...'}),
        }

class Scan_ReportForm(forms.ModelForm):
    class Meta:
        model = Scan_Report
        fields = ('type_scan', 'ref_doctors', 'report_name', 'date', 'file', 'user')
        widgets = {
            'user':forms.TextInput(attrs={'value':'', 'id':'user1', 'type':'hidden'}),
            'type_scan':forms.Select(attrs={'class':'form-control'}),
            'ref_doctors':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ref Doctors'}),
            'report_name':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Report name'}),
            'date':forms.DateInput(attrs={'class':'form-control', 'placeholder':'Date'}),
            'file':forms.FileInput(),
        }