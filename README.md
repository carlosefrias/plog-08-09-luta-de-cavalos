# Luta de Cavalos

Luta de Cavalos is a two-player game where each player controls a knight on a 10x10 board. The goal is to accumulate the most points by moving the knight to different positions on the board. The game ends when there are no more valid moves, and the player with the most points wins.

## How to Play

1. The game starts with two knights: the white knight (`W`) and the black knight (`B`).
2. The white knight is controlled by the computer using the minimax algorithm with alpha-beta pruning.
3. The black knight is controlled by the player using mouse clicks.
4. Each square on the board contains a number. Moving a knight to a square adds the number on that square to the player's points.
5. The game alternates turns between the white knight and the black knight.
6. The game ends when there are no more valid moves for either knight.
7. The player with the most points at the end of the game wins.

## How to Run

1. Ensure you have Python and Pygame installed on your system.
2. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/lutaDeCavalos.git
    ```
3. Navigate to the repository directory:
    ```bash
    cd lutaDeCavalos
    ```
4. Run the game:
    ```bash
    python luta_de_cavalos.py
    ```

## Controls

- **Black Knight (Player):** Click on a valid move to move the black knight.
- **White Knight (Computer):** The computer will automatically move the white knight using the minimax algorithm.

## Scoring

- Each square on the board contains a number.
- Moving a knight to a square adds the number on that square to the player's points.
- The player with the most points at the end of the game wins.

## Example

![Game Screenshot](screenshot.png)

Enjoy playing Luta de Cavalos!
