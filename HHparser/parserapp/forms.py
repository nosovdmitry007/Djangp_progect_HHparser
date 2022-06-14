from django import forms
from .models import Vacancy


class SearchForm(forms.Form):
    data = (('name', 'В названии вакансии'),
            ('company_name', 'В названии компании'),
            ('description', 'В описание'))
    delite = (('no_delit','Не удалять'),('delit','Удалить'))
    name = forms.CharField(label='Поисковый запрос',widget=forms.TextInput(attrs={'placeholder': 'Запрос', 'class': 'form-control'}))

    where = forms.ChoiceField(choices=data, label='Где искать',widget=forms.Select(attrs={'class': 'form-control'}))
    res = forms.CharField(label='Сколько результатов поиска выводить',
                           widget=forms.TextInput(attrs={'placeholder': 'Кол-во вакансий', 'class': 'form-control'}))

    delit = forms.ChoiceField(choices=delite, label='Удалить данные из БД',widget=forms.Select(attrs={'class': 'form-control'}))



class ComentForm(forms.ModelForm):

    comment = forms.CharField(label='Введите коментарий для вакансии',widget=forms.Textarea(attrs={'placeholder': 'Коментарий', 'class': 'form-control'}))

    class Meta:
        model = Vacancy
        fields = ('comment',)
