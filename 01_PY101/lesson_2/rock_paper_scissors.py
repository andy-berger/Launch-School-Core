import random

VALID_CHOICES = ["rock", "paper", "scissors", "spock", "lizard"]

def prompt(message):
    print(f"==> {message}")

def display_welcome_message():
    welcome_message = "Welcome to Rock, Paper, Scissors, Spock, Lizard!"
    print(f"{welcome_message}\n{"-" * len(welcome_message)}")

def determine_winner(player, computer):
    winning_conditions = [
        ("rock", "scissors"), ("rock", "lizard"),
        ("paper", "rock"), ("paper", "spock"),
        ("scissors", "paper"), ("scissors", "lizard"),
        ("spock", "rock"), ("spock", "scissors"),
        ("lizard", "spock"), ("lizard", "paper")
    ]
    if (player, computer) in winning_conditions:
        return "player"

    if (computer, player) in winning_conditions:
        return "computer"

    return "tie"

def display_winner(winner):
    if winner == "player":
        prompt("You win!")
    elif winner == "computer":
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

def keep_score(winner, score_player, score_computer):
    if winner == "player":
        score_player += 1
    elif winner == "computer":
        score_computer += 1

    return (score_player, score_computer)

def get_user_choice():
    prompt(f"Choose one: {", ".join(VALID_CHOICES)}")
    prompt("You may type in just the first "
           "letter or first two letters. If needed, "
           "you will be asked for clarification.")
    choice = input()

    match choice.casefold():
        case "r" | "ro":
            choice = "rock"
        case "p" | "pa":
            choice = "paper"
        case "s":
            choice = "scissors_or_spock"
        case "sc":
            choice = "scissors"
        case "sp":
            choice = "spock"
        case "l":
            choice = "lizard"

    scissors_or_spock_choice = ""
    if choice == "scissors_or_spock":
        while scissors_or_spock_choice not in ["1", "2"]:
            prompt('Please clarify your choice of "s". '
                   'Select "1" for scissors or "2" for spock.')
            scissors_or_spock_choice = input()

    if scissors_or_spock_choice == "1":
        choice = "scissors"
    elif scissors_or_spock_choice == "2":
        choice = "spock"

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    return choice

def run_game(player_score, computer_score):
    display_welcome_message()
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(VALID_CHOICES)

        prompt(f"You chose {user_choice}, computer chose {computer_choice}")

        winner_result = determine_winner(user_choice, computer_choice)
        display_winner(winner_result)

        player_score, computer_score = keep_score(
            winner_result, player_score, computer_score)
        winner_text = ("You are the" if player_score > computer_score
        else "The computer is the")

        if player_score >= 3 or computer_score >= 3:
            prompt(f"The game is over. {winner_text} grand winner! "
                f"Your score: {player_score} "
                f"Computer's score: {computer_score}")
            break

        prompt(f"Your score: {player_score} "
            f"Computer's score: {computer_score}")

        prompt("Do you want to play again? (y/n)?")
        answer = input().casefold()
        while True:
            if answer.startswith("n") or answer.startswith("y"):
                break

            prompt('Please enter "y" or "n".')
            answer = input().casefold()

        if answer[0] == "n":
            break

run_game(0, 0)