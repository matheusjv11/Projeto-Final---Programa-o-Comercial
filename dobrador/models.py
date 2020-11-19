from django.db import models

# Create your models here.
class Dobrador(models.Model):

    nome = models.CharField(max_length=100)
    elemento = models.CharField('Elemento', max_length=100, choices=[('AR', 'AR'),('ÁGUA', 'ÁGUA'),('TERRA', 'TERRA'),('FOGO', 'FOGO')])
    descricao = models.TextField('Descrição Pessoal')
    profissao = models.CharField(max_length=100)
    idade = models.IntegerField('Idade')
    genero = models.CharField('Gênero', max_length=100, choices=[('MASCULINO', 'MASCULINO'),('FEMININO', 'FEMININO'),('NEUTRO', 'NEUTRO')])
    data_cadastro = models.DateTimeField('Primeiro acesso', auto_now_add=True)
    

    def __str__(self):
        return '{0} - {1} ({2})'.format(self.nome, self.elemento, self.genero)