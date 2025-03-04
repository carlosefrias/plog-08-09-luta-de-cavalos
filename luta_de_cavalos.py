import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 10, 10
SQUARE_SIZE = WIDTH // COLS

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Inicialização da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Luta de Cavalos")

# Função para criar o tabuleiro com números aleatórios
def create_board():
    numbers = [f"{i:02d}" for i in range(100)]
    random.shuffle(numbers)
    board = [[numbers[row * COLS + col] for col in range(COLS)] for row in range(ROWS)]
    return board

# Função para desenhar o tabuleiro
def draw_board(board):
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            font = pygame.font.SysFont(None, 40)
            text = font.render(board[row][col], True, RED)
            screen.blit(text, (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + 20))

# Função para obter a posição do cavalo
def get_knight_position(board, knight):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == knight:
                return (row, col)
    return (None, None)

# Função para mover o cavalo
def move_knight(board, knight, row, col):
    current_row, current_col = get_knight_position(board, knight)
    if current_row is not None and current_col is not None:
        board[current_row][current_col] = "--"  # Marca a casa como inacessível
    board[row][col] = knight

# Função principal do jogo
def main():
    board = create_board()
    white_knight = "W"
    black_knight = "B"
    move_knight(board, white_knight, 0, 0)  # Coloca o cavalo branco na primeira linha
    move_knight(board, black_knight, 9, 9)  # Coloca o cavalo preto na última linha

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_board(board)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()