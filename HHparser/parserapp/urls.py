from django.urls import path
from parserapp import views


app_name = 'parserapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('form/', views.form_post, name='form'),
    path('results/', views.result, name='results'),
    path('vacancy/<int:id>/', views.vacancy, name='vacancy'),
    path('coment/<int:id>/', views.coment, name='coment'),
    path('skil_list/', views.SkilViews, name='skil_list'),
    path('skil_vacanc/<int:id>/', views.Skilvacancy, name='skil_vacanc')
]