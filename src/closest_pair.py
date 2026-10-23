from math import hypot

from src.jogador import Jogador

def calcula_distancia_euclidiana(primeiro: Jogador, segundo: Jogador) -> float:
    return hypot(segundo.x - primeiro.x, segundo.y - primeiro.y)
