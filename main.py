import random

game_is_active = True

board_spaces = set()
player_moves = set()
computer_moves = set()

# Initialize an empty board
board = [[' ' for _ in range(3)] for _ in range(3)]


win_states = [
    # Horizontal win states
    {(0, 0), (0, 1), (0, 2)},
    {(1, 0), (1, 1), (1, 2)},
    {(2, 0), (2, 1), (2, 2)},
    # Vertical win states
    {(0, 0), (1, 0), (2, 0)},
    {(0, 1), (1, 1), (2, 1)},
    {(0, 2), (1, 2), (2, 2)},
    # Diagonal win states
    {(0, 0), (1, 1), (2, 2)},
    {(0, 2), (1, 1), (2, 0)}
]


def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)


def check_win(moves):
    for win in win_states:
        if win.issubset(moves):
            return True
    return False


def is_draw():
    return all(board[row][col] != ' ' for row in range(3) for col in range(3))


while game_is_active:
    valid_input = [0, 1, 2]
    print_board(board)

    while True:  # Start of new loop for input validation
        user_row = int(input("Choose a Row 0-2: "))
        user_column = int(input("Choose a Column 0-2: "))

        # Check if input is valid
        if user_row not in valid_input or user_column not in valid_input:
            print("Invalid input, only use 0-2")
            continue  # This will skip the rest of the loop and start it over, asking for input again
        else:
            break  # Valid input received, break out of the input validation loop

    # Check if move is valid
    if board[user_row][user_column] == ' ':
        board[user_row][user_column] = 'X'
        player_moves.add((user_row, user_column))
        if check_win(player_moves):
            print_board(board)
            print("YOU WIN")
            break
        elif is_draw():
            print_board(board)
            print("ITS A DRAW")
            break
    else:
        print("That spot is already taken, please choose another")

    # Computers turn
    while True:
        computer_row, computer_column = random.randint(0, 2), random.randint(0, 2)
        if board[computer_row][computer_column] == ' ':
            board[computer_row][computer_column] = 'O'
            computer_moves.add((computer_row, computer_column))
            break
    if check_win(computer_moves):
        print_board(board)
        print("Computer wins!")
        break
    elif is_draw():
        print_board(board)
        print("It's a draw!")
        break
