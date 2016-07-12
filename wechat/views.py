from __future__ import unicode_literals
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage
 
 
WECHAT_TOKEN = ''
AppID = ''
AppSecret = ''
 
# 实例化 WechatBasic
wechat_instance = WechatBasic(
    token=WECHAT_TOKEN,
    appid=AppID,
    appsecret=AppSecret
)


def wechat(request):
    if request.method == 'GET':
        # 检验合法性
        # 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
 
        if not wechat_instance.check_signature(
                signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponseBadRequest('Verify Failed')
 
        return HttpResponse(
            request.GET.get('echostr', ''), content_type="text/plain")
 
    # 解析本次请求的 XML 数据
    try:
        wechat_instance.parse_data(data=request.body)
    except ParseError:
        return HttpResponseBadRequest('Invalid XML Data')
 
    # 获取解析好的微信请求信息
    message = wechat_instance.get_message()
 
    # 关注事件以及不匹配时的默认回复
    response = wechat_instance.response_text(
        content = (
            '感谢您的关注！\n回复【功能】两个字查看支持的功能，还可以回复任意内容开始聊天'
            '\n【<a href="http://104.128.80.53:8000/">小心的博客</a>】'
            ))
    if isinstance(message, TextMessage):
        # 当前会话内容
        content = message.content.strip()
        if content == '功能':
            reply_text = (
                    '目前支持的功能：\n1. 关键词后面加上【教程】两个字可以搜索教程，'
                    '比如回复 "Django 后台教程"\n'
                    '2. 回复任意词语，查天气，陪聊天，讲故事，无所不能！\n'
                    '还有更多功能正在开发中哦 ^_^\n'
                    '【<a href="http://104.128.80.53:8000/">小心的博客</a>】'
                )
        elif content.endswith('教程'):
            reply_text = '您要找的教程如下：'
        elif content == '贰颜':
            reply_text = '她是猪 ^ _ ^'
        else:
            reply_text = (
                '自己玩泥巴去吧 ^ _ ^\n'
                '【<a href="http://6a071219.ngrok.natapp.cn/demo1/">小心的博客</a>】')
 
        response = wechat_instance.response_text(content=reply_text)
 
    return HttpResponse(response, content_type="application/xml")

def index(request):
	return render(request,"wechat/index.html")

def demo1(request):
	return render(request,"wechat/demo1.html") 

def demo2(request):
	return render(request,"wechat/demo2.html") 
