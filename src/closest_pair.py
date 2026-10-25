from dataclasses import dataclass
from math import hypot

from src.jogador import Jogador

@dataclass
class ClosestPair:
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

def encontra_closest_pair(jogadores: list[Jogador]) -> ClosestPair:
    if len(jogadores) < 2:
        raise ValueError("Necessário pelo menos dois jogadores")

    jogadores_por_x = ordena_jogadores_por_x(jogadores)
    jogadores_por_y = ordena_jogadores_por_y(jogadores)

    return closest_pair_recursivo(jogadores_por_x, jogadores_por_y)

def closest_pair_caso_base(jogadores: list[Jogador]) -> ClosestPair:
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

    return ClosestPair(
        jogador1=jogador1,
        jogador2=jogador2,
        distancia=menor_distancia,
    )

def closest_pair_recursivo(
    jogadores_por_x: list[Jogador],
    jogadores_por_y: list[Jogador]
) -> ClosestPair:
    
    if len(jogadores_por_x) <= 3:
        return closest_pair_caso_base(jogadores_por_x)

    meio = len(jogadores_por_x) // 2
    jogadores_esquerda_x = jogadores_por_x[:meio]
    jogadores_direita_x = jogadores_por_x[meio:]
    x_divisao = jogadores_por_x[meio].x

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

    melhor_resultado = resultado_esquerda
    if resultado_direita.distancia < resultado_esquerda.distancia:
        melhor_resultado = resultado_direita

    jogadores_faixa = [
        jogador
        for jogador in jogadores_por_y
        if abs(jogador.x - x_divisao) < melhor_resultado.distancia
    ]

    return closest_pair_faixa(jogadores_faixa, melhor_resultado)

def closest_pair_faixa(
    jogadores_faixa: list[Jogador],
    melhor_resultado: ClosestPair,
) -> ClosestPair:
    for primeiro in range(len(jogadores_faixa)):
        limite = min(primeiro + 8, len(jogadores_faixa))

        for segundo in range(primeiro + 1, limite):
            jogador1 = jogadores_faixa[primeiro]
            jogador2 = jogadores_faixa[segundo]

            if jogador2.y - jogador1.y >= melhor_resultado.distancia:
                break

            distancia = calcula_distancia_euclidiana(jogador1, jogador2)

            if distancia < melhor_resultado.distancia:
                melhor_resultado = ClosestPair(
                    jogador1=jogador1,
                    jogador2=jogador2,
                    distancia=distancia,
                )

    return melhor_resultado
