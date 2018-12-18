from django.shortcuts import render
from django.http import HttpResponse
from .models import User


# Create your views here.
def login(request):
	return render(request, 'login.html')


def login_handle(request):
	input_user = request.POST.get('us')
	input_pswd = request.POST.get('pw')
	db_user = User.objects.values('username')
	db_users = [i['username'] for i in db_user]
	print(input_user, input_pswd, db_users)
	if input_user not in db_users:
		return HttpResponse('用户名不存在，请重新输入！')
	else:
		db_pw = User.objects.get(username=input_user).password
		print(db_pw, '--------------------')
		if db_pw == input_pswd:
			return HttpResponse('登录成功！')
		else:
			return HttpResponse('用户名密码不匹配，请重新输入！')


def register(request):
	return render(request, 'register.html')


def register_handle(request):
	input_user = request.POST.get('us')
	input_pswd = request.POST.get('pw')
	input_pw_con = request.POST.get('pw_confirm')
	db_user = User.objects.values('username')
	db_users = [i['username'] for i in db_user]

	user = User()
	print(db_users, user, '---------------------------------------')
	if input_user in db_users:
		return HttpResponse('用户名已存在，请重新输入！')

	else:
		if input_pswd != input_pw_con:
			return HttpResponse('两次输入的密码不一致，请重新输入！')

		else:
			user.username = input_user
			user.password = input_pswd
			user.save()
			return HttpResponse('注册成功')

