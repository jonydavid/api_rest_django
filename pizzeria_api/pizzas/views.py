import errno
from django.contrib import auth
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import permissions, status
from .models import Pizza, Ingrediente
from .serializers import DetallePizzaSerializer, GetTodasLasPizzasSerializer, IngredienteSerializer, PizzaData
from rest_framework.response import Response
from rest_framework_simplejwt import authentication
from rest_framework.authentication import  BasicAuthentication

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([BasicAuthentication, authentication.JWTAuthentication])
def crear_pizza(request):
    if request.user.is_staff | request.user.is_superuser:
        serializer = PizzaData(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Solo puede modificar super user o staff")

@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([BasicAuthentication, authentication.JWTAuthentication])
def put_pizza(request):
    if request.user.is_staff | request.user.is_superuser:
        try:
            pizzas = Pizza.objects.get(id=request.data['id'])
            pizzas.nombre=request.data['nombre']
            pizzas.precio=request.data['precio']
            pizzas.estado=request.data['estado']
            pizzas.save()
            return Response("ok", status=status.HTTP_201_CREATED)
        except errno:
            return Response(errno, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Solo puede modificar super user o staff")

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([BasicAuthentication, authentication.JWTAuthentication])
def get_pizzas(request):
    queryset = Pizza.objects.all().filter(estado="ACTIVO")
    if request.user.is_superuser:
        queryset = Pizza.objects.all()

    serializer = GetTodasLasPizzasSerializer(
        queryset,
        context={'request': request},
        many=True
    )
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([BasicAuthentication, authentication.JWTAuthentication])
def get_detail(request):
    queryset = Pizza.objects.all().filter(id=request.data['id'])
    serializer = DetallePizzaSerializer(
        queryset,
        context={'request': request},
        many=True
    )

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([BasicAuthentication, authentication.JWTAuthentication])
def crear_ingrediente(request, format=None):
    if request.user.is_staff | request.user.is_superuser:
        serializer = IngredienteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Solo puede modificar super user o staff")

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([BasicAuthentication, authentication.JWTAuthentication])
def get_ingredientes(request):

    queryset = Ingrediente.objects.all()

    serializer = IngredienteSerializer(
        queryset,
        context={'request': request},
        many=True
    )

    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([BasicAuthentication, authentication.JWTAuthentication])
def put_ingrediente(request):
    if request.user.is_staff | request.user.is_superuser:
        try:
            ingrediente = Ingrediente.objects.get(id=request.data['id'])
            ingrediente.nombre=request.data['nombre']
            ingrediente.precio=request.data['categoria']
            ingrediente.save()
            return Response("ok", status=status.HTTP_201_CREATED)
        except errno:
            return Response(errno, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Solo puede modificar super user o staff")

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([BasicAuthentication, authentication.JWTAuthentication])
def delete_ingrediente(request):
    pizza =Pizza.objects.filter(ingrediente__id=request.data['id'])
    if pizza.count()>0:
       return Response("No se puede eliminar")
    else:

        if request.user.is_staff | request.user.is_superuser:
            try:
                ingrediente = Ingrediente.objects.get(id=request.data['id'])
                ingrediente.delete()
                return Response("ok", status=status.HTTP_201_CREATED)
            except errno:
                return Response(errno, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Solo puede modificar super user o staff")

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([BasicAuthentication, authentication.JWTAuthentication])
def add_ingrediente(request):
    pizza = Pizza.objects.get(id=request.data['id'])
    topping = Ingrediente.objects.get(id=request.data['ingrediente'])
    pizza.ingrediente.add(topping)

    return Response("ok",status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([BasicAuthentication, authentication.JWTAuthentication])
def remove_ingrediente(request):
    pizza = Pizza.objects.get(id=request.data['id'])
    topping = Ingrediente.objects.get(id=request.data['ingrediente'])
    pizza.ingrediente.remove(topping)

    return Response("ok",status=status.HTTP_201_CREATED)
