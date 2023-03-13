from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Home/Home.html')

def login(request):
    return render(request, 'Home/Login.html')

def signup(request):
    return render(request, 'Home/Signup.html')

def analysis(request):
    return render(request, 'Home/Analysis.html')

# def livescore(request):
#     return render(request, 'Home/Livescore.html')

# def profile(request):
#     return render(request, 'Home/Profile.html')



