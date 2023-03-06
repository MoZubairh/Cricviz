from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Home/Home.html')

def login(request):
    return render(request, 'Home/Login.html')

def signup(request):
    return render(request, 'Home/Signup.html')