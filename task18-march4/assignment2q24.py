"""24.Implement the game rock, paper, scissors
Rock smashes scissors.
Paper covers rock.
Scissors cut paper.
"""

import random


def get_user_choice():
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"


def play_game(player_name):
    print(f"\nLet's play Rock, Paper, Scissors, {player_name}!")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\n{player_name} chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(f"\n{result}")

    return result


def display_game_summary(
    player_name,
    total_rounds,
    user_wins,
    computer_wins,
    ties,
    user_score,
    computer_score,
):
    print("\nGame Summary:")
    print(f"Total Rounds Played: {total_rounds}")
    print(f"{player_name} won {user_wins} rounds.")
    print(f"Computer won {computer_wins} rounds.")
    print(f"Tied {ties} rounds.")
    print(f"Overall Score - {player_name}: {user_score}, Computer: {computer_score}")


def main():
    player_name = input("Enter your name: ")
    total_rounds = 0
    user_wins = 0
    computer_wins = 0
    ties = 0
    user_score = 0
    computer_score = 0

    print(f"Welcome to Rock, Paper, Scissors, {player_name}!")

    while True:
        result = play_game(player_name)
        total_rounds += 1

        if "You win" in result:
            user_wins += 1
            user_score += 1
        elif "Computer wins" in result:
            computer_wins += 1
            computer_score += 1
        else:
            ties += 1

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            display_game_summary(
                player_name,
                total_rounds,
                user_wins,
                computer_wins,
                ties,
                user_score,
                computer_score,
            )
            print("\nThanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
