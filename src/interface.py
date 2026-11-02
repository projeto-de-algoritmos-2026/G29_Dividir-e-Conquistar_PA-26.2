import tkinter as tk

from src.jogador import (
    ALTURA_MAPA,
    LARGURA_MAPA,
    MAX_JOGADORES,
    MIN_JOGADORES,
    Jogador,
    gera_jogadores,
)

TAMANHO_MAPA = 600
MARGEM = 10
ESCALA = TAMANHO_MAPA / max(LARGURA_MAPA, ALTURA_MAPA)
RAIO = 5

class Interface:
    def __init__(self, janela: tk.Tk) -> None:
        self.janela = janela
        self.janela.title("Closest Pair - Jogadores mais próximos")

        controles = tk.Frame(janela)
        controles.pack(padx=10, pady=(10, 0), fill="x")

        tk.Label(controles, text="Jogadores:").pack(side="left")
        self.quantidade = tk.IntVar(value=20)
        tk.Spinbox(
            controles, from_=MIN_JOGADORES, to=MAX_JOGADORES,
            textvariable=self.quantidade, width=5,
        ).pack(side="left", padx=5)
        tk.Button(
            controles, text="Gerar jogadores", command=self.gera_novos_jogadores
        ).pack(side="left")

        lado = TAMANHO_MAPA + 2 * MARGEM
        self.canvas = tk.Canvas(janela, width=lado, height=lado, bg="white")
        self.canvas.pack(padx=10, pady=10)

        self.gera_novos_jogadores()

    def gera_novos_jogadores(self) -> None:
        try:
            quantidade = self.quantidade.get()
        except tk.TclError:
            quantidade = 0

        # se digitarem algo fora do limite, ajusta para o mais proximo
        quantidade = max(MIN_JOGADORES, min(MAX_JOGADORES, quantidade))
        self.quantidade.set(quantidade)

        self.jogadores = gera_jogadores(quantidade)
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
