from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not  None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentails please register this form")
            return redirect('register')
        return redirect('login')
    return render(request, 'login111.html')
# else:
#             messages.info(request, 'Passwords do not match')
#             return redirect('register')
#             return redirect('/')
#             return render(request,'register.html')


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
                user.save()
                return redirect("login")
                print("User created")
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')