from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request, 'register.html')
if password == passwords:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.save();
            print("user created")
        else:
            print("pass not matching")
        return redirect("/")