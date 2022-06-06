from django import forms
from .models import Vacancy


class SearchForm(forms.Form):
    data = (('name', 'В названии вакансии'),
            ('company_name', 'В названии компании'),
            ('description', 'В описание'))
    delite = (('delit','Удалить'),('no_delit','Не удалять'))
    name = forms.CharField(label='Поисковый запрос',widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))

    where = forms.ChoiceField(choices=data, label='Где искать',widget=forms.Select(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    delit = forms.ChoiceField(choices=delite, label='Удалить данные из БД',widget=forms.Select(attrs={'placeholder': 'Name', 'class': 'form-control'}))



class ComentForm(forms.ModelForm):

    comment = forms.CharField(label='Введите коментарий для вакансии',widget=forms.Textarea(attrs={'placeholder': 'Коментарий', 'class': 'form-control'}))

    class Meta:
        model = Vacancy
        fields = ('comment',)
