from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from parserapp.models import Skills_table, Params
from .models import Vacancy
from .forms import SearchForm

from .parser import  hh_serch

# Create your views here.
def main_view(request):
    return render(request, 'parserapp/index.html')


def form_post(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            # Получить данные из форы
            name_search = form.cleaned_data['name']
            where_search = form.cleaned_data['where']
            print('kojimi',name_search,where_search)
            hh_serch(name_search, where_search)

            param = Params.objects.all()
            results = []

            for post in Vacancy.objects.all():
                k = post.skils.all()

                z = []
                for y in k:
                    z.append(y)
                guv = [post] + [z]
                results.append(guv)

            return render(request, 'parserapp/results.html', context={'posts': results, 'param': param})
        else:
            print('bohb ouh uj')
            return render(request, 'parserapp/form.html', context={'form': form})
    else:
        form = SearchForm()
        return render(request, 'parserapp/form.html', context={'form': form})


def result(request):
    param = Params.objects.all()
    results=[]

    for post in Vacancy.objects.all():
        k=post.skils.all()

        z=[]
        for y in k:
            z.append(y)
        guv = [post] + [z]
        results.append(guv)

    return render(request, 'parserapp/results.html', context={'posts': results,'param':param})
