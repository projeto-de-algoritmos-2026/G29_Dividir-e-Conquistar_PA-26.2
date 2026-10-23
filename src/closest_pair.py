from dataclasses import dataclass
from math import hypot

from src.jogador import Jogador

@dataclass
class ResultadoParMaisProximo:
    jogador1: Jogador
    jogador2: Jogador
    distancia: float

def calcula_distancia_euclidiana(primeiro: Jogador, segundo: Jogador) -> float:
    return hypot(segundo.x - primeiro.x, segundo.y - primeiro.y)

def ordena_jogadores_por_x(jogadores: list[Jogador]) -> list[Jogador]:
    return sorted(
        jogadores,
        key=lambda jogador: (jogador.x, jogador.y, jogador.id),
    )

def ordena_jogadores_por_y(jogadores: list[Jogador]) -> list[Jogador]:
    return sorted(
        jogadores,
        key=lambda jogador: (jogador.y, jogador.x, jogador.id),
    )

def encontra_par_mais_proximo(jogadores: list[Jogador]) -> ResultadoParMaisProximo:
    return

def encontra_par_mais_prox_caso_base(jogadores: list[Jogador]) -> ResultadoParMaisProximo:
    jogador1 = jogadores[0]
    jogador2 = jogadores[1]
    menor_distancia = calcula_distancia_euclidiana(jogador1, jogador2)

    for primeiro in range(len(jogadores) - 1):
        for segundo in range(primeiro + 1, len(jogadores)):
            distancia = calcula_distancia_euclidiana(
                jogadores[primeiro],
                jogadores[segundo],
            )

            if distancia < menor_distancia:
                jogador1 = jogadores[primeiro]
                jogador2 = jogadores[segundo]
                menor_distancia = distancia

    return ResultadoParMaisProximo(
        jogador1=jogador1,
        jogador2=jogador2,
        distancia=menor_distancia,
    )
