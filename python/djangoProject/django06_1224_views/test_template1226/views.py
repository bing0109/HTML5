from django.shortcuts import render


# Create your views here.
def login(request):
    pg_title = '登录'
    context = {'pg_title': pg_title}
    return render(request, 'muban1226/login.html', context)


def register(request):
    pg_title = '注册'
    context = {'pg_title': pg_title}
    return render(request, 'muban1226/register.html', context)


def user_center_info(request):
    pg_title = '用户中心'
    nav_title = 'info'
    context = {'pg_title': pg_title, 'nav_title': nav_title}
    return render(request, 'muban1226/user_center_info.html', context)


def user_center_order(request):
    pg_title = '用户中心'
    nav_title = 'order'
    context = {'pg_title': pg_title, 'nav_title': nav_title}
    return render(request, 'muban1226/user_center_order.html', context)


def user_center_site(request):
    pg_title = '用户中心'
    nav_title = 'site'
    context = {'pg_title': pg_title, 'nav_title': nav_title}
    return render(request, 'muban1226/user_center_site.html', context)



