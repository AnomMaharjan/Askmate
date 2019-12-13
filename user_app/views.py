from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserModel

# Create your views here.


def LoginAuth(request):
    if request.method == "POST":
        e = request.POST.get('email')
        p = request.POST.get('pass')
        user = UserModel.objects.filter(email=e, password=p)
        if(user.count() > 0):
            for user in user:
                request.session['email'] = user.email
                request.session['id'] = user.id
                request.session['name'] = user.name
                return redirect('qna:read')

        else:
            return HttpResponse("Wrong Credentials")

    else:
        return render(request, "login.htm")


def logout(request):
    request.session.flush()
    return redirect('user:login')
