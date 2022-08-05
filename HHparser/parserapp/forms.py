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

class PhotoFilterForm(forms.Form):
    form = (('jpeg', 'JPEG'),
            ('jpg', 'JPG'),
            ('cr', 'Kodak: CR'),
            ('k25', 'Kodak: K25'),
            ('kdc', 'Kodak: KDC'),
            ('crw', 'Canon: CRW'),
            ('cr2', 'Canon: CR2'),
            ('cr3', 'Canon: CR3'),
            ('erf', 'Epson: ERF'),
            ('nef', 'Nikon: NEF'),
            ('nrw', 'Nikon: NRW'),
            ('orf', 'Olympus: ORF'),
            ('pef', 'Pentax: PEF'),
            ('rw2', 'Panasonic: RW2'),
            ('arw', 'Sony: ARW'),
            ('srf', 'Sony: SRF'),
            ('sr2', 'Sony: SR2'))
    put = forms.CharField(label='Путь к папке с фотографиями',widget=forms.TextInput(attrs={'placeholder': 'Путь', 'class': 'form-control'}))
    format = forms.ChoiceField(choices=form, label='Расширение файлов',widget=forms.Select(attrs={'class': 'form-control'}))
