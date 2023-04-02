from django.shortcuts import render, HttpResponse

def home(request):
    name = ['Alex','Smith','Steve','stephen']
    context = {
        'name': name
    }
    return render(request,'home.html',context)