from django.urls import path
from .views import Menu, CRUD, agregarpokemon, eliminarPokemon

urlpatterns = [
    path('', Menu),
    path('CRUD/', CRUD),
    path('addPokemon/', agregarpokemon),
    path('eliminarPokemon/<int:id_pokemon>/', eliminarPokemon)
]
