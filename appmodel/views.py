from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect("/")

def register(request):

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        passwords = request.POST["password2"]
        if password == passwords:
            if User.objects.filter(username=username).exists():
                print("user already registered")
            elif User.objects.filter(email=email).exists():
                print("email alredy registered")
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save();
                print("user created")
        else:
            print("password not matching")
        return redirect("/")
    else:
        return render(request, 'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            print("invalid")
            return redirect("login")

    else:
        return render(request, 'login.html')