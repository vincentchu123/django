# -*- coding: utf-8 -*-
from blog.models import Blog
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth #用户验证
# Create your views here.
def index(request):

    blog_list = Blog.objects.all()
    return render_to_response('index.html',{'blogs':blog_list})
#登陆处理
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    users_ = [username]
   # 判断用户名和密码不为空
    #if username != '' and password != '':
    # return HttpResponse('login success!')
    #response = HttpResponseRedirect('/login_ok/')
    #response.set_cookie('username',username,3600) #用户名cookie 
    #response.set_cookie('username',username,3600) #用户名cookie 
        #request.session['username']=username
        #return response  
    user = auth.authenticate(username=username, password=password)
    if user is not None:
    	auth.login(request, user) # 验证登录
        response = HttpResponseRedirect('/login_ok/')
        request.session['username'] = users_
        return response                             
    else:
        return render_to_response('index.html',{'error':'username or password error!','blogs':blog_list})
  # 登录成功
def login_ok(request):
    blog_list = Blog.objects.all()
    #username=request.COOKIES.get('username','') #读取浏览器cookie
    username=request.session.get('username','') #读取用户session
    return render_to_response('login_ok.html',{'user': username, 'blog_list':blog_list})
def logout(request):
    response=HttpResponseRedirect('/index/')
    #response.delete_cookie('username')
    del request.session['username']         # 清理用户 session
    return response