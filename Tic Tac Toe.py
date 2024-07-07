import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check if player wins or not.
def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False

# Minimax function, It recursively evaluates all possible moves to find the best one.
def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -float("inf")
        for (i, j) in get_empty_cells(board):
            board[i][j] = "O"
            eval = minimax(board, depth + 1, False)
            board[i][j] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for (i, j) in get_empty_cells(board):
            board[i][j] = "X"
            eval = minimax(board, depth + 1, True)
            board[i][j] = " "
            min_eval = min(min_eval, eval)
        return min_eval

# This function uses the minimax function to find the best possible move for the AI
def best_move(board):
    best_score = -float("inf")
    move = None
    for (i, j) in get_empty_cells(board):
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

# This is the main function that sets up the game loop.
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human = "X"
    ai = "O"

    while True:
        print_board(board)

        if check_winner(board, human):
            print("User wins!")
            break
        if check_winner(board, ai):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        human_turn = input("Your move (row col): ").split()
        if human_turn:
            row, col = int(human_turn[0]), int(human_turn[1])
            if make_move(board, row, col, human):
                if is_full(board) or check_winner(board, human):
                    continue
                print_board(board)
                print("AI is thinking...")
                row, col = best_move(board)
                make_move(board, row, col, ai)

if __name__ == "__main__":
    main()