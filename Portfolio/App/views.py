from django.shortcuts import render

# Create your views here.
def App(request):
    if request.method=='GET':
        return render(request,'portfolio.html')