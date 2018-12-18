from django.shortcuts import render
from django.http import HttpResponse
from .models import Translate


# Create your views here.
def translateaction(request):
    return render(request, 'translate.html')


def translate_handle(request):
    input_cn = request.GET.get("cn").strip(' ')
    input_en = request.GET.get("en").strip(' ')
    language = request.GET.get('language')
    translates = request.GET.get('translate')
    if translates == 'start_translate':
        if language == 'cntoen':
            # print(Translate.objects.get(id='0'), '-----------------？？？？？？？？？？？？？？？？？？？？？？？？-')
            print(Translate.objects.values('en'), '------------------')

            try:
                db_en = [i['en'] for i in Translate.objects.values('en','cn') if i['cn']==input_cn]
                db_ens = ','.join(db_en)
                return HttpResponse((input_cn + '的英文翻译是：', db_ens), charset='utf8')
            except Exception:
                return HttpResponse('对不起，查到不到 “%s” 对应的英文翻译。' % input_cn)

        elif language == 'entocn':
            try:
                db_cn = [i['cn'] for i in Translate.objects.values('cn','en') if i['en']==input_en]
                db_cns = ','.join(db_cn)
                print(db_cn)
                return HttpResponse(('translate "%s" to chinese is: %s' % (input_en, db_cns)), charset='utf8')
            except Exception:
                return HttpResponse('sorry,there is no chinese translation of "%s" in db.' % input_en)
        else:
            return HttpResponse('出问题了，请重新进入页面。<br>something error.')

    elif translates == 'submit_translate':
        translate_item = Translate()
        translate_item.cn = input_cn
        translate_item.en = input_en
        print(translate_item,translate_item.id,translate_item.en,translate_item.cn,'----------')
        translate_item.save()
        return HttpResponse('%s：%s<br>添加原文、译文成功。<br>add original&translation success.' % (input_cn, input_en))
        # return HttpResponse('添加翻译成功')
    else:
        return HttpResponse('出问题了，请重新进入页面。<br>something error.')
