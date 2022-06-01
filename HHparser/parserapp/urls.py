from django.urls import path
from parserapp import views


app_name = 'parserapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('form/', views.form_post, name='form'),
    path('results/', views.result, name='results'),
]