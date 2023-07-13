import pygame
import json
from constantes import *

def cargar_json_data(path:str) -> list:
    '''
    La funcion importa los datos del json.
    Recibe por parametro la URL del json.
    Retorna la lista que contiene dicho archivo con su informacion.
    '''
    with open(path, "r") as file:
        lista = json.load(file)
    return lista["levels"]

