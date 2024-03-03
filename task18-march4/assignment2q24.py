"""24.Implement the game rock, paper, scissors
Rock smashes scissors.
Paper covers rock.
Scissors cut paper.
"""

import random

def get_user_choice():
    # Function to get the user's choice
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_opponent_choice(opponent_name, is_computer):
    # Function to get the opponent's random choice or user's choice
    if is_computer:
        return random.choice(["rock", "paper", "scissors"])
    else:
        return get_user_choice()

def determine_winner(user_choice, opponent_choice):
    # Function to determine the winner of the round
    if user_choice == opponent_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and opponent_choice == "scissors")
        or (user_choice == "paper" and opponent_choice == "rock")
        or (user_choice == "scissors" and opponent_choice == "paper")
    ):
        return "You win!"
    else:
        return "Opponent wins!"

def play_game(player_name, opponent_name, play_with_computer):
    # Function to play a single round of the game
    print(f"\nLet's play Rock, Paper, Scissors, {player_name}!")

    user_choice = get_user_choice()
    print(f"\nLet's play Rock, Paper, Scissors, {opponent_name}!")
    opponent_choice = get_opponent_choice(opponent_name, play_with_computer)

    print(f"\n{player_name} chose: {user_choice}")
    print(f"{opponent_name} chose: {opponent_choice}")

    result = determine_winner(user_choice, opponent_choice)
    print(f"\n{result}")

    return result

def display_game_summary(
    player_name,
    opponent_name,
    total_rounds,
    user_wins,
    opponent_wins,
    ties,
    user_score,
    opponent_score,
):
    # Function to display the game summary
    print("\nGame Summary:")
    print(f"Total Rounds Played: {total_rounds}")
    print(f"{player_name} won {user_wins} rounds.")
    print(f"{opponent_name} won {opponent_wins} rounds.")
    print(f"Tied {ties} rounds.")
    print(f"Overall Score - {player_name}: {user_score}, {opponent_name}: {opponent_score}")

def main():
    # Main function to run the Rock, Paper, Scissors game
    player_name = input("Enter your name: ")  # Get the player's name

    # Ask if the user wants to play with the computer or other players
    play_with_computer = input("Do you want to play with the computer? (y/n): ").lower() == "y"

    if not play_with_computer:
        opponent_name = input("your opponent: ")
    else:
        opponent_name = "Computer"

    # Initialize game variables
    total_rounds = 0
    user_wins = 0
    opponent_wins = 0
    ties = 0
    user_score = 0
    opponent_score = 0

    print(f"Welcome to Rock, Paper, Scissors, {player_name}!")
    print(f"Welcome to Rock, Paper, Scissors, {opponent_name}!")

    while True:
        # Play a round of the game
        result = play_game(player_name, opponent_name, play_with_computer)
        total_rounds += 1

        # Update game statistics based on the result
        if "You win" in result:
            user_wins += 1
            user_score += 1
        elif "Opponent wins" in result:
            opponent_wins += 1
            opponent_score += 1
        else:
            ties += 1

        # Ask if the player wants to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            # Display the game summary when the player decides to stop
            display_game_summary(
                player_name,
                opponent_name,
                total_rounds,
                user_wins,
                opponent_wins,
                ties,
                user_score,
                opponent_score,
            )
            print("\nThanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
