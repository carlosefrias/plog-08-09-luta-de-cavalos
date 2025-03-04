import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 10, 10
SQUARE_SIZE = WIDTH // COLS
TOP_BAR_HEIGHT = 50

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Inicialização da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT + TOP_BAR_HEIGHT))
pygame.display.set_caption("Luta de Cavalos")

# Função para criar o tabuleiro com números aleatórios
def create_board():
    numbers = [f"{i:02d}" for i in range(100)]
    random.shuffle(numbers)
    board = [[numbers[row * COLS + col] for col in range(COLS)] for row in range(ROWS)]
    return board

# Função para desenhar o tabuleiro com movimentos válidos destacados e jogador atual
def draw_board(board, valid_moves=[], current_player=None, white_points=0, black_points=0):
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            if (row, col) in valid_moves or (current_player and (row, col) == get_knight_position(board, "W" if current_player == "white" else "B")):
                color = BLUE
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE + TOP_BAR_HEIGHT, SQUARE_SIZE, SQUARE_SIZE))
            font = pygame.font.SysFont(None, 40)
            text = font.render(board[row][col], True, RED)
            screen.blit(text, (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + 20 + TOP_BAR_HEIGHT))

    # Desenha a barra superior com os pontos
    font = pygame.font.SysFont(None, 40)
    white_text = font.render(f"White: {white_points}", True, BLACK)
    black_text = font.render(f"Black: {black_points}", True, BLACK)
    screen.blit(white_text, (10, 10))
    screen.blit(black_text, (WIDTH - black_text.get_width() - 10, 10))

# Função para obter a posição do cavalo
def get_knight_position(board, knight):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == knight:
                return (row, col)
    return (None, None)

# Função para verificar se a posição é válida
def is_valid_position(row, col):
    return 0 <= row < ROWS and 0 <= col < COLS

# Função para obter movimentos válidos do cavalo
def get_knight_moves(row, col, board):
    moves = [
        (row + 2, col + 1), (row + 2, col - 1),
        (row - 2, col + 1), (row - 2, col - 1),
        (row + 1, col + 2), (row + 1, col - 2),
        (row - 1, col + 2), (row - 1, col - 2)
    ]
    return [(r, c) for r, c in moves if is_valid_position(r, c) and board[r][c] != "--" and board[r][c] != "W" and board[r][c] != "B"]

# Função para remover números simétricos
def remove_symmetric(board, number):
    if number[0] != number[1]:
        symmetric_number = number[1] + number[0]
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == symmetric_number:
                    board[row][col] = "--"

# Função para mover o cavalo e acumular pontos
def move_knight(board, knight, row, col, points):
    current_row, current_col = get_knight_position(board, knight)
    if current_row is not None and current_col is not None:
        board[current_row][current_col] = "--"  # Marca a casa como inacessível
    points += int(board[row][col])
    remove_symmetric(board, board[row][col])
    board[row][col] = knight
    return points

# Função para obter a posição do clique do usuário
def get_click_position(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def minimax(board, depth, is_maximizing, knight, points, alpha, beta):
    if depth == 0:
        return points

    moves = get_knight_moves(*get_knight_position(board, knight), board)
    if is_maximizing:
        max_eval = float('-inf')
        for move in moves:
            new_board = [row[:] for row in board]
            new_points = move_knight(new_board, knight, move[0], move[1], points)
            eval = minimax(new_board, depth - 1, False, knight, new_points, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in moves:
            new_board = [row[:] for row in board]
            new_points = move_knight(new_board, knight, move[0], move[1], points)
            eval = minimax(new_board, depth - 1, True, knight, new_points, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board, knight, points):
    best_move = None
    best_value = float('-inf')
    moves = get_knight_moves(*get_knight_position(board, knight), board)
    for move in moves:
        new_board = [row[:] for row in board]
        new_points = move_knight(new_board, knight, move[0], move[1], points)
        move_value = minimax(new_board, 3, False, knight, new_points, float('-inf'), float('inf'))
        if move_value > best_value:
            best_value = move_value
            best_move = move
    return best_move

# Função principal do jogo
def main():
    board = create_board()
    white_knight = "W"
    black_knight = "B"
    white_points = 0
    black_points = 0
    move_knight(board, white_knight, 0, 0, white_points)  # Coloca o cavalo branco na primeira linha
    move_knight(board, black_knight, 9, 9, black_points)  # Coloca o cavalo preto na última linha

    running = True
    turn = "white"
    valid_moves = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and turn == "black":
                pos = pygame.mouse.get_pos()
                row, col = get_click_position(pos)
                if (row, col) in valid_moves:
                    black_points = move_knight(board, black_knight, row, col, black_points)
                    turn = "white"
                    valid_moves = []

        if turn == "white" and not valid_moves:
            best_move = get_best_move(board, white_knight, white_points)
            if best_move:
                white_points = move_knight(board, white_knight, best_move[0], best_move[1], white_points)
                turn = "black"
            else:
                running = False

        if turn == "black" and not valid_moves:
            valid_moves = get_knight_moves(*get_knight_position(board, black_knight), board)
            if not valid_moves:
                running = False

        draw_board(board, valid_moves, turn, white_points, black_points)
        pygame.display.flip()

    if white_points > black_points:
        print("White wins with", white_points, "points!")
    elif black_points > white_points:
        print("Black wins with", black_points, "points!")
    else:
        print("It's a tie!")

    pygame.quit()

if __name__ == "__main__":
    main()