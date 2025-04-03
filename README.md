# Pong Game

Este é um simples jogo de Pong desenvolvido em Python usando a biblioteca Pygame, feito com a IA ChatGPT para fins de estudo. O objetivo é jogar contra outro jogador (ou contra você mesmo, no caso de controle local) e marcar pontos ao fazer a bola passar pela raquete do adversário. O jogo termina quando um dos jogadores atinge 10 pontos.

## Requisitos

- Python 3.x
- Biblioteca Pygame

## Como rodar o projeto

### 1. Instalar o Python

Se você ainda não tem o Python instalado, você pode baixá-lo e instalá-lo a partir do site oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/).

### 2. Instalar o Pygame

O Pygame é a biblioteca usada para criar a interface gráfica do jogo. Para instalá-la, abra o terminal ou prompt de comando e execute o seguinte comando:

```bash
pip install pygame
```

### 3. Baixar o código do jogo

 Clone ou baixe o repositório com o código fonte do jogo. Se você está usando Git, você pode executar:
```bash
git clone https://seu-repositorio.git
```
Ou você pode baixar o arquivo .zip diretamente e extrair em uma pasta de sua escolha.

### 4. Rodar o jogo
Para rodar o jogo, abra o terminal ou prompt de comando e navegue até a pasta onde o arquivo pong.py (ou o nome que você deu ao seu script) está localizado. Em seguida, execute o seguinte comando:

```bash
python pong.py
```
O jogo será iniciado e você poderá jogar com um amigo localmente usando as teclas:

W e S para mover a raquete da esquerda para cima e para baixo.

Setas para cima e setas para baixo para mover a raquete da direita para cima e para baixo.

### 5. Finalização do jogo
O jogo terminará quando um dos jogadores atingir 10 pontos. A pontuação será registrada no arquivo pontuacoes.txt, que será criado na pasta onde o jogo está rodando. O arquivo de pontuação armazenará os resultados após cada partida.

### 6. Personalização
Você pode alterar a velocidade da bola, a velocidade das raquetes e as dimensões da tela e da bola diretamente no código, editando as variáveis no início do script.

### Como funciona
O jogo é controlado por teclado com as teclas W e S para o jogador da esquerda e as setas para o jogador da direita.

O jogo tem uma pausa de 1 segundo após cada ponto.

O vencedor é o primeiro a alcançar 10 pontos.

A pontuação final é salva no arquivo pontuacoes.txt.
