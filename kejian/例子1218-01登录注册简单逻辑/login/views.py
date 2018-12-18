from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def login(request):
	return render(request,'login.html')
def login_handler(request):
	#第一步：从前端获取表单的提交的元素内容 
	username=request.POST.get('username')
	password=request.POST.get('password')
	#第二步:从数据库取记录，django操作User类
	#user=User()相当于把user实例化
	#User.objects指的是User类里所有的记录
	#user=User.objects.get(pk=1)等号右边的User大写
	try:
		user=User.objects.get(username=username)
		print(user.username)
		print(user.password)
		print(password)
		print(username)
	#第三步:判断一下当前记录的username与前端获取的内容是否相同，password也一样
		if user.username==username and  user.password==password:
	
			return HttpResponse('登录成功')
		else:
			return HttpResponse('登录失败')
	except Exception:
		return HttpResponse('登录失败')
def register(request):
	return render(request,'register.html')
def register_handler(request):
	#第一步：从前端获取表单提交的元素内容 
	username=request.POST.get('username')
	password=request.POST.get('password')
	#存数据库,操作类
	#数据库产生新数据，对应django应该产生一个新对象 
	user=User()
	#user.username=username意义不同，前面的username表示是user对象里面的属性，后面username是前面获取前端的变量名
	user.username=username
	user.password=password
	#调用user的save()相当于调用了insert into user values(XXX,XXXXX)
	user.save()
	#views.py里的方法必须返回HttpResponse对象，或者返回render,返回render必须有网页
	return HttpResponse('注册成功')
