from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return f"{self.nome} <{self.id}>"




class Evento(models.Model):
    nome = models.CharField(max_length=256)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL,null=True)
    local = models.CharField(max_length=256, blank = True)
    link = models.CharField(max_length=256, blank = True)
    data = models.DateField(null=True)
    participantes = models.IntegerField(default=0)
    #def __init__(self, nome, categoria, local=None, link=None):
        #self.nome = nome 
        #self.categoria = categoria
        #self.local = local
        #self.link = link

#aula_python = Evento(" Aula de Python", "Backend", "Salvador")
#aula_js = Evento(" Aula de Javascript", "FullStack", "Salvador")

#eventos = [
    #aula_python,
    #aula_js,
#]