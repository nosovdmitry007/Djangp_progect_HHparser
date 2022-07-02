from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from operator import itemgetter
from django.urls import reverse_lazy
from .models import Vacancy, Skills_table
from .forms import SearchForm
from django.views.generic import ListView, DetailView,  UpdateView, TemplateView
from .parser import hh_serch
from django.views.generic.edit import FormView


#главная страница
class AboutView(TemplateView):
    template_name = "parserapp/index.html"

#список всех вакансий

class VacancListView(LoginRequiredMixin,ListView):
    model = Vacancy
    template_name = "parserapp/results.html"
    context_object_name = 'vac'
    paginate_by = 20

    def get_queryset(self):

        vac = Vacancy.objects.filter(user=self.request.user,vis=True)

        return vac

#Форма поиска

class SearchFormView(LoginRequiredMixin,FormView):
    template_name = 'parserapp/form.html'
    form_class = SearchForm
    success_url = reverse_lazy('parserapp:results')

    def form_valid(self, form):
        user_serch = self.request.user
        name_search = form.cleaned_data['name']
        where_search = form.cleaned_data['where']
        del_bd = form.cleaned_data['delit']
        rec=form.cleaned_data['res']
        hh_serch(name_search, where_search, del_bd,user_serch,rec)

        return super().form_valid(form)


#Детальная информация по вакансии

class VacancyDetailView(LoginRequiredMixin,DetailView):
    model = Skills_table
    template_name = 'parserapp/vacancy.html'

    context_object_name = 'post'
    def get(self, request, *args, **kwargs):
        self.vac_id = kwargs['id']
        return super().get(request, *args, **kwargs)
    def get_object(self, queryset=None):
        vac = Vacancy.objects.filter(pk=self.vac_id,user=self.request.user,vis=True)
        results = []
        for post in vac:
            k = post.skils.all()
            z = []
            for y in k:
                z.append(y)
            guv = [post] + [z]
            results.append(guv)
        return results

#обновление или добавление данных
class CommentUpdataView(LoginRequiredMixin,UpdateView):
    fields = ('comment',)
    model = Vacancy
    success_url = reverse_lazy(f'parser:results')
    template_name = 'parserapp/comment.html'

#список скилов

class SkillListView(LoginRequiredMixin,ListView):
    model = Skills_table
    template_name = "parserapp/skills_table_list.html"
    context_object_name = 'skils'
    paginate_by = 20
    def get_queryset(self):
        results = Skills_table.objects.extra(
            select=dict(key="content_item.data -> 'skil'")
        ).values('skil').order_by('skil').annotate(total=Count('skil'))

        results = sorted(results, key=itemgetter('total'), reverse=True)
        return results

#список вакансий по выбранному скилу

class SkilVacDetailView(LoginRequiredMixin,DetailView):
    model = Skills_table
    template_name = 'parserapp/skil_vacanc.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        self.skil = kwargs['skil']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        vacanc = Vacancy.objects.prefetch_related('skils')
        results = []
        skil = 0
        for post in vacanc:
            k = post.skils.all()
            z = []
            for y in k:
                z.append(y)
                if self.skil == y.skil:
                    skil += 1
            if skil > 0:
                guv = [post] + [z]
                results.append(guv)
                skil = 0
        return results

class VacDeleteView(LoginRequiredMixin,UpdateView):
    fields = ('vis',)
    model = Vacancy
    success_url = reverse_lazy(f'parser:results')
    template_name = 'parserapp/vac_delete.html'
