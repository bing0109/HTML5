from django.shortcuts import render
from django.http import HttpResponse
from .models import User, MDpw
import time


# Create your views here.
def login(request):
	return render(request, 'yaofang/login.html')


def login_handler(request):
	input_user = request.POST.get('us')
	input_pswd = request.POST.get('pw')
	# db_user = User.objects.values('username')
	# db_users = [i['username'] for i in db_user]
	db_user = User.objects.filter(username=input_user).values('username')
	db_users = [i['username'] for i in db_user]
	# print(input_user, input_pswd, db_users)

	if len(db_users) == 0:
		return HttpResponse('用户名不存在，请重新输入！')
	else:
		db_pw = User.objects.get(username=input_user).password
		mdpw = MDpw(input_pswd, input_user)
		mdpw_input = mdpw.md_pw2()
		print(db_pw, '------------23234234--------')
		if db_pw == mdpw_input:
			# return HttpResponse('登录成功！')
			return render(request, 'yaofang/login_succ.html')
		else:
			return HttpResponse('用户名密码不匹配，请重新输入！')

def mainpage(request):
	return render(request, 'yaofang/main.html')


def register(request):
	return render(request, 'yaofang/register.html')


def register_handler(request):
	input_user = request.POST.get('us')
	input_pswd = request.POST.get('pw')
	input_pw_con = request.POST.get('pw_confirm')

	if input_user == '' or input_pswd == '':
		return HttpResponse('用户名或密码不能为空')
	else:
		'''
		用get获取数据看到数据，try方法检查
		try:
			db_user = User.objects.get(username=input_user)
			return HttpResponse('用户名已存在，请重新输入！')
		except Exception:
			密码处理的代码
			return HttpResponse('注册成功！')
			'''
		# db_user = User.objects.values('username')		这个方法获取到了没有过滤的全部的数据，可能会很占内存，最好别直接用
		# db_users = [i['username'] for i in db_user]
		db_user = User.objects.filter(username=input_user).values('username')
		db_users = [i['username'] for i in db_user]
		print(db_user, '--------3232323获取username--------')

		user = User()
		print(db_users, user, '------------4545454545---------------')
		if input_user in db_users:
			return HttpResponse('用户名已存在，请重新输入！')

		else:
			if input_pswd != input_pw_con:
				return HttpResponse('两次输入的密码不一致，请重新输入！')

			else:
				user.username = input_user
				md5pw = MDpw(input_pswd, input_user)
				user.password = md5pw.md_pw2()
				print(user.password, '------234234234-------')
				user.save()
				# return HttpResponse('<h1>注册成功</h1>')
				return render(request, 'yaofang/regist_succ.html')


def after_register(request):
	return render(request, 'login.html')
