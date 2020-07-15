from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    return render(request,'index.html')

def log_in(request):
    return render(request,'log_in.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['username']
        email = request.POST['email']
        password=request.POST['password']

        if User.objects.filter(username = firstname).exists():
            print('user name taken  ')
            return redirect('/')
        else:    
            user = User.objects.create_user(username = firstname, email= email, password =password)
            user.save()
            return redirect('log_in')
    else:
        return render(request,'registration.html')