import random
words = ["apple", "banana", "cherry", "kiwi"]
selected_word = random.choice(words)
scrambled_word = list(selected_word)
random.shuffle(scrambled_word)
scrambled_word = "".join(scrambled_word)
print(f"""Welcome to the word scramble game!
Try to guess the original word from the scrambled word: {scrambled_word}
You have 5 attempts to guess the word.""")
tries = 5
ans = input("Enter your guess: ")
while tries > 0:
    if ans.strip().lower() == selected_word:
        print("Congratulations! You guessed the word!")
        break
    tries -= 1
    if tries == 0:
        print(f"You're out of attempts. The correct word was: {selected_word}")
        break
    if ans != selected_word:
        print(f"Incorrect guess. Try again.You have {tries} attempts left.")
        ans = input("Enter your guess: ")
    
    