"""24.Implement the game rock, paper, scissors
Rock smashes scissors.
Paper covers rock.
Scissors cut paper.
"""

import random


def get_user_choice(player_name):
    while True:
        user_input = input(
            f"{player_name}, enter your choice (rock, paper, or scissors): "
        ).lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors.'")


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"


def play_game(player_names):
    print("\nLet's play Rock, Paper, Scissors!")

    results = {}

    for player in player_names:
        player_choice = get_user_choice(player)
        computer_choice = get_computer_choice()

        print(f"\n{player} chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(f"\n{result}\n")
        results[player] = result

    return results


def display_game_summary(results):
    print("\nGame Summary:")
    for player, result in results.items():
        print(f"{player}: {result}")


player_names = []
num_players = int(input("Enter the number of players: "))
for i in range(1, num_players + 1):
    player_names.append(input(f"Enter the name for Player {i}: "))

total_rounds = 0
results = {player: {"wins": 0, "ties": 0} for player in player_names}

while True:
    round_results = play_game(player_names)
    total_rounds += 1

    for player, result in round_results.items():
        if "You win" in result:
            results[player]["wins"] += 1
        elif "Computer wins" not in result:  # Assuming all other cases are ties
            results[player]["ties"] += 1

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != "y":
        display_game_summary(results)
        print("\nThanks for playing! Goodbye.")
        break
