from multiprocessing import context
from rest_framework import serializers

from pizzeria_api.pizzas.models import Ingrediente, Pizza

class PizzaData(serializers.ModelSerializer):
    class Meta:
        model= Pizza
        fields = '__all__'

class IngredienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingrediente
        fields = (
            'nombre',
            'categoria'
        )

class GetTodasLasPizzasSerializer(serializers.ModelSerializer):
    total_ingredientes = serializers.ReadOnlyField(source='get_total_ingredientes')

    class Meta:
        model = Pizza
        fields = (
            'id',
            'nombre',
            'precio',
            'total_ingredientes'

        )

class DetallePizzaSerializer(serializers.ModelSerializer):
    ingredientes =  serializers.ReadOnlyField(source='get_pizza_detail')
    class Meta:
        model = Pizza
        fields = (
            'nombre',
            'precio',
            'estado',
            'ingredientes'
        )
