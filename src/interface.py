import tkinter as tk

from src.jogador import ALTURA_MAPA, LARGURA_MAPA, Jogador, gera_jogadores

TAMANHO_MAPA = 600
MARGEM = 10
ESCALA = TAMANHO_MAPA / max(LARGURA_MAPA, ALTURA_MAPA)
RAIO = 5

class Interface:
    def __init__(self, janela: tk.Tk) -> None:
        self.janela = janela
        self.janela.title("Closest Pair - Jogadores mais próximos")

        lado = TAMANHO_MAPA + 2 * MARGEM
        self.canvas = tk.Canvas(janela, width=lado, height=lado, bg="white")
        self.canvas.pack(padx=10, pady=10)

        self.jogadores = gera_jogadores(20)
        self.desenha_jogadores()

    def para_tela(self, jogador: Jogador) -> tuple[float, float]:
        # converte a posicao no mapa (0 a 1000) para pixels
        return MARGEM + jogador.x * ESCALA, MARGEM + jogador.y * ESCALA

    def desenha_jogadores(self) -> None:
        self.canvas.delete("all")

        for jogador in self.jogadores:
            x, y = self.para_tela(jogador)
            self.canvas.create_oval(
                x - RAIO, y - RAIO, x + RAIO, y + RAIO,
                fill="steelblue", outline="",
            )
            self.canvas.create_text(
                x, y - RAIO - 6, text=str(jogador.id), font=("Arial", 7)
            )

def main() -> None:
    janela = tk.Tk()
    Interface(janela)
    janela.mainloop()

if __name__ == "__main__":
    main()
