from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
import random
from io import BytesIO

# Create your views here.


def form1(request):
    return render(request, 'form1224.html')


def form1_handle(request):
    habits1 = request.POST.get('habit')
    habits = request.POST.getlist('habit')
    print(habits1, '-------habits1------')  # get只能获取一个元素
    print(habits, '--------habits-----')    # getlist获取到的是一个列表

    # 如果由session，把session的内容写在页面上，如果没有，把用户名写道session中
    username = request.POST.get('usr')
    user = request.session.get('usr', '')
    if user == '':
        request.session['usr'] = username
        resp = HttpResponse(', '.join(habits))
        resp.set_cookie('usr', username)
    else:
        resp = HttpResponse(', '.join(habits), user)
        resp.set_cookie('usr', username)

    verify_input = request.POST.get('verifytext').upper()
    verify_session = request.session.get('verify_text').upper()
    print(verify_input, '123123', verify_session)
    if verify_input == verify_session:
        ver = '验证码正确'
    else:
        ver = '验证码错误'
    print(ver)
    return resp


def get_random_color():
    random_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    return random_color


def verifycode(request):
    width = 170
    height = 60
    # bgcolor = get_random_color()
    bgcolor = (219, 219, 219)

    # 生成一个图片对象
    img = Image.new('RGB', (width, height), bgcolor)

    #生成一个图片画笔对象
    draw = ImageDraw.Draw(img)

    # 写入随机文字
    strs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    results = ''
    for i in range(4):
        results += strs[random.randrange(len(strs))]

    # 随机生成100个干扰点/噪点，放的位置在生成文字后，点就在文字上层，放在钱就在文字下层
    for i in range(100):
        x, y = random.randrange(width), random.randrange(height)
        fillcolor = get_random_color()
        draw.point((x, y), fill=fillcolor)

    def verify_text_font():
        # ubuntu系统中字体的位置 /usr/share/fonts/truetype/freefont/
        fontlist = ['Phetsarath_OT.ttf', 'FreeMono.ttf', 'FreeMonoBoldOblique.ttf', 'FreeSerifItalic.ttf']
        # fontlist = ['Phetsarath_OT.ttf','Phetsarath_OT.ttf','Phetsarath_OT.ttf','Phetsarath_OT.ttf']
        fontsize = random.randint(30, 35)
        fonttype = fontlist[random.randrange(len(fontlist))]
        return ImageFont.truetype(font=fonttype, size=fontsize)

    draw.text((random.randrange(0, 30), random.randrange(0, 20)), results[0], fill=get_random_color(), font=verify_text_font())
    draw.text((random.randrange(40, 70), random.randrange(0, 20)), results[1], fill=get_random_color(), font=verify_text_font())
    draw.text((random.randrange(80, 110), random.randrange(0, 20)), results[2], fill=get_random_color(), font=verify_text_font())
    draw.text((random.randrange(120, 140), random.randrange(0, 20)), results[3], fill=get_random_color(), font=verify_text_font())

    # 验证码的值保存到session中
    request.session['verify_text'] = ''.join(results)

    # 随机生成5条干扰线，放的位置在生成文字后，线条就在文字上层，放在钱就在文字下层
    for i in range(5):
        xyxy = (random.randrange(width), random.randrange(height), random.randrange(width), random.randrange(height))
        fillcolor = get_random_color()
        draw.line(xyxy, fill=fillcolor, width=1)

    # 不需要在硬盘上保存文件，直接在内存中加载就可以
    ios = BytesIO()
    # 将生成的图片数据保存在io对象中
    img.save(ios, 'png')

    return HttpResponse(ios.getvalue(), 'image/png')

