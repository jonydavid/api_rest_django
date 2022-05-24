from django.db import models

CATEGORIAS = (
    ('Basico', 'Basico'),
    ('Premium', 'Premium')
)

class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60,blank=True, null=True)
    categoria = models.CharField(choices=CATEGORIAS, null=True, max_length=50)

class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50,blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=15,blank=True, null=True)
    ingrediente = models.ManyToManyField(to=Ingrediente)

    def get_pizza_detail(self):
        return (ingrediente.nombre for ingrediente in self.ingrediente.all())

    def get_total_ingredientes(self):
        return self.ingrediente.all().count()
