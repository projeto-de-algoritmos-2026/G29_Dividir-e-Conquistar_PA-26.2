from src.closest_pair import encontra_closest_pair
from src.jogador import gera_jogadores

QTDE_JOGADORES = 100 #temporario

def main() -> None:
    jogadores = gera_jogadores(QTDE_JOGADORES)
    resultado = encontra_closest_pair(jogadores)

    for jogador in jogadores:
        print(f"Jogador {jogador.id}: ({jogador.x:.2f}, {jogador.y:.2f})")

    print(
        f"\nJogadores mais próximos: {resultado.jogador1.id} e "
        f"{resultado.jogador2.id}"
    )
    print(f"Distância: {resultado.distancia:.2f}")

if __name__ == "__main__":
    main()
