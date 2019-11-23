from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from  QSHOP.common import set_password
from .models import Manager
import json
from django.http import JsonResponse


# Create your views here.
def base(request):
    return render(request,'manage_base.html')

def index(request):
    manager_name = request.session.get("manager_name")
    # id = request.session["id"]
    manager=request.COOKIES.get("manager")
    print(manager_name,manager,id)
    if manager_name and manager:
        return render(request,'common/index.html')
    else:
        return HttpResponseRedirect('/manager/login')


def register(request):
    error = ""
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        repeat_password = data.get('repeat_password')
        print(name,email,password,repeat_password)
        if password != repeat_password:
            error = "两次密码不一致"
            return render(request, 'common/register.html', {'error': error})
        md5_pwd = set_password(set_password(password))
        m=Manager.objects.filter(manager_name=name)
        if not m.exists():
            m=Manager.objects.create(manager_name=name,email=email,password=md5_pwd)
            print(m,type(m))
            return HttpResponseRedirect('/manager/login')
        error = "用户名重复"
    return render(request,'common/register.html',{'error':error})

def check_username(request):
    result = {"flag":0}
    data = request.GET
    username = data.get("username")
    print(username)
    if username != "":
        m = Manager.objects.filter(manager_name=username)
        if not m.exists():
            result["flag"] = 1
        # message= "用户名重复"
    return HttpResponse(json.dumps(result))

def login(request):
    error=""
    if request.method=="POST":
        data = request.POST
        manager_name = data.get("username")
        password = data.get("password")
        # print(manager_name,password)
        md5_pwd = set_password(set_password(password))
        # print(md5_pwd)
        try:
            m = Manager.objects.get(manager_name=manager_name,password=md5_pwd)
            #设置session
            request.session['manager_name'] = manager_name
            request.session['id'] = m.id
            #设置cookie
            response = HttpResponseRedirect('/manager/index')
            response.set_cookie("manager",manager_name)
            return response
        except:
            error = "用户名密码有误"

    return render(request,'common/login.html',{'error':error})

def logout(request):
    request.session.clear()
    response = HttpResponseRedirect('/manager/login')
    response.delete_cookie('manager')
    return response