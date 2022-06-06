# Поиск вакансий
import requests
import time
from parserapp.models import Vacancy, Skills_table, Params


def hh_serch(tex, param, del_bd):

    url = 'https://api.hh.ru/vacancies'

    Params.objects.all().delete()
    if del_bd == 'delit':
        Vacancy.objects.all().delete()
        Skills_table.objects.all().delete()
    else:
        pass

    if param == "name":
        ser = 'В названии вакансии '
    elif param == "company_name":
        ser = 'В названии компании'
    elif param == "description":
        ser ='В описание'


    Params.objects.create(name_search=tex, where_search=ser)

    vac = 0
    key = []
    skills=[]
    for i in range(1):
        time.sleep(1)
        params = {
            'text': tex,
            'search_field': param,
            'page': i,
            'area': 1,
        }

        result = requests.get(url, params=params).json()

        for z in range(20):
            try:

                if result['items'][z]['salary']:
                    if result['items'][z]['salary']['from'] :

                        zp1='от ' + str(result['items'][z]['salary']['from'])
                    else:
                        zp1=''
                    if result['items'][z]['salary']['to']:
                       zp2 = ' до ' + str(result['items'][z]['salary']['to'])
                    else:
                        zp2=''
                    zp=zp1 + zp2 + ' ' + result['items'][z]['salary']['currency']
                else:
                    zp = 'Не указана'

                ab = result['items'][z]['snippet']['responsibility'].replace('<highlighttext>', '')
                ab = ab.replace('</highlighttext>','')

                vac = Vacancy.objects.create(name=result['items'][z]['name'], salary=zp,
                                       about=ab,
                                       link=result['items'][z]['alternate_url'])

                for skills_vac in requests.get(result['items'][z]['url']).json()['key_skills']:
                    skill_vacancy = skills_vac['name']
                    # if skill_vacancy not in skills:
                    #
                    #     skills.append(skill_vacancy)
                        # try:
                    vac.skils.create(skil=skill_vacancy)
                        # except:
                        #     pass

            except:
                pass

