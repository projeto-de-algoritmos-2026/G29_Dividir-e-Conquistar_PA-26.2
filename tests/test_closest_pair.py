from itertools import combinations
from math import isclose
from random import Random

import pytest

from src.closest_pair import calcula_distancia_euclidiana, encontra_closest_pair
from src.jogador import Jogador

def test_calcula_distancia_euclidiana() -> None:
    jogador1 = Jogador(id=1, x=0, y=0)
    jogador2 = Jogador(id=2, x=3, y=4)

    assert calcula_distancia_euclidiana(jogador1, jogador2) == 5

def test_encontra_par_entre_as_duas_metades() -> None:
    jogadores = [
        Jogador(id=1, x=0, y=0),
        Jogador(id=2, x=5, y=5),
        Jogador(id=3, x=6, y=5),
        Jogador(id=4, x=10, y=0),
    ]

    resultado = encontra_closest_pair(jogadores)

    assert {resultado.jogador1.id, resultado.jogador2.id} == {2, 3}
    assert resultado.distancia == 1

def test_encontra_jogadores_na_mesma_posicao() -> None:
    jogadores = [
        Jogador(id=1, x=0, y=0),
        Jogador(id=2, x=10, y=10),
        Jogador(id=3, x=10, y=10),
        Jogador(id=4, x=30, y=30),
    ]

    resultado = encontra_closest_pair(jogadores)

    assert {resultado.jogador1.id, resultado.jogador2.id} == {2, 3}
    assert resultado.distancia == 0

def test_resultado_equivale_a_comparacao_de_todos_os_pares() -> None:
    gerador = Random(42)
    jogadores = [
        Jogador(
            id=identificador,
            x=gerador.uniform(0, 1000),
            y=gerador.uniform(0, 1000),
        )
        for identificador in range(1, 101)
    ]
    distancia_esperada = min(
        calcula_distancia_euclidiana(jogador1, jogador2)
        for jogador1, jogador2 in combinations(jogadores, 2)
    )

    resultado = encontra_closest_pair(jogadores)

    assert isclose(resultado.distancia, distancia_esperada)

def test_nao_altera_a_lista_original() -> None:
    jogadores = [
        Jogador(id=1, x=30, y=30),
        Jogador(id=2, x=10, y=10),
        Jogador(id=3, x=20, y=20),
    ]
    ordem_original = jogadores.copy()

    encontra_closest_pair(jogadores)

    assert jogadores == ordem_original

@pytest.mark.parametrize("jogadores", [[], [Jogador(id=1, x=0, y=0)]])
def test_exige_pelo_menos_dois_jogadores(jogadores: list[Jogador]) -> None:
    with pytest.raises(ValueError, match="pelo menos dois"):
        encontra_closest_pair(jogadores)