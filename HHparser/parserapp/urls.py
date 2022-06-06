from django.urls import path
from parserapp import views

app_name = 'parserapp'

urlpatterns = [
    path('', views.AboutView.as_view(), name='index'),
    path('form/', views.SearchFormView.as_view(), name='form'),
    path('results/', views.VacancListView.as_view(), name='results'),
    path('vacancy/<int:id>/', views.VacancyDetailView.as_view(), name='vacancy'),
    path('comment/<int:pk>/', views.CommentUpdataView.as_view(), name='coment'),
    path('skil_list/', views.SkillListView.as_view(), name='skil_list'),
    path('skil_vacanc/<int:id>/', views.SkilVacDetailView.as_view(), name='skil_vacanc')
]