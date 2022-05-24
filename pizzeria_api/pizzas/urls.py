from django.urls import path,include
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

api_urls = [
    path('crear_pizza', crear_pizza),
    path('put_pizza', put_pizza),
    path('get_pizzas', get_pizzas),
    path('detalle_pizzas', get_detail),
    path('crear_ingrediente', crear_ingrediente), 
    path('get_ingredientes', get_ingredientes), 
    path('put_ingrediente', put_ingrediente), 
    path('delete_ingrediente', delete_ingrediente), 
    path('add_ingrediente', add_ingrediente),
    path('remove_ingrediente', remove_ingrediente),   
]

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(api_urls)),

]

urlpatterns = format_suffix_patterns(urlpatterns)