from dataclasses import dataclass
from random import uniform

LARGURA_MAPA = 1000
ALTURA_MAPA = 1000
MIN_JOGADORES = 2
MAX_JOGADORES = 100

@dataclass
class Jogador:
    id: int
    x: float
    y: float

def gera_jogadores(quantidade: int) -> list[Jogador]:
    return [
        Jogador(
            id=identificador,
            x=uniform(0, LARGURA_MAPA),
            y=uniform(0, ALTURA_MAPA),
        )
        for identificador in range(1, quantidade + 1)
    ]
