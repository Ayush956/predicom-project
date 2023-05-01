from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        password = request.POST.get("password")
        person = authenticate(request,username=uname,password=password)
        if person is not None:
            request.session['uname'] = uname
            return redirect("/home/")
        else:
            return HttpResponse("Something went Wrong")
    return render(request,"login.html")

def f(request):
    ok = request.session.get("uname")
    return ok

def logout(request):
    del request.session["uname"]
    return redirect("/home/")

def signup(request):
    if request.method=='POST':
        uname = request.POST.get("uname")
        email = request.POST.get("email")
        password = request.POST.get("pass")
        conpass = request.POST.get("conpass")
        if password!=conpass:
            return HttpResponse("Something went wrong")
        else:
            my_user = User.objects.create_user(uname,password,conpass)
            my_user.save()
            return redirect("/home/")
    return render(request,"signup.html")
    # return render(request,"signup.html")
