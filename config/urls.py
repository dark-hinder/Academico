from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pessoa/', PessoasView.as_view(), name='pessoa'),
    path('matricula/', MatriculasView.as_view(), name='matricula'),
    path('cidade/', CidadesView.as_view(), name='cidade'),
    path('curso/', CursosView.as_view(), name='curso'),
    path('turma/', TurmasView.as_view(), name='turma'),
    path('ocupacao/', OcupacoesView.as_view(), name='ocupacao'),
    path('disciplina/', DisciplinasView.as_view(), name='disciplina'),
    ]

