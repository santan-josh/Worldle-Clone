import random
def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words 

def is_valid_guess(guess, guesses):
    return guess in guesses

def evaluate_guess(guess, word):
    result = ""

    for i in range(5):
        if guess[i] == word[i]:
            result += "\033[32m" + guess[i]
        else:
            if guess [i] in word:
                result += "\033[33m" + guess[i]
            else:
                result += "\033[0m" + guess[i]

    return result + "\033[0m"

def wordle(guesses,answers):
    print("welcome to WORDLE! ")
    secret_word = random.choice(answers).lower()


    attempts = 1
    max_attempts = 6


    while attempts <= max_attempts:
        guess = input("ENTER GUESS" + str(attempts) + ": ").lower()
        if not is_valid_guess(guess,guesses):
            print("INVALID")
            continue
        if guess == secret_word:
            print("CONGRATULATIONS! YOURE SMARTER THAN YOU LOOK ", secret_word)
            break
        attempts += 1
        feedback = evaluate_guess(guess, secret_word)
        print(feedback)

    if attempts > max_attempts:
        print("GAME OVER, THE SECRET WORD WAS", secret_word)


guesses = load_dictionary("guesses.txt")
answers = load_dictionary("answers.txt")

wordle(guesses, answers)


print("THANK YOU FOR PLAYING")