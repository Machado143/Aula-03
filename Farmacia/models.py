from django.db import models

# Create your models here.
class Medicamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()



class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    medicamento = models.ManyToManyField(
        to=Medicamento,
        related_name='clientes',
        through='ClienteMedicamento',
        through_fields=('cliente', 'medicamento'),
    )



class ClienteMedicamento(models.Model):
    cliente = models.ForeignKey(
        to=Cliente,
        on_delete=models.CASCADE,
    )
    medicamento = models.ForeignKey(
        to=Medicamento,
        on_delete=models.CASCADE,
    )

