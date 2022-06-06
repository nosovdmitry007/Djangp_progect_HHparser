from django.urls import reverse_lazy
from parserapp.models import Params
from .models import Vacancy,Skills_table
from .forms import SearchForm
from django.views.generic import ListView, DetailView,  UpdateView, TemplateView
from .parser import hh_serch
from django.views.generic.edit import FormView

#главная страница
class AboutView(TemplateView):
    template_name = "parserapp/index.html"

#список всех вакансий
class VacancListView(ListView):
    model = Vacancy
    template_name = "parserapp/results.html"
    context_object_name = 'vac'
    def get_queryset(self):
        param = Params.objects.all()
        vac = Vacancy.objects.all()
        result=[param]+[vac]
        return result

#Форма поиска
class SearchFormView(FormView):
    template_name = 'parserapp/form.html'
    form_class = SearchForm
    success_url = reverse_lazy('parserapp:results')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        name_search = form.cleaned_data['name']
        where_search = form.cleaned_data['where']
        del_bd = form.cleaned_data['delit']
        hh_serch(name_search, where_search, del_bd)
        return super().form_valid(form)


#Детальная информация по вакансии
class VacancyDetailView(DetailView):
    model = Skills_table
    template_name = 'parserapp/vacancy.html'
    context_object_name = 'post'
    def get(self, request, *args, **kwargs):
        self.vac_id = kwargs['id']
        return super().get(request, *args, **kwargs)
    def get_object(self, queryset=None):
        vac = Vacancy.objects.filter(pk=self.vac_id)
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
class CommentUpdataView(UpdateView):
    fields = ('comment',)
    model = Vacancy
    success_url = reverse_lazy(f'parser:results')
    template_name = 'parserapp/comment.html'

#список скилов
class SkillListView(ListView):
    model = Skills_table
    template_name = "parserapp/skills_table_list.html"
    context_object_name = 'skils'
    def get_queryset(self):
        skills = []
        skils = Skills_table.objects.all()
        results = []
        for s in skils:
            if s.skil not in skills:
                skills.append(s.skil)
                col = Skills_table.objects.filter(skil=s.skil).count()
                res = [s.id] + [s.skil] + [col]
                results.append(res)
        def sort_by_col(emp):
            return emp[2]
        results.sort(key=sort_by_col, reverse=True)
        return results

#список вакансий по выбранному скилу
class SkilVacDetailView(DetailView):
    model = Skills_table
    template_name = 'parserapp/skil_vacanc.html'
    context_object_name = 'post'
    def get(self, request, *args, **kwargs):
        self.skil_id = kwargs['id']
        return super().get(request, *args, **kwargs)
    def get_object(self, queryset=None):
        vac = Vacancy.objects.all()
        sk = Skills_table.objects.filter(pk=self.skil_id)
        results = []
        skil = 0
        for post in vac:
            k = post.skils.all()
            z = []
            for y in k:
                z.append(y)
                if sk[0].skil == y.skil:
                    skil += 1
            if skil > 0:
                guv = [post] + [z]
                results.append(guv)
                skil = 0
        return results
