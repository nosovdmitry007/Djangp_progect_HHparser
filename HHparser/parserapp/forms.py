from django import forms

# >>> f = ContactForm(data, initial=data)

class SearchForm(forms.Form):
    data = (('name', 'В названии вакансии'),
            ('company_name', 'В названии компании'),
            ('description', 'В описание'))
    name = forms.CharField(label='Поисковый запрос',widget=forms.TextInput(attrs={'class': 'special'}))

    where = forms.ChoiceField(choices=data, label='Где искать')