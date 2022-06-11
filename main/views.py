#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def stating(request):
    return render(request,'start.html',{'name':'USER'});
def add(request):
    val1= int(request.POST["number1"])
    val2= int(request.POST["number2"])
    res=val1+val2

    return render(request,"result.html", {"result":res})
