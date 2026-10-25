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

def closest_pair_caso_base(jogadores: list[Jogador]) -> ResultadoParMaisProximo:
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

def closest_pair_recursivo(
    jogadores_por_x: list[Jogador],
    jogadores_por_y: list[Jogador]
) -> ResultadoParMaisProximo:
    
    if len(jogadores_por_x) <= 3:
        return closest_pair_caso_base(jogadores_por_x)

    meio = len(jogadores_por_x) // 2
    jogadores_esquerda_x = jogadores_por_x[:meio]
    jogadores_direita_x = jogadores_por_x[meio:]

    ids_esquerda = {jogador.id for jogador in jogadores_esquerda_x}
    jogadores_esquerda_y = [
        jogador for jogador in jogadores_por_y if jogador.id in ids_esquerda
    ]
    jogadores_direita_y = [
        jogador for jogador in jogadores_por_y if jogador.id not in ids_esquerda
    ]

    resultado_esquerda = closest_pair_recursivo(
        jogadores_esquerda_x,
        jogadores_esquerda_y,
    )
    resultado_direita = closest_pair_recursivo(
        jogadores_direita_x,
        jogadores_direita_y,
    )

    if resultado_esquerda.distancia <= resultado_direita.distancia:
        return resultado_esquerda

    return resultado_direita
