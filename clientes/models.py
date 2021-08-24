
# O /Models/ é onde estão os campos essenciais e comportamentos dos dados que serão armazenados;
# Mapeamento para a tabela do banco de dados
# https://docs.djangoproject.com/en/3.2/topics/db/models/

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=3)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name