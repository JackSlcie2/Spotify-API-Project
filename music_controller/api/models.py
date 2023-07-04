from django.db import models
import random
import string

def generate_inique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, 
                                      k=length))
        if Pacientes.objects.filter(code=code).count() == 0:
            break
    return code


# Create your models here.
class Pacientes(models.Model):
    cpf = models.CharField(max_length=14, 
                            default='', 
                            unique=True)
    rg = models.CharField(max_length=14, 
                            default='', 
                            unique=True)
    nome = models.CharField(max_length=50, 
                            default='', 
                            unique=False)
    dia = models.CharField(max_length=2,
                            unique=False)
    mes = models.CharField(max_length=2,
                            unique=False)
    ano = models.CharField(max_length=4,
                            unique=False)

    
