import random
from enum import Enum

# Enum class for the game actions
class Action(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"
    LIZARD = "lizard"
    SPOCK = "spock"

# Function to determine the winner
def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        return f"Both players selected {user_action}. It's a tie!", 0
    
    # Rock beats Scissors and Lizard
    if user_action == Action.ROCK:
        if computer_action == Action.SCISSORS or computer_action == Action.LIZARD:
            return "Rock crushes Scissors or Lizard! You win!", 1
        else:
            return "Paper covers Rock or Spock disproves Rock! You lose.", -1

    # Paper beats Rock and Spock
    elif user_action == Action.PAPER:
        if computer_action == Action.ROCK or computer_action == Action.SPOCK:
            return "Paper covers Rock or disproves Spock! You win!", 1
        else:
            return "Scissors cuts Paper or Lizard eats Paper! You lose.", -1
    
    # Scissors beats Paper and Lizard
    elif user_action == Action.SCISSORS:
        if computer_action == Action.PAPER or computer_action == Action.LIZARD:
            return "Scissors cuts Paper or decapitates Lizard! You win!", 1
        else:
            return "Rock crushes Scissors or Spock smashes Scissors! You lose.", -1

    # Lizard beats Paper and Spock
    elif user_action == Action.LIZARD:
        if computer_action == Action.PAPER or computer_action == Action.SPOCK:
            return "Lizard eats Paper or poisons Spock! You win!", 1
        else:
            return "Rock crushes Lizard or Scissors decapitates Lizard! You lose.", -1

    # Spock beats Rock and Scissors
    elif user_action == Action.SPOCK:
        if computer_action == Action.ROCK or computer_action == Action.SCISSORS:
            return "Spock smashes Rock or Scissors! You win!", 1
        else:
            return "Paper disproves Spock or Lizard poisons Spock! You lose.", -1

# Main function to play the game
def play_game():
    possible_actions = [Action.ROCK, Action.PAPER, Action.SCISSORS, Action.LIZARD, Action.SPOCK]
    
    player_score = 0
    computer_score = 0
    
    while True:
        # Capture User Input
        user_input = input("Enter a choice (rock, paper, scissors, lizard, spock): ").lower()

        if user_input not in ["rock", "paper", "scissors", "lizard", "spock"]:
            print("Invalid input, please enter a valid choice.")
            continue
        
        user_action = Action[user_input.upper()]
        
        computer_action = random.choice(possible_actions)
        print(f"\nYou chose {user_action.value}, computer chose {computer_action.value}.\n")

        result_message, result = determine_winner(user_action, computer_action)
        print(result_message)
        
        # Update Scores
        if result == 1:
            player_score += 1
        elif result == -1:
            computer_score += 1
        
        print(f"Your score: {player_score} | Computer's score: {computer_score}")
        
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"Final Scores - You: {player_score}, Computer: {computer_score}")
            print("Thanks for playing! Goodbye.")
            break

# Run the game
if __name__ == "__main__":
    play_game()
