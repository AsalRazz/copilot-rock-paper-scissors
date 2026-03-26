# Write a rock, paper, scissors, lizard, spock game
# import random module
import random
# define main function that handles all the logic
def main():
    # define a list of choices
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    # define winning combinations: key beats all values in its list
    winning_moves = {
        "rock":     ["scissors", "lizard"],
        "paper":    ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard":   ["paper", "spock"],
        "spock":    ["rock", "scissors"],
    }
    # loop until the user chooses to stop
    while True:
        # display numbered menu including stop option
        print("\nChoose your option:")
        for i, choice in enumerate(choices, 1):
            print(f"  {i}.  {choice.capitalize()}")
        print(f"  {len(choices) + 1}.  Stop")
        # get user input by number
        try:
            selection = int(input("\nEnter number: "))
            if selection < 1 or selection > len(choices) + 1:
                raise ValueError
        except ValueError:
            print(f"Invalid choice. Please enter a number between 1 and {len(choices) + 1}.")
            continue
        # stop the game if the user selects the stop option
        if selection == len(choices) + 1:
            print("Thanks for playing. Goodbye!")
            break
        user_choice = choices[selection - 1]
        print(f"You chose: {user_choice.capitalize()}")
        # get computer choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice.capitalize()}")
        # determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif computer_choice in winning_moves[user_choice]:
            print("You win!")
        else:
            print("Computer wins!")
# call the main function
if __name__ == "__main__":
    main()