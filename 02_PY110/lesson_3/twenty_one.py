import random
import os

DECK_SUITS = ["H", "D", "C", "S"]
DECK_NUMERIC_VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
DECK_VALUES = DECK_NUMERIC_VALUES + ["J", "Q", "K", "A"]
DECK_TERMS = {"J": "Jack", "Q": "Queen", "K": "King", "A": "Ace"}
TARGET_SCORE = 21
DEALER_MIN_STAY = 17
TARGET_WINS = 3

def shuffle_deck(deck):
    random.shuffle(deck)

def initialize_deck():
    deck = []
    for suit in DECK_SUITS:
        for value in DECK_VALUES:
            deck.append([suit, value])

    shuffle_deck(deck)
    return deck

def deal_cards(deck):
    return deck.pop()

def deal_initial_cards(deck):
    return [deal_cards(deck), deal_cards(deck)]

def translate_card(card):
    if card[1] in DECK_NUMERIC_VALUES:
        return card[1]

    return DECK_TERMS[card[1]]

def prompt(message):
    print(f"=> {message}")

def get_validated_input(prompt_message, valid_options):
    prompt(f"{prompt_message} ")
    while True:
        answer = input().lower().strip()
        if answer in valid_options:
            return answer
        prompt(f"Please enter one of: {', '.join(valid_options)}")

def player_turn():
    answer = get_validated_input("Please choose: hit or stay?", ["hit", "stay", "h", "s"])
    return answer

def total(cards):
    # cards = [['H', '3'], ['S', 'Q'], ... ]
    values = [card[1] for card in cards]

    sum_val = 0
    for value in values:
        if value == "A":
            sum_val += 11
        elif value in ['J', 'Q', 'K']:
            sum_val += 10
        else:
            sum_val += int(value)

    # correct for Aces
    aces = values.count("A")
    while sum_val > TARGET_SCORE and aces:
        sum_val -= 10
        aces -= 1

    return sum_val

def busted(cards):
    return total(cards) > TARGET_SCORE

def determine_winner(player_hand, dealer_hand):
    player_score = total(player_hand)
    dealer_score = total(dealer_hand)

    winner = None
    reason = None
    score = f"Player score: {player_score} | Dealer score: {dealer_score}"

    if busted(player_hand):
        winner, reason = "Dealer", "Player busted"
    elif busted(dealer_hand):
        winner, reason = "Player", "Dealer busted"
    elif player_score == dealer_score:
        reason = "It's a tie"
    elif player_score > dealer_score:
        winner, reason = "Player", "Player won"
    elif player_score < dealer_score:
        winner, reason = "Dealer", "Dealer won"

    return winner, reason, score

def announce_winner(player_hand, dealer_hand):
    winner, reason, score = determine_winner(player_hand, dealer_hand)

    if "busted" in reason:
        prompt(f"{reason}, {winner.lower()} won! {score}")
    elif reason == "It's a tie":
        prompt(f"{reason}! {score}")
    else:
        prompt(f"{reason}! {score}")

def hit(deck, cards):
    return cards + [deal_cards(deck)]

def play_twenty_one():
    deck = initialize_deck()
    player_hand = deal_initial_cards(deck)
    dealer_hand = deal_initial_cards(deck)

    prompt(f"Dealer has: {translate_card(dealer_hand[0])} and unknown card")
    prompt(f"You have:   {translate_card(player_hand[0])} and {translate_card(player_hand[1])}")

    player_total = total(player_hand)
    prompt(f"Your total is: {player_total}")

    while True:
        player_decision = player_turn()
        if player_decision in ["hit", "h"]:
            player_hand = hit(deck, player_hand)
            player_total = total(player_hand)
            prompt(f"You chose to hit! Your cards are now: {', '.join(translate_card(card) for card in player_hand)}")
            prompt(f"Your total is now: {player_total}")
            if busted(player_hand):
                break
        elif player_decision in ["stay", "s"]:
            prompt("You chose to stay!")
            break

    if not busted(player_hand):
        prompt(f"Dealer reveals: {translate_card(dealer_hand[0])} and {translate_card(dealer_hand[1])}")
        prompt(f"Dealer's total is: {total(dealer_hand)}")

        while total(dealer_hand) < DEALER_MIN_STAY:
            dealer_hand = hit(deck, dealer_hand)
            prompt(f"Dealer hits! Dealer's cards are now: {', '.join(translate_card(card) for card in dealer_hand)}")
            prompt(f"Dealer's total is now: {total(dealer_hand)}")

    announce_winner(player_hand, dealer_hand)
    winner = determine_winner(player_hand, dealer_hand)[0]
    return winner

def is_match_over(player_wins, dealer_wins):
    return player_wins >= TARGET_WINS or dealer_wins >= TARGET_WINS

def play_match():
    round = 1
    wins_player = 0
    wins_dealer = 0
    match_over = is_match_over(wins_player, wins_dealer)

    os.system("clear")
    prompt("=== Welcome to Twenty-One ===")
    prompt(f"The player who wins {TARGET_WINS} times first wins the match.")
    prompt("Press any key to continue.")
    input()

    while not match_over:
        os.system("clear")
        prompt(f"=== Round {round} of Twenty-One ===")
        round += 1
        winner = play_twenty_one()
        if winner == "Player":
            wins_player += 1
        elif winner == "Dealer":
            wins_dealer += 1

        match_over = is_match_over(wins_player, wins_dealer)

        if not match_over:
            prompt(f"Round wins so far: Player: {wins_player} | Dealer: {wins_dealer}")
            another_round = get_validated_input("Play another round? (y/n)", ["y", "n"])
            if another_round == "n":
                prompt("Thank you for playing Twenty-One!")
                break

    match_winner = "Player" if wins_player > wins_dealer else "Dealer"
    times_word_player = "times" if wins_player == 0 or wins_player > 1 else "time"
    times_word_dealer = "times" if wins_dealer == 0 or wins_dealer > 1 else "time"
    prompt(f"{match_winner} is the match winner! Player won {wins_player} {times_word_player} | Dealer won {wins_dealer} {times_word_dealer}")

play_match()