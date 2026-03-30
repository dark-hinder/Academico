from django.db import models

# Create your models here.
    #class Pessoa:

class Ocupacao(models.Model):
    nome = models.CharField(max_length=25, null=False, blank=False, verbose_name="Ocupação")

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name="Ocupacao"
        verbose_name_plural="Ocupacoes"
    
    #Class Ensino:
        
class AreaSaber(models.Model):
    nome = models.CharField(max_length=25, null=False, blank=False, verbose_name="Áreas do Saber")

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name="Saber"
        verbose_name_plural="Saberes"