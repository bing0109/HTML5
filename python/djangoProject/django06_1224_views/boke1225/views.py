# coding=utf8
from django.shortcuts import render, redirect
from .models import *
import time
import sys
from django.db.models import *
from django.core.paginator import Paginator
# Create your views here.


def bk_index(request, pgid):
    if pgid == '':
        pgid = 1

    # bks = Article.objects.all().order_by('-ar_create_time').values('id', 'ar_title', 'ar_brief', 'ar_create_time', 'author_id__us_nickname')
    bks = Article.objects.all().order_by('-ar_create_time')
    print(bks, '----4-------')              # 刷新一次，打印了多次？？？？？？？
    print(sys.getsizeof(bks), '------getsizeof bks----------')
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
    context = {'bk_object': index_page_obj, 'total_pgs': total_pages, 'pgls': page_list, 'pgtype': 'index'}
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
    # new_bk.ar_create_time = time.asctime(time.localtime())
    new_bk.author_id = bk_author
    new_bk.save()

    return redirect('/index/')


def ar_delete(request, ar_id):
    # 要给id加int，否则取不到结果
    ar_to_be_del = Article.objects.get(pk=int(ar_id))
    ar_to_be_del.delete()
    # ar_to_be_del.save()
    print(ar_id, 'del----------')
    return redirect('/index/')


def ar_modify(request, ar_id):
    #
    ar_to_be_modify = Article.objects.get(pk=int(ar_id))
    # ar_title = ar_to_be_modify.values('ar_title')
    # ar_brief = ar_to_be_modify.values('ar_brief')
    # ar_content = ar_to_be_modify.values('ar_content')
    context = {'modifytext': ar_to_be_modify}
    return render(request, 'boke/bk_edit.html', context)


def edit_bk_submit(request, ar_id):
    ar_to_be_submit = Article.objects.get(pk=int(ar_id))
    ar_to_be_submit.ar_title = request.POST.get('bktitle')
    ar_to_be_submit.ar_brief = request.POST.get('bkbrief')
    ar_to_be_submit.ar_content = request.POST.get('bkcontent')
    ar_to_be_submit.ar_update_time = time.strftime('%Y-%m-%D %H:%M:%S', time.localtime())
    ar_to_be_submit.save()
    return redirect('/index/')


def ar_search(request, pg_id):
    if pg_id == '':
        pg_id = 1

    # try:
    #     kw = request.POST.get('keyboard')
    #     print(kw, '----try----')
    #
    # except Exception:
    #     kw = request.POST.get('kw_ajax')
    #     print(kw, '------except----')

    if request.method == 'GET':
        kw = request.GET.get('keyboard')
        # if kw is None:
        #     kw = request.GET.get('kw_ajax')
        # pg_id = request.GET.get('pg_id')
        print(kw, '---kw--get---')

    if request.is_ajax():
        kw = request.GET.get('kw_ajax')
        pg_id = request.GET.get('pgid')
        if kw is None:
            kw = request.POST.get('kw_ajax')
            pg_id = request.GET.get('pgid')
            print('----ajax--post----')
        print(kw, pg_id, '---kw--ajax---')

    if request.method == 'POST':
        kw = request.POST.get('keyboard')
        print(kw, '---kw--post---')

    s_article = Article.objects.filter(Q(ar_title__contains=kw) | Q(ar_brief__contains=kw) | Q(ar_content__contains=kw)).order_by('-ar_create_time')

    for ar in s_article:
        ar.ar_title = ar.ar_title.replace(str(kw), '<span style="color:red">'+str(kw)+'</span>')
        ar.ar_brief = ar.ar_brief.replace(str(kw), '<span style="color:red">'+str(kw)+'</span>')
        ar.ar_content = ar.ar_content.replace(str(kw), '<span style="color:red">'+str(kw)+'</span>')

    pages = Paginator(s_article, 3)

    # 获取第id页的数据
    index_page_obj = pages.page(int(pg_id))
    # 获取页数的列表
    page_list = pages.page_range
    # 获取总页数
    total_pages = pages.num_pages
    # 为render创建一个传递参数的字典
    context = {'bk_object': index_page_obj, 'se_kw': kw, 'total_pgs': total_pages, 'pgls': page_list, 'pgtype': 'search'}
    # 把字典作为render的第三个参数传递给前端

    return render(request, 'boke/index.html', context)
