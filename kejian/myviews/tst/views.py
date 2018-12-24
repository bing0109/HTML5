from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image,ImageDraw,ImageFont
from io import BytesIO
import random
# Create your views here.
def login(request):
    return render(request,'login.html')
def login_chuli(request):
    lover=request.POST.getlist('lover')
    print(lover)
    username=request.POST.get('username')
    #如果有session把session的内容写到页面上，如果没有，把用户名写到session中

    user=request.session.get('username','')
    if user=='':
        request.session['username']=username
        resp = HttpResponse(lover)
        resp.set_cookie('username', username)

    else:
        resp = HttpResponse(str(lover)+' '+user)
        resp.set_cookie('username', username)
    return resp
def virifycode(reqeust):
    width=300
    height=120
    bgcolor=(random.randrange(0,255),random.randrange(0,255),255)

    im=Image.new('RGB',(width,height),bgcolor)
    draw=ImageDraw.Draw(im)
    for i in range(1000):
        xy=(random.randrange(width),random.randrange(height))
        fillcolor=(255,random.randrange(255),random.randrange(255))
        draw.point(xy,fill=fillcolor)
    for i in range(10):
        xy=(random.randrange(width),random.randrange(height),random.randrange(width),random.randrange(height))
        fillcolor = (255, random.randrange(255), random.randrange(255))
        draw.line(xy,fill=fillcolor,width=1)
    strs='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    result=''
    for i in range(4):
            result+=strs[random.randrange(len(strs))]
    textfont=ImageFont.truetype(font='Phetsarath_OT.ttf',size=50)
    textcolor=(random.randrange(255),255,random.randrange(255))
    draw.text((50,5),result[0],fill=textcolor,font=textfont)
    draw.text((100,40), result[1], fill=textcolor, font=textfont)
    draw.text((140,15), result[2], fill=textcolor, font=textfont)
    draw.text((200,30), result[3], fill=textcolor, font=textfont)
    ios=BytesIO()
    im.save(ios,'png')
    return HttpResponse(ios.getvalue(),'image/png')

