from django.contrib import admin
from .models import *
from django.contrib import admin

from django.contrib import admin
from .models import *

# ---------------------------
# i) Ocupação e Pessoas
# ---------------------------
class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1


@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]


# ---------------------------
# vii) UF (Cidade) e Pessoas
# ---------------------------
class PessoaCidadeInline(admin.TabularInline):
    model = Pessoa
    extra = 1


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    inlines = [PessoaCidadeInline]


# ---------------------------
# ii) Instituição e Cursos
# ---------------------------
class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1


@admin.register(InstituicaoEnsino)
class InstituicaoAdmin(admin.ModelAdmin):
    inlines = [CursoInline]


# ---------------------------
# iii) Área do Saber e Cursos
# ---------------------------
class CursoAreaInline(admin.TabularInline):
    model = Curso
    extra = 1


@admin.register(AreaSaber)
class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoAreaInline]


# ---------------------------
# iv) Cursos e Disciplinas
# (via tabela intermediária)
# ---------------------------
class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline]


# ---------------------------
# v) Disciplinas e Avaliações
# ---------------------------
class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]


# ---------------------------
# vi) Turmas e Alunos
# (via Matrícula)
# ---------------------------
class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline]


# ---------------------------
# ix) Estudantes, Disciplinas,
# Avaliações e Frequência
# ---------------------------
class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1


class AvaliacaoPessoaInline(admin.TabularInline):
    model = Avaliacao
    extra = 1


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = [FrequenciaInline]


# ---------------------------
# Registros restantes
# ---------------------------
admin.site.register(Turno)
admin.site.register(CursoDisciplina)
admin.site.register(Matricula)
admin.site.register(AvaliacaoTipo)
admin.site.register(Frequencia)
admin.site.register(Ocorrencia)