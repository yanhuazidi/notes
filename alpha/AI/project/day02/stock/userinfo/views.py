from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
import json
from .models import *

# Create your views here.


def register_(request):
    if request.method == "POST":
        new_user = UserInfo()
        new_user.username = request.POST.get("username","")
        if not new_user.username:
            return HttpResponse(json.dumps({"result":False, "data":"", "error":"用户名不能为空"}))
        olduser = UserInfo.objects.filter(username=new_user.username)
        if olduser:
            return HttpResponse(json.dumps({"result":False, "data":"", "error":"用户名已存在"}))
        if request.POST.get("pwd") != request.POST.get("cpwd"):
            return HttpResponse(json.dumps({"result": False, "data": "", "error": "两次密码不一致"}))
        new_user.password = make_password(request.POST.get("pwd"),None,'pbkdf2_sha1')
        new_user.save()
        return HttpResponse(json.dumps({"result":True, "data":"注册成功", "error":""}))

    if request.method == "GET":
        return HttpResponse(json.dumps({"result":True, "data":"", "error":""}))

from django.contrib.auth import login, authenticate, logout
def login_(request):
    if request.method == "POST":
        username = request.POST.get("username","")
        pwd = request.POST.get("pwd","")
        if not username:
            return HttpResponse(json.dumps({"result": False, "data": "", "error": "用户名不能为空"}))
        user = authenticate(username=username,password=pwd)
        if user is not None and user.is_active:
            login(request,user)
            url = request.COOKIES.get("source_url",'')
            return HttpResponse(json.dumps({"result":True,"data":{"url":url,"username":username},"error":""}))
        else:
            return HttpResponse(json.dumps({"result": False, "data": "", "error": "用户名密码错误"}))
    if request.method == "GET":
        return HttpResponse(json.dumps({"result":True,"data":"","error":""}))

def logout_(request):
    logout(request)
    return HttpResponse(json.dumps({"result": True, "data": "已登出", "error": ""}))












