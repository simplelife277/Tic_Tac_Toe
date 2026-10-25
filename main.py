def display_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    moves = 0

    while True:
        display_board(board)
        print(f"Player {player}'s turn")

        try:
            position = int(input("Choose a position (1-9): "))
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue

        if position < 1 or position > 9:
            print("Invalid position. Choose 1-9.")
            continue

        row = (position - 1) // 3
        col = (position - 1) % 3

        if board[row][col] != " ":
            print("That position is already occupied!")
            continue

        board[row][col] = player
        moves += 1

        if check_winner(board, player):
            display_board(board)
            print(f"Player {player} wins!")
            break

        if moves == 9:
            display_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"


while True:
    play_game()
    again = input("Play again? (yes/no): ").strip().lower()

    if again not in ("yes", "y"):
        print("Thanks for playing!")
        break
