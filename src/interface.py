import tkinter as tk
from time import perf_counter

from src.closest_pair import ClosestPair, encontra_closest_pair
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
        tk.Button(
            controles, text="Encontrar par mais próximo",
            command=self.encontra_par,
        ).pack(side="left", padx=5)

        lado = TAMANHO_MAPA + 2 * MARGEM
        self.canvas = tk.Canvas(janela, width=lado, height=lado, bg="white")
        self.canvas.pack(padx=10, pady=10)

        self.texto_resultado = tk.Label(janela, justify="left", font=("Arial", 10))
        self.texto_resultado.pack(padx=10, pady=(0, 10), anchor="w")

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
        self.texto_resultado.config(text="Clique em 'Encontrar par mais próximo'.")

    def encontra_par(self) -> None:
        inicio = perf_counter()
        resultado = encontra_closest_pair(self.jogadores)
        tempo_ms = (perf_counter() - inicio) * 1000

        self.desenha_jogadores()
        self.desenha_par(resultado)

        j1, j2 = resultado.jogador1, resultado.jogador2
        self.texto_resultado.config(text=(
            f"Par mais próximo: jogador {j1.id} ({j1.x:.1f}, {j1.y:.1f}) e "
            f"jogador {j2.id} ({j2.x:.1f}, {j2.y:.1f})\n"
            f"Distância: {resultado.distancia:.2f}   |   "
            f"Tempo: {tempo_ms:.3f} ms"
        ))

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

    def desenha_par(self, resultado: ClosestPair) -> None:
        x1, y1 = self.para_tela(resultado.jogador1)
        x2, y2 = self.para_tela(resultado.jogador2)
        self.canvas.create_line(x1, y1, x2, y2, fill="red", width=2)

        for x, y in ((x1, y1), (x2, y2)):
            self.canvas.create_oval(
                x - RAIO - 2, y - RAIO - 2, x + RAIO + 2, y + RAIO + 2,
                fill="red", outline="",
            )

def main() -> None:
    janela = tk.Tk()
    Interface(janela)
    janela.mainloop()

if __name__ == "__main__":
    main()
