import pygame
import sys
import time  # Para adicionar a pausa de 1 segundo

# Inicializa o pygame
pygame.init()

# Definir a largura e altura da janela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong")

# Definir as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Definir a bola e as raquetes
RAQUETE_LARGURA = 15
RAQUETE_ALTURA = 90
BOLA_RAIO = 10

# Velocidade das raquetes e da bola (declaradas globalmente)
raquete_velocidade = 10
bola_velocidade_x = 7
bola_velocidade_y = 7

# Função para desenhar as raquetes e a bola
def desenhar_raquete(x, y):
    pygame.draw.rect(tela, BRANCO, (x, y, RAQUETE_LARGURA, RAQUETE_ALTURA))

def desenhar_bola(x, y):
    pygame.draw.circle(tela, BRANCO, (x, y), BOLA_RAIO)

# Função para salvar a pontuação em um arquivo de texto
def salvar_pontuacao(pontos_esquerda, pontos_direita):
    with open("pontuacoes.txt", "a") as arquivo:
        arquivo.write(f"Esquerda: {pontos_esquerda} - Direita: {pontos_direita}\n")

# Função principal do jogo
def main():
    global bola_velocidade_x, bola_velocidade_y  # Usar variáveis globais

    # Posições iniciais
    raquete_esquerda_y = (ALTURA - RAQUETE_ALTURA) // 2
    raquete_direita_y = (ALTURA - RAQUETE_ALTURA) // 2
    bola_x = LARGURA // 2
    bola_y = ALTURA // 2

    # Pontuação
    pontos_esquerda = 0
    pontos_direita = 0

    # Controle de tempo
    clock = pygame.time.Clock()

    # Loop principal do jogo
    while True:
        # Verificar eventos (teclado, fechar janela)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                # Salvar a pontuação antes de fechar
                salvar_pontuacao(pontos_esquerda, pontos_direita)
                pygame.quit()
                sys.exit()

        # Obter os teclados pressionados
        teclas = pygame.key.get_pressed()

        # Movimentação das raquetes
        if teclas[pygame.K_w] and raquete_esquerda_y > 0:
            raquete_esquerda_y -= raquete_velocidade
        if teclas[pygame.K_s] and raquete_esquerda_y < ALTURA - RAQUETE_ALTURA:
            raquete_esquerda_y += raquete_velocidade

        if teclas[pygame.K_UP] and raquete_direita_y > 0:
            raquete_direita_y -= raquete_velocidade
        if teclas[pygame.K_DOWN] and raquete_direita_y < ALTURA - RAQUETE_ALTURA:
            raquete_direita_y += raquete_velocidade

        # Movimento da bola
        bola_x += bola_velocidade_x
        bola_y += bola_velocidade_y

        # Colisão com a parte superior e inferior
        if bola_y - BOLA_RAIO <= 0 or bola_y + BOLA_RAIO >= ALTURA:
            bola_velocidade_y = -bola_velocidade_y

        # Colisão com as raquetes
        if bola_x - BOLA_RAIO <= RAQUETE_LARGURA and raquete_esquerda_y < bola_y < raquete_esquerda_y + RAQUETE_ALTURA:
            bola_velocidade_x = -bola_velocidade_x
        if bola_x + BOLA_RAIO >= LARGURA - RAQUETE_LARGURA and raquete_direita_y < bola_y < raquete_direita_y + RAQUETE_ALTURA:
            bola_velocidade_x = -bola_velocidade_x

        # Se a bola passar das raquetes (marcar pontos)
        if bola_x - BOLA_RAIO <= 0:
            pontos_direita += 1
            bola_x, bola_y = LARGURA // 2, ALTURA // 2  # Resetar a bola
            # Pausar o jogo por 1 segundo após marcar ponto
            time.sleep(1)

        if bola_x + BOLA_RAIO >= LARGURA:
            pontos_esquerda += 1
            bola_x, bola_y = LARGURA // 2, ALTURA // 2  # Resetar a bola
            # Pausar o jogo por 1 segundo após marcar ponto
            time.sleep(1)

        # Verificar se alguém atingiu 10 pontos para finalizar o jogo
        if pontos_esquerda >= 10 or pontos_direita >= 10:
            vencedor = "Esquerda" if pontos_esquerda > pontos_direita else "Direita"
            # Salvar pontuação final
            salvar_pontuacao(pontos_esquerda, pontos_direita)
            # Mostrar mensagem de fim de jogo
            fonte = pygame.font.SysFont("Arial", 40)
            texto_fim = fonte.render(f"{vencedor} ganhou!", True, BRANCO)
            tela.fill(PRETO)
            tela.blit(texto_fim, (LARGURA // 2 - texto_fim.get_width() // 2, ALTURA // 2 - texto_fim.get_height() // 2))
            pygame.display.update()
            time.sleep(3)  # Exibir mensagem por 3 segundos
            pygame.quit()
            sys.exit()

        # Preencher a tela com fundo preto
        tela.fill(PRETO)

        # Desenhar as raquetes e a bola
        desenhar_raquete(10, raquete_esquerda_y)
        desenhar_raquete(LARGURA - RAQUETE_LARGURA - 10, raquete_direita_y)
        desenhar_bola(bola_x, bola_y)

        # Desenhar a pontuação
        fonte = pygame.font.SysFont("Arial", 30)
        texto_pontos = fonte.render(f"{pontos_esquerda}  -  {pontos_direita}", True, BRANCO)
        tela.blit(texto_pontos, (LARGURA // 2 - texto_pontos.get_width() // 2, 20))

        # Atualizar a tela
        pygame.display.update()

        # Controlar a taxa de atualização do jogo (FPS)
        clock.tick(60)

# Iniciar o jogo
if __name__ == "__main__":
    main()
