import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
GAMES_TO_WIN_MATCH = 5
MIDDLE_SQUARE = 5
BEGINNING_PLAYER = "choose"

WINNING_LINES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
    [1, 5, 9], [3, 5, 7]              # diagonals
]

def prompt(message):
    print(f"=> {message}")

def display_board(board):
    os.system('clear')

    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print()
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print()

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def join_or(choices, main_delimiter=', ', end_delimiter='or'):
    match len(choices):
        case 0:
            return ""
        case 1:
            return str(choices[0])
        case _:
            choices_string = [str(num) for num in choices]
            return f"{main_delimiter.join(choices_string[:-1])} {end_delimiter} {choices_string[-1]}"

def get_validated_input(prompt_message, valid_options):
    while True:
        prompt(prompt_message)
        answer = input().lower().strip()
        if answer in valid_options:
            return answer
        prompt(f"Please enter one of: {', '.join(valid_options)}")

def alternate_player(current_player):
    return "computer" if current_player == "player" else "player"

def choose_square(board, current_player):
    if current_player == "player":
        player_chooses_square(board)
    else:
        computer_chooses_square(board)

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square: {join_or(valid_choices)}")
        square = input().strip()
        if square in valid_choices:
            break

        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER

def find_at_risk_square(line, board, marker):
    markers_in_line = [board[square] for square in line]

    if markers_in_line.count(marker) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
    return None

def computer_chooses_square(board):
    square = None
    for line in WINNING_LINES:
        square = find_at_risk_square(line, board, COMPUTER_MARKER) or find_at_risk_square(line, board, HUMAN_MARKER)
        if square:
            break

    if not square:
        square = MIDDLE_SQUARE if board[MIDDLE_SQUARE] == INITIAL_MARKER else random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
               and board[sq2] == HUMAN_MARKER
               and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
               and board[sq2] == COMPUTER_MARKER
               and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def check_match_winner(score, winner):
    if score[winner] == GAMES_TO_WIN_MATCH:
        prompt(f"Match finished. {winner} won the match! Final score: Player {score['Player']} | Computer {score['Computer']}")
        return True
    else:
        prompt(f"{winner} won! Current score: Player {score['Player']} | Computer {score['Computer']}")
        return False

def play_tic_tac_toe(first_player):
    score = {'Player': 0, 'Computer': 0}

    if first_player == "choose":
        first_player_key = get_validated_input(
            'Who should begin: (p)layer or (c)omputer (choose "p" or "c")',
            ["p", "c"]
        )

        first_player = "player" if first_player_key == "p" else "computer"

    while True:
        board = initialize_board()

        current_player = first_player
        while True:
            display_board(board)
            choose_square(board, current_player)
            current_player = alternate_player(current_player)

            if someone_won(board) or board_full(board):
                break

        display_board(board)

        if someone_won(board):
            winner = detect_winner(board)
            score[winner] += 1

            if check_match_winner(score, winner):
                score = {'Player': 0, 'Computer': 0}
                answer = get_validated_input("Play another match? (y or n)", ["y", "n"])
            else:
                answer = get_validated_input("Play again? (y or n)", ["y", "n"])
        else:
            prompt("It's a tie!")
            answer = get_validated_input("Play again? (y or n)", ["y", "n"])

        if answer == "n":
            prompt('Thanks for playing Tic Tac Toe!')
            return

play_tic_tac_toe(BEGINNING_PLAYER)