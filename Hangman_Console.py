import random

# =========================
# WORD DATASET
# =========================
word_categories = {

    "Programming": [
        "python", "variable", "function", "compiler",
        "algorithm", "database", "debugging", "syntax"
    ],

    "Technology": [
        "keyboard", "monitor", "internet", "software",
        "hardware", "processor", "network", "cybersecurity"
    ],

    "Animals": [
        "elephant", "giraffe", "kangaroo", "penguin",
        "dolphin", "alligator", "chimpanzee", "tiger"
    ],

    "Countries": [
        "india", "canada", "germany", "japan",
        "brazil", "france", "australia", "singapore"
    ],

    "Space": [
        "planet", "galaxy", "nebula", "asteroid",
        "gravity", "astronaut", "satellite", "comet"
    ]
}

# =========================
# HANGMAN STAGES
# =========================
hangman_stages = [

    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,

    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# =========================
# SELECT CATEGORY
# =========================
print("🎮 WELCOME TO HANGMAN 🎮\n")

print("Choose a Category:\n")

categories = list(word_categories.keys())

for i, category in enumerate(categories, start=1):
    print(f"{i}. {category}")

# User selects category
choice = int(input("\nEnter category number: "))

selected_category = categories[choice - 1]

# =========================
# SELECT RANDOM WORD
# =========================
secret_word = random.choice(
    word_categories[selected_category]
).upper()

display_word = ["_"] * len(secret_word)

guessed_letters = []

attempts_left = 6
score = 0

# =========================
# GAME START
# =========================
print(f"\n📂 Category: {selected_category}")

# =========================
# GAME LOOP
# =========================
while attempts_left > 0 and "_" in display_word:

    print(hangman_stages[6 - attempts_left])

    print("Word:", " ".join(display_word))
    print("Attempts Left:", attempts_left)
    print("Score:", score)
    print("Guessed Letters:", ", ".join(guessed_letters))

    guess = input("\nGuess a letter: ").upper()

    # =========================
    # INPUT VALIDATION
    # =========================
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Enter only ONE alphabet letter.\n")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # =========================
    # CORRECT GUESS
    # =========================
    if guess in secret_word:

        print("✅ Correct Guess!\n")

        for index, letter in enumerate(secret_word):

            if letter == guess:
                display_word[index] = guess
                score += 10

    # =========================
    # WRONG GUESS
    # =========================
    else:

        print("❌ Wrong Guess!\n")

        attempts_left -= 1

# =========================
# FINAL RESULT
# =========================
if "_" not in display_word:

    print(hangman_stages[6 - attempts_left])

    print("\n🎉 YOU WIN!")
    print("Word:", secret_word)
    print("Final Score:", score)

else:

    print(hangman_stages[6])

    print("\n💀 GAME OVER!")
    print("The word was:", secret_word)