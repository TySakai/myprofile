from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'personal/home.html')

def solpod_about(request):
    return render(request, 'personal/solpod_about.html')

def solpod_desc(request):
    return render(request, 'personal/solpod_desc.html')

def solpod_result(request):
    return render(request, 'personal/solpod_result.html')

def lct_about(request):
    return render(request, 'personal/lct_about.html')

def lct_pid(request):
    return render(request, 'personal/lct_pid.html')

def lct_result(request):
    return render(request, 'personal/lct_result.html')
