from django.shortcuts import render
from basic.models import Country
from django.views.generic import View
# Create your views here.

class base(View):
    def get(self, request, *args, **kwargs):
        records=Country.objects.order_by('country')
        return render(request,'basic/index.html',{'records':records})

    def post(self, request, *args, **kwargs):
        inp=request.POST.get('countr')
        if inp.isnumeric():
            records = Country.objects.filter(countrycode=int(inp)).order_by('country')
        else:
            records = Country.objects.filter(country=inp.capitalize()).order_by('country')
        return render(request, 'basic/index.html', {'records': records})

