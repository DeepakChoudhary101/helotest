from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'home.html')
username='hello'
password='7000'
def submit(request):
    if request.method=='POST':
        x=request.POST['username']
        y=request.POST['password']
        if x==username and y==password:


            return render(request ,'submit.html')
        else:
            return render(request,'home.html')



    
# Create your views here