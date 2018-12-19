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
            if input_cn != '':
                # print(Translate.objects.get(id=1), '------------------')
                # print(Translate.objects.get(cn=input_cn).en, '---1111------报错的话可能是查不到数据或查到多个数据--')
                # print(Translate.objects.values('en'), '----------222222222222--------')
                # db_en = [i['en'] for i in Translate.objects.values('en', 'cn') if i['cn'] == input_cn]
                db_en = [i['en'] for i in Translate.objects.filter(cn=input_cn).values('en')]

                if db_en != []:
                    db_ens = ','.join(db_en)
                    return HttpResponse((input_cn + '的英文翻译是：', db_ens), charset='utf8')
                else:
                    return HttpResponse('对不起，查到不到 “%s” 对应的英文翻译。' % input_cn)
            else:
                return HttpResponse('请输入中文原文。')

        elif language == 'entocn':
            if input_en != '':
                try:
                    # db_cn = [i['cn'] for i in Translate.objects.values('cn', 'en') if i['en'] == input_en]
                    db_cn = [i['cn'] for i in Translate.objects.filter(en=input_en).values('cn')]
                    if db_cn != []:
                        db_cns = ','.join(db_cn)
                        print(db_cn, input_en, '------------55555-----------')
                        return HttpResponse(('translate "%s" to chinese is: %s' % (input_en, db_cns)), charset='utf8')
                    else:
                        return HttpResponse('sorry,there is no chinese translation of "%s" in db.' % input_en)
                except Exception:
                    return HttpResponse('sorry,there is no chinese translation of "%s" in db.' % input_en)
            else:
                return HttpResponse('pleas input original english text.')

        else:
            return HttpResponse('出问题了，请重新进入页面。<br>something error.')

    elif translates == 'submit_translate':
        db_items = Translate.objects.values('cn', 'en')

        print([[i['cn'], i['en']] for i in db_items], '----44444-------', [input_cn, input_en])
        db_items_list = [[i['cn'], i['en']] for i in db_items]
        if [input_cn, input_en] not in db_items_list:
            translate_item = Translate()
            translate_item.cn = input_cn
            translate_item.en = input_en
            print(translate_item, translate_item.id, translate_item.en, translate_item.cn, '---33333-------')
            translate_item.save()
            return HttpResponse('%s：%s<br>添加原文/译文成功。<br>add original/translation success.' % (input_cn, input_en))
        else:
            return HttpResponse('%s：%s<br>原文/译文已存在。<br>original/translation is already exist.' % (input_cn, input_en))

    else:
        return HttpResponse('出问题了，请重新进入页面。<br>something error.')
