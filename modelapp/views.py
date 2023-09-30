from django.shortcuts import render
from .forms import userdataform

# Create your views here.

def index(request):
    form=userdataform()
    return render(request,'home1.html',{'form':form})
def submit(request):
    if request.method=='POST':
        
        # data.save()
        return render(request,'submit1.html')
