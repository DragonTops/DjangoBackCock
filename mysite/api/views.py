import MySQLdb
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import  get_token
from django.contrib.auth import authenticate, login
from django.db.utils import  IntegrityError
# Create your views here.

#class
#@csrf_exempt
def createUser(request):
    if "csrfmiddlewaretoken" in request.POST.keys():
        try:
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            login(request, user)
        except IntegrityError as error:
            print(error.args[0]==1062)
            if error.args[0]==1062:
                return HttpResponse('{ response: UserExists, error: ' + str(error.args) + " }")
            else:
                return HttpResponse('{ response: UknownError}')
        return HttpResponse('{success}')
    else:
    #try:
    #    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    #except MySQLdb.IntegrityError as error:
    #    print(error.args)
    #    return HttpResponse('{ response: 404, ' + str(HttpResponse(get_token(request))) + "}")
    ##if request.POST['username'] in User.username_validator
        return HttpResponse(str(get_token(request)))

def loginUser(request):
    request.session.modified = True
    if "csrfmiddlewaretoken" in request.POST.keys():
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if (user is not None):
            login(request, user)
            return HttpResponse("Login success : " + request.user.username)
        else:
            return HttpResponse("User not found")
    else:
        return HttpResponse(str(get_token(request)))

def getData(request):
    if "csrfmiddlewaretoken" in request.POST.keys():
        user = request.user
        if (user.is_authenticated):
            return HttpResponse(user.email + "|" + user.username)
        else:
            return HttpResponse("User not auth")
    else:
        return HttpResponse(str(get_token(request)))