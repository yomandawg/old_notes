from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def qna(request):
    return render(request, 'qna.html')

def mypage(request):
    return render(request, 'mypage.html')

def signup(request):
    return render(request, 'signup.html')

def not_found(request, not_found):
    return render(request, 'not_found.html', {'not_found': not_found})