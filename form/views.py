from django.shortcuts import render
from .forms import Student
# Create your views here.
def home(request):
    form=Student(auto_id='True',label_suffix='',initial={'name':'prashanth','email':'prashanth@gamil.com'})
    return render(request,'app/home.html',{'form':form})