import random
import os


def play_game(guess_number_range, max_tries):
    player_name = input("Enter your name: ")
    computer_guess = random.randint(1, guess_number_range)
    tries = 0
    won = False

    while tries < max_tries:
        player_guess = int(input(f"Guess a number (1 to {guess_number_range}): "))
        tries += 1

        if player_guess == computer_guess:
            print(f"🎉 Correct! You guessed it in {tries} tries.")
            update_scoreboard(player_name, tries, "won")
            won = True
            break
        elif player_guess > computer_guess:
            print("Too High!")
        else:
            print("Too Low!")

        print(f"Attempts left: {max_tries - tries}")

    if not won:
        print(f"❌ Sorry, the correct number was {computer_guess}")
        update_scoreboard(player_name, tries, "lost")

    replay_option = input("Do you want to play again? (Y/N): ").strip().lower()
    if replay_option == 'y':
        start_game()
    else:
        display_scoreboard()
        return "Thank you, see you next time!"


def start_game():
    difficulty = input("Welcome to the Number Guessing Game!\nChoose difficulty (Easy, Medium, Hard): ").strip().lower()

    if difficulty in ['easy', 'e']:
        return play_game(50, 10)
    elif difficulty in ['medium', 'm']:
        return play_game(100, 7)
    else:
        return play_game(200, 5)


def update_scoreboard(name, tries, result, filename="scoreboard.txt"):
    with open(filename, 'a') as file:
        file.write(f"{name},{tries},{result}\n")


def display_scoreboard(filename="scoreboard.txt", top_n=5):
    scores = []

    try:
        with open(filename, "r") as file:
            for line in file:
                name, tries, result = line.strip().split(',')
                if result == "won":
                    scores.append((name, int(tries)))
    except FileNotFoundError:
        print("No scores yet!")
        return

    if not scores:
        print("No winning scores yet!")
        return

    scores.sort(key=lambda x: x[1])  # sort by attempts

    print("\n🏆 --- Leaderboard ---")
    for i, (name, tries) in enumerate(scores[:top_n], start=1):
        print(f"{i}. {name} - {tries} attempts")
    print("----------------------\n")


print(start_game())
