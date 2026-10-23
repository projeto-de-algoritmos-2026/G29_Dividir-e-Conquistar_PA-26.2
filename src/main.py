from src.jogador import gera_jogadores

QTDE_JOGADORES = 50 #temporario

def main() -> None:
    jogadores = gera_jogadores(QTDE_JOGADORES)

    for jogador in jogadores:
        print(f"Jogador {jogador.id}: ({jogador.x:.2f}, {jogador.y:.2f})")

if __name__ == "__main__":
    main()
