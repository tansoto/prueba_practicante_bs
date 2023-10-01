from django.urls import path
from .views import Menu, CRUD, agregarpokemon, eliminarPokemon, editarPokemon, editarPokemon2

urlpatterns = [
    path('', Menu),
    path('CRUD/', CRUD),
    path('addPokemon/', agregarpokemon),
    path('eliminarPokemon/<int:id_pokemon>/', eliminarPokemon),
    path('editarPoke/<int:id_pokemon>/', editarPokemon),
    path('editarPokemon/', editarPokemon2)
]
