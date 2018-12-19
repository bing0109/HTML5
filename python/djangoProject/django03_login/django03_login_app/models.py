from django.db import models
from hashlib import md5

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=256)



class MDpw():
	def __init__(self, pw, usr):
		self.pw = pw
		self.us = usr

	def md_pw(self):
		'''
			滴pw进行md5算法处理，切片后分别翻转，再拼接
		:return:
		'''
		md = md5()
		md.update(self.pw.encode('utf8'))
		md_pw1 = md.hexdigest()
		md_pw1_1 = md_pw1[:16][::-1]
		md_pw1_2 = md_pw1[16:][::-1]

		md_pw_last = md_pw1_1 + md_pw1_2
		print(md_pw1, md_pw_last, '----123123123------')
		return md_pw_last

	def md_pw2(self):
		'''
			通过用户名和密码，分别算md5，再逐个字符相加的方法进行加密
		:return:
		'''
		md = md5()
		md.update(self.pw.encode('utf8'))
		md_pw1 = md.hexdigest()

		us = md5()
		us.update(self.us.encode('utf8'))
		md_us1 = us.hexdigest()

		md_pw_last = ''
		n = 0
		for i in md_pw1:
			md_pw_last = md_pw_last + (i+md_us1[n])
			n += 1

		print(md_pw1, md_us1, md_pw_last, '----321321321------')
		return md_pw_last



'''
202cb962ac59075b964b07152d234b70
7b432d25170b469b57095ca269bc202
5f4dcc3b5aa765d61d8327deb882cf99
'''