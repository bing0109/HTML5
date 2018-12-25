# coding=utf8
from django.shortcuts import render, redirect
from .models import *
import time
from django.core.paginator import Paginator
# Create your views here.


def bk_index(request, pgid):
    if pgid == '':
        pgid = 1

    bks = Article.objects.all().values('id', 'ar_title', 'ar_brief', 'ar_create_time', 'author_id__us_nickname')
    print(bks, '----4-------')              # 刷新一次，打印了多次？？？？？？？
    # 把获取到的数据放在Paginator组件中分页
    pages = Paginator(bks, 2)
    print('---------3333------------')       # 刷新一次，打印了多次？？？？？？？
    # 获取第id页的数据
    index_page_obj = pages.page(int(pgid))
    # 获取页数的列表
    page_list = pages.page_range
    # 获取总页数
    total_pages = pages.num_pages
    # 为render创建一个传递参数的字典
    context = {'bk_object': index_page_obj, 'total_pgs': total_pages, 'pgls': page_list}
    # 把字典作为render的第三个参数传递给前端
    return render(request, 'boke/index.html', context)


def new_boke(request):
    return render(request, 'boke/new_boke.html')


def new_bk_submit(request):
    bk_title = request.POST.get('bktitle')
    bk_brief = request.POST.get('bkbrief')
    bk_content = request.POST.get('bkcontent')
    bk_author = UserInfo.objects.get(pk=1)
    new_bk = Article()
    new_bk.ar_title = bk_title
    new_bk.ar_brief = bk_brief
    new_bk.ar_content = bk_content
    new_bk.ar_create_time = time.asctime(time.localtime())
    new_bk.author_id = bk_author
    new_bk.save()

    return redirect('/index/')


def ar_delete(request, ar_id):
    ar_to_be_del = Article.objects.get(pk=ar_id)
    ar_to_be_del.delete()
    ar_to_be_del.save()

    return redirect('/index/')


def ar_modify(request, ar_id):

    return redirect('/index/')
