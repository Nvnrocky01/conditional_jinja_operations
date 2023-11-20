from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':9}
    return render(request,'conditions.html',d)

def ifelse(request):
    d={'a':9,'b':10}
    return render(request,'if else.html',d)

def elif_(request):
    d={'a':9,'b':10,'c':20}
    return render(request,'elif.html',d)

def nestedif(request):
    d={'a':10,'b':9,'c':30,'d':20}
    return render(request,'nested if.html',d)
