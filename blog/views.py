from django.shortcuts import render,HttpResponse,render_to_response
#from django.template.context_processors import csrf
from django.template import RequestContext
from .models import User,Say,Feeling
import json
import random
import math

#datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') 格式化日期

#表单提交请求
"""def login(request):
    msg = ''
    users = User.objects.all()
    if request.method == 'POST':
        user = request.POST['username']
        pd   = request.POST['password']
        for i in range(len(users)):
            msg = ''
            if user == users[i].username:
                if pd  == users[i].passwd:
                    msg += '认证成功'
                    return render_to_response("home.html")
                    break
                else:
                    msg += '密码错误！'
            else:
                msg += '用户名错误'
        return render_to_response("login.html",{"user":msg})

    else:
        return render_to_response("login.html")"""

# def login_index(request):
#     return render_to_response("login.html")


#ajax发送post请求，django以json响应
def login(request):
    print (111)
    data = dict()
    users = User.objects.all()
    if request.method == "POST":
        print (111111)
        user   = request.POST["username"]
        pd = request.POST["password"]
        for i in range(len(users)):
            msg = ""
            if user == users[i].username:
                if pd == users[i].passwd:
                    data["url"] = "http://127.0.0.1:8000/"
                    return HttpResponse(json.dumps(data),content_type="application/json")
                else:
                    msg += "密码错误"
                    data["msg"] = msg
                    break
            else:
                msg += "用户名错误"
                data["msg"] = msg
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return render_to_response("login.html")

 #用户注册post请求

def register(request):
    print(111)
    data = dict()
    users = User.objects.all()
    if  request.method == "POST":
        user   = request.POST["username"]
        pd = request.POST["password"]
        Email  = request.POST["email"]
        for i in range(len(users)):
            msg = ""
            if user == users[i].username:
                msg += "该用户名已存在或长度小于5位"
                data["msg"] = msg
                return HttpResponse(json.dumps(data), content_type="application/json")
                break
        userinfor = User(username=user,passwd=pd,email=Email)
        userinfor.save()
        data["url"] = "http://127.0.0.1:8000/"
        return HttpResponse(json.dumps(data),content_type="application/json")
#每日一说ajax post请求
def say(request):
    once_say = Say.objects.all()
    index = random.randint(0,len(once_say))
    send_data = once_say[index].saying
    return HttpResponse(send_data)

#主页html
def home(request):
    feels = Feeling.objects.order_by("-id")
    feel_length = len(Feeling.objects.all())
    feel_list = []
    page_len =  str(math.ceil(feel_length/5))
    for i in range(5):
        feel_list.append(feels[i])
    return render_to_response("home.html",{"feel_list":feel_list})

#说说ajax post请求
def talk(request):
    feel = Feeling.objects.order_by("-id")
    feel_length = len(Feeling.objects.all())
    page_len =  math.ceil(feel_length/5)
    current_page = int(request.POST["current_page"])
    reste = feel_length%5
    send_dict = {}        #post数据类型 字典
    talks = []           #说说内容列表
    counts = []         #说说点赞次数列表
    range_length = 5
    length = 5
    if request.POST["data"] == "next":
        if current_page == page_len-1 and reste != 0:
            range_length = reste
            length = current_page*5
        else:
            length =  (current_page)*5 
    elif request.POST["data"] =="previous":
        range_length = 5
        length = (current_page-2)*5
    for i in range(range_length):
        talks.append((feel[i+length]).feeling)
        counts.append((feel[i+length]).like_times)
    send_dict["talks"] = talks
    send_dict["counts"] = counts
    send_dict["page_len"] = page_len
    return HttpResponse(json.dumps(send_dict), content_type="application/json")


#点赞 ajax post请求，之后优化 可以做异常处理
def like_count(request):
	rev_times = request.POST["count"]
	rev_content = request.POST["content"].strip()
	database_data = Feeling.objects.get(feeling=rev_content)
	send_data = str(int(rev_times)+1)
	database_data.like_times = send_data
	database_data.save()
	return HttpResponse(send_data)

def shuoshuo(request):
	feels = Feeling.objects.order_by("-createTime")
	feels_list = list()
	for i in range(len(feels)):
		feels_list.append(feels[i])
	return render_to_response("shuoshuo.html",{"feels_list":feels_list},context_instance=RequestContext(request))	










