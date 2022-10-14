from django.shortcuts import render
from .forms import Registration
# Create your views here.
def hey(request):
    content=Registration()
    content.order_fields(field_order=['name','email'])
    return render(request,'app/about.html',{'content':content})