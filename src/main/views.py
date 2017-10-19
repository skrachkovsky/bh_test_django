from django.db.models import Q, Count
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views import View
from main.models import Table1


class Index(View):
    def get(self, request):
        # if request.method == 'GET':
        #     pass
        # elif request.method == 'POST':
        #     pass
        # print(request.GET.get('param1'))
        # print(request.GET.getlist('param1'))
        # print(request.method)
        # print(request.user)
        # print(request.session)
        res = Table1.objects.all()
        # res = res.filter(name__startswith='test', value__range=(1, 100))\
        #     .exclude(value=3)
        res = res.filter(
            (Q(name__startswith='test') | Q(value__range=(1, 100)))
            & ~Q(value=3)
        )
        res = res.order_by('-id')\
            .distinct()
        # res = res.filter(tables2__pk__isnull=False)

        res = res.annotate(tables2_count=Count('tables2'))

        print(list(res))
        return TemplateResponse(request, 'main/index.html', {
            'varname': '1212',
            'res': res
        })


def page(request, number):
    return TemplateResponse(request, 'main/page.html')


def pages(request, year=None, month=None, day=None):
    return HttpResponse('pages %s' % '-'.join([str(year), str(month), str(day)]))
