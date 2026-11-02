# G29_Dividir-e-Conquistar_PA-26.2

## Execução

Na raiz do projeto, abra a interface com:

```bash
python -m src.main
```

Na janela:

- **Jogadores**: quantidade de jogadores no mapa (2 a 100);
- **Gerar jogadores**: sorteia novas posições;
- **Encontrar par mais próximo**: executa o Closest Pair e destaca o par em vermelho;
- **Mostrar divisões**: exibe os cortes da recursão (laranja = divisão principal, cinza = divisões internas) e a faixa central em amarelo.

### Testes

```bash
pip install -r requirements.txt
python -m pytest
```
