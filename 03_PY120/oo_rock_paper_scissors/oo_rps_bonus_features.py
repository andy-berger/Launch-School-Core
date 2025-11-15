import random

class Move:
    name = ""
    beats = set()

    def defeats(self, other):
        return other.name in self.beats

    def __str__(self):
        return self.name

class Rock(Move):
    name= "rock"
    beats = {"scissors", "lizard"}

class Paper(Move):
    name= "paper"
    beats = {"rock", "spock"}

class Scissors(Move):
    name= "scissors"
    beats = {"paper", "lizard"}

class Lizard(Move):
    name= "lizard"
    beats = {"spock", "paper"}

class Spock(Move):
    name= "spock"
    beats = {"scissors", "rock"}

class Player:
    def __init__(self):
        self.move = None

class Computer(Player):
    def choose(self):
        self.move = random.choice(CHOICES)()

CHOICES = (Rock, Paper, Scissors, Spock, Lizard)

MOVE_BY_NAME = {
    "lizard": Lizard,
    "paper": Paper,
    "rock": Rock,
    "scissors": Scissors,
    "spock": Spock,
}

class Human(Player):
    def choose(self):
        prompt = "Please choose rock, paper, scissors, spock or lizard: "

        while True:
            choice = input(prompt).strip().lower()
            move_cls = MOVE_BY_NAME.get(choice)
            if move_cls:
                self.move = move_cls()
                return

            print(f"Sorry, {choice} is not valid")

class R2D2(Computer):
    def choose(self):
        self.move = Rock()

class HAL(Computer):
    def choose(self):
        self.move = random.choices(
            CHOICES,
            weights=[1, 1, 2, 1, 1]
        )[0]()

class Daneel(Computer):
    def __init__(self):
        super().__init__()
        self.last_human_move = None

    def choose(self):
        if self.last_human_move is not None:
            self.move = type(self.last_human_move)()
        else:
            self.move = random.choice(CHOICES)()

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = random.choice([R2D2, HAL, Daneel])()
        self._human_score = 0
        self._computer_score = 0
        self._max_score = 5
        self._move_history = []
        self._prev_human_move = None

    def _display_rules(self):
        print("\nRules:")
        print(" - Rock crushes Scissors and Lizard")
        print(" - Paper covers Rock and disproves Spock")
        print(" - Scissors cuts Paper and decapitates Lizard")
        print(" - Lizard eats Paper and poisons Spock")
        print(" - Spock vaporizes Rock and smashes Scissors\n")

    def _display_welcome_message(self):
        print("Welcome to Rock Paper Scissors Lizard Spock!")
        self._display_rules()
        print(f"You are playing against {self._computer.__class__.__name__}.")

    def _display_goodbye_message(self):
        print("Thanks for playing Rock Paper Scissors Lizard Spock. Goodbye!")

        if self._move_history:
            print("Move history:")
            for round_number, move in enumerate(self._move_history, 1):
                print(f"Round {round_number} - "
                      f"You: {move['human']} | "
                      f"Computer: {move['computer']} | "
                      f"Round winner: {move['round_winner']}"
                      )

    def _round_result(self):
        human_move, computer_move = self._human.move, self._computer.move

        if human_move.name == computer_move.name:
            return "tie"

        return "human" if human_move.defeats(computer_move) else "computer"

    def _display_winner(self):
        print(f"You chose: {self._human.move}")
        print(f"The computer chose: {self._computer.move}")

        result = self._round_result()
        if result == "human":
            print("You win!")
            self._track_score("human")
        elif result == "computer":
            print("Computer wins!")
            self._track_score("computer")
        else:
            print("It's a tie")

        print(f"Score - You: {self._human_score} | "
              f"Computer: {self._computer_score}")
        self._move_history.append({
            "human": self._human.move.name,
            "computer": self._computer.move.name,
            "round_winner": result
        })

    def _track_score(self, winner):
        if winner == "human":
            self._human_score += 1
        else:
            self._computer_score += 1

    def _reached_max_score(self):
        return (self._human_score >= self._max_score or
                self._computer_score >= self._max_score)

    def _display_grand_winner(self):
        winner = (
            "You" if self._human_score > self._computer_score
            else "Computer"
            )
        verb = "are" if winner == "You" else "is"
        print(f"{winner} {verb} the grand winner! "
        f"First to reach a score of {self._max_score}.")

    def play(self):
        self._display_welcome_message()

        while True:
            if hasattr(self._computer, "last_human_move"):
                self._computer.last_human_move = self._prev_human_move

            self._human.choose()
            self._computer.choose()
            self._display_winner()
            self._prev_human_move = self._human.move

            if self._reached_max_score():
                self._display_grand_winner()
                break

            if not self._play_again():
                break

        self._display_goodbye_message()

    def _play_again(self):
        while True:
            answer = (input("Would you like to play again? (y/n) ")
                      .strip()
                      .lower())

            if answer in ["y", "yes"]:
                return True
            if answer in ["n", "no"]:
                return False
            print("Please enter 'y' or 'n'.")

RPSGame().play()