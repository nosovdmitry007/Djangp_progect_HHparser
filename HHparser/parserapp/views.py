from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from parserapp.models import Params
from .models import Vacancy,Skills_table
from .forms import SearchForm, ComentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .parser import  hh_serch
from django.views.generic.base import ContextMixin

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
            del_bd = form.cleaned_data['delit']
            hh_serch(name_search, where_search, del_bd)

            param = Params.objects.all()
            vac = Vacancy.objects.all()

            return render(request, 'parserapp/results.html', context={'param': param, 'vac': vac})
        else:
            # print('bohb ouh uj')
            return render(request, 'parserapp/form.html', context={'form': form})
    else:
        form = SearchForm()
        return render(request, 'parserapp/form.html', context={'form': form})


def result(request):
    param = Params.objects.all()
    vac = Vacancy.objects.all()

    return render(request, 'parserapp/results.html', context={'param':param,'vac':vac})

def vacancy(request,id):
    vac = Vacancy.objects.filter(pk=id)
    results=[]

    for post in vac:
        k=post.skils.all()

        z=[]
        for y in k:
            z.append(y)
        guv = [post] + [z]
        results.append(guv)
    return render(request, 'parserapp/vacancy.html', context={'post': results})


def coment(request,id):
    vac = Vacancy.objects.filter(pk=id)
    if request.method == 'GET':
        form = ComentForm()
        return render(request, 'parserapp/coment.html', context={'form': form})
    else:
        form = ComentForm(request.POST, files=request.FILES)
        if form.is_valid():
            com=form.cleaned_data['comment']
            Vacancy.objects.filter(pk=id).update(comment=com)
            vac = Vacancy.objects.filter(pk=id)
            results = []

            for post in vac:
                k = post.skils.all()

                z = []
                for y in k:
                    z.append(y)
                guv = [post] + [z]
                results.append(guv)
            return render(request, 'parserapp/vacancy.html', context={'post': results})
        else:
            form = ComentForm()
            return render(request, 'parserapp/coment.html', context={'form': form})

def SkilViews(request):
    skills = []
    skils = Skills_table.objects.all()
    results = []
    for s in skils:
        if s.skil not in skills:
            skills.append(s.skil)
            col = Skills_table.objects.filter(skil=s.skil).count()
            res = [s.id]+[s.skil] + [col]
            results.append(res)

    def sort_by_col(emp):
        return emp[2]

    results.sort(key=sort_by_col,reverse=True)
    return render(request, 'parserapp/skills_table_list.html', context={'skils': results})



def Skilvacancy(request, id):
    vac = Vacancy.objects.all()
    sk = Skills_table.objects.filter(id=id)
    results=[]
    skil = 0
    for post in vac:
        k = post.skils.all()
        z=[]
        for y in k:
            z.append(y)
            if sk[0].skil == y.skil:
                skil+=1
        if skil>0:
            guv = [post] + [z]
            results.append(guv)
            skil = 0

    return render(request, 'parserapp/skil_vacanc.html', context={'post': results})
