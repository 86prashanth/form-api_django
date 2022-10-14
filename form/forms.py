from django import forms
# form creation
class Student(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()