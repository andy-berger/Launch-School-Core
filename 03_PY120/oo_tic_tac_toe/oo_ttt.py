import random
import os

def clear_screen():
    os.system("clear")

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    def __str__(self):
        return self.marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

class Board:
    def __init__(self):
        self.reset()

    def reset(self):
        self.squares = {key: Square() for key in range(1, 10)}

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}")
        print("     |     |")
        print()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def is_full(self):
        return len(self.unused_squares()) == 0

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

    def display_with_clear(self):
        clear_screen()
        print("\n")
        self.display()

    def is_unused_square(self, key):
        return self.squares[key].is_unused()

    def unused_squares(self):
        return [key for key in self.squares if self.is_unused_square(key)]

class Player:
    def __init__(self, marker):
        self.marker = marker
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    def increment_score(self):
        self.score += 1

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),  # top row of the board
        (4, 5, 6),  # center row of the board
        (7, 8, 9),  # bottom row of the board
        (1, 4, 7),  # left column of the board
        (2, 5, 8),  # middle column of the board
        (3, 6, 9),  # right column of the board
        (1, 5, 9),  # diagonal: top-left to bottom-right
        (3, 5, 7)   # diagonal: top-right to bottom-left
    )

    MATCH_GOAL = 3

    @staticmethod
    def _join_or(elements, delimiter=", ", final_word="or"):
        elements_as_string = [str(element) for element in elements]
        length = len(elements)

        if length == 0:
            return ""
        if length == 1:
            return elements_as_string[0]
        if length == 2:
            return (f"{elements_as_string[0]} {final_word} "
                    f"{elements_as_string[1]}")

        return (f"{delimiter.join(elements_as_string[:-1])}{delimiter}"
                f"{final_word} {elements_as_string[-1]}")

    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self.first_player = self.human

    def play(self):
        self.display_welcome_message()

        while True:
            self.play_one_game()

            if (self.is_match_winner(self.human) or
                self.is_match_winner(self.computer)):
                winner = ("human" if self.human.score >
                self.computer.score else "computer")
                print(f"Match over after the {winner} won"
                      f"{self.MATCH_GOAL} times.")
                break

            if not self.play_again():
                break

            self.first_player = self.toggle_player(self.first_player)

            print("Let's play again!")
            print()
        self.display_goodbye_message()

    def play_one_game(self):
        current_player = self.first_player
        self.board.reset()
        self.board.display()

        while True:
            self.player_moves(current_player)
            if self.is_game_over():
                break

            self.board.display_with_clear()
            current_player = self.toggle_player(current_player)

        self.board.display_with_clear()
        self.update_match_score()
        self.display_results()

    def play_again(self):
        while True:
            answer = input("Play again (y/n)? ").lower()

            if answer in ["y", "n"]:
                break

            print("Sorry, that's not a valid choice.\n")

        clear_screen()
        return answer == "y"

    def display_welcome_message(self):
        clear_screen()
        print("Welcome to Tic Tac Toe!")
        print()

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    def display_results(self):
        if self.is_winner(self.human):
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            print("I won! Take that, human!")
        else:
            print("A tie game. How boring.")

        print(f"Score - Human: {self.human.score} | "
              f"Computer: {self.computer.score}")

    def human_moves(self):
        while True:
            valid_choices = self.board.unused_squares()
            printable_choices = TTTGame._join_or(valid_choices)
            prompt = f"Choose a square ({printable_choices}): "
            choice = input(prompt)

            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, that's not a valid choice.")
            print()

        self.board.mark_square_at(choice, self.human.marker)

    def computer_moves(self):
        # chose a square to win
        choice_offensive = self.offensive_computer_move()

        # try to block an immediate threat
        choice_defensive = self.defensive_computer_move()

        if choice_offensive:
            choice = choice_offensive
        elif choice_defensive:
            choice = choice_defensive
        else:
            choice = self.pick_center_square()

        if not choice:
            choice = self.pick_random_square()

        self.board.mark_square_at(choice, self.computer.marker)

    def opportunistic_computer_move(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            key = self.critical_square(row, player)
            if key:
                return key

        return None

    def critical_square(self, row, player):
        if self.board.count_markers_for(player, row) == 2:
            for key in row:
                if self.board.is_unused_square(key):
                    return key

        return None

    def defensive_computer_move(self):
        return self.opportunistic_computer_move(self.human)

    def offensive_computer_move(self):
        return self.opportunistic_computer_move(self.computer)

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def someone_won(self):
        return (self.is_winner(self.human) or
                self.is_winner(self.computer))

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True

        return False

    def pick_center_square(self):
        # pick center square (#5) if available
        return 5 if self.board.is_unused_square(5) else None

    def pick_random_square(self):
        valid_choices = self.board.unused_squares()
        return random.choice(valid_choices)

    def update_match_score(self):
        if self.is_winner(self.human):
            self.human.increment_score()
        elif self.is_winner(self.computer):
            self.computer.increment_score()

    def is_match_winner(self, player):
        return player.score >= self.MATCH_GOAL

    def player_moves(self, player):
        if player is self.human:
            self.human_moves()
        else:
            self.computer_moves()

    def toggle_player(self, player):
        return self.computer if player is self.human else self.human

game = TTTGame()
game.play()
