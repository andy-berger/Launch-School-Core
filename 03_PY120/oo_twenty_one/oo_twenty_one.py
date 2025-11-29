import random

class Card:
    def __init__(self):
        # STUB
        # What attributes does a card need? Rank? Suit?
        #   Points?
        pass

class Deck:
    SUITS = ('H', 'D', 'S', 'C')
    VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    def __init__(self):
        self.deck = [f"{v}{s}" for v in self.VALUES for s in self.SUITS]
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Participant:
    def __init__(self):
        self.hand = []

    def score(self):
        ranks = [card[:-1] for card in self.hand]
        total, aces = 0, 0

        for rank in ranks:
            if rank in ("J", "Q", "K"):
                total += 10
            elif rank == "A":
                total += 11
                aces += 1
            else:
                total += int(rank)

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total

    def is_busted(self):
        return self.score() > 21

class Player(Participant):
    pass

class Dealer(Participant):
    pass

class TwentyOneGame:
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()
        self.bankroll = 5

    def start(self):
        self.display_welcome_message()

        while 0 < self.bankroll < 10:
            self.setup_round()
            print(f"Bankroll: ${self.bankroll}")
            self.deal_cards()
            self.show_cards()
            self.player_turn()

            if self.player.is_busted():
                winner = "dealer"
                self.apply_payout(winner)
                self.display_result()
                if not self.play_again():
                    break

                continue

            self.dealer_turn()
            winner = self.determine_winner()
            self.apply_payout(winner)
            self.display_result()

            if not self.play_again():
                break

        self.display_goodbye_message()

    def deal_cards(self):
        self.player.hand = [self.deck.deal(), self.deck.deal()]
        self.dealer.hand = [self.deck.deal(), self.deck.deal()]

    def show_cards(self, hide_dealer=True):
        print(f"Player: {self.hand_str(self.player.hand)} | "
              f"Total: {self.player.score()}")

        if hide_dealer:
            hidden = ["??"] + self.dealer.hand[1:]
            print(f"Dealer: {self.hand_str(hidden)}")
        else:
            print(f"Dealer: {self.hand_str(self.dealer.hand)} | "
                  f"Total: {self.dealer.score()}")

    def player_turn(self):
        while True:
            player_choice = input("Would you like to (h)it or "
                                  "(s)tay? ").strip().lower()

            if player_choice not in ["h", "s"]:
                print("Sorry, you must enter 'h' or 's'.")
                continue

            if player_choice == "h":
                self.player.hand.append(self.deck.deal())
                print("You chose to hit!")
                self.show_cards(hide_dealer=True)

                if self.player.is_busted():
                    return

            if player_choice == "s":
                return

    def dealer_turn(self):
        print("Dealer's turn...")
        self.show_cards(hide_dealer=False)

        while self.dealer.score() < 17:
            print("Dealer hits!")
            self.dealer.hand.append(self.deck.deal())
            self.show_cards(hide_dealer=False)

        if self.dealer.is_busted():
            print("Dealer busted!")
            return

        print(f"Dealer stays at {self.dealer.score()}.")

    def display_welcome_message(self):
        print("Welcome to Twenty-One!")

    def display_goodbye_message(self):
        print("Thank you for playing Twenty-One!")

    def display_result(self):
        player_total, dealer_total = self.player.score(), self.dealer.score()

        if player_total > 21:
            print("You busted! Dealer wins!")
        elif dealer_total > 21:
            print("Dealer busted! You win!")
        elif dealer_total < player_total:
            print("You win!")
        elif dealer_total > player_total:
            print("Dealer wins!")
        else:
            print("It's a tie!")

        print(f"Bankroll: ${self.bankroll}")

    def setup_round(self):
        self.player.hand = []
        self.dealer.hand = []

    def determine_winner(self):
        player_total, dealer_total = self.player.score(), self.dealer.score()

        if player_total > 21:
            return "dealer"
        if dealer_total > 21:
            return "player"
        if player_total > dealer_total:
            return "player"
        if dealer_total > player_total:
            return "dealer"

        return "tie"

    def apply_payout(self, winner):
        if winner == "player":
            self.bankroll += 1
        elif winner == "dealer":
            self.bankroll -= 1

    def play_again(self):
        if self.bankroll == 0:
            print("You're broke. Game over.")
            return False
        if self.bankroll == 10:
            print("You're rich! Game over.")
            return False

        while True:
            answer = input("Play again (y/n): ").strip().lower()
            if answer in ["y", "yes"]:
                return True
            if answer in ["n", "no"]:
                return False
            print("Invalid input. Please enter 'y' or 'n'.")

    def hand_str(self, cards):
        return ", ".join(cards)

game = TwentyOneGame()
game.start()