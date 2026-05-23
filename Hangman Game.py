import random
import tkinter as tk
from tkinter import messagebox

# =========================
# WORD DATASET
# =========================
word_categories = {

    "Programming": [
        "python", "variable", "function", "compiler",
        "algorithm", "database", "debugging", "syntax",
        "inheritance", "recursion", "object", "class",
        "loop", "array", "string", "boolean", "exception", 
        "library", "framework", "api", "version", "control",
        "github", "terminal", "command", "line", "interface", "software",
    ],

    "Technology": [
        "keyboard", "monitor", "internet", "software",
        "hardware", "processor", "network", "cybersecurity",
        "artificial", "intelligence", "machine", "learning",
        "virtual", "reality", "augmented", "blockchain",
        "cloud", "computing", "data", "encryption", "algorithm",
    ],

    "Animals": [
        "elephant", "giraffe", "kangaroo", "penguin",
        "dolphin", "alligator", "chimpanzee", "tiger",
        "lion", "zebra", "rhinoceros", "hippopotamus",
        "crocodile", "flamingo", "ostrich", "koala",
        "panda", "sloth", "armadillo", "porcupine",
    ],

    "Countries": [
        "india", "canada", "germany", "japan",
        "brazil", "france", "australia", "singapore",
        "italy", "spain", "mexico", "netherlands",
        "sweden", "norway", "denmark", "finland",
        "switzerland", "austria", "belgium", "portugal",

    ],

    "Space": [
        "planet", "galaxy", "nebula", "asteroid",
        "gravity", "astronaut", "satellite", "comet",
        "blackhole", "supernova", "cosmos", "universe",
        "meteor", "orbit", "telescope", "spacecraft",
            "rocket", "lunar", "solar", "eclipse",

    ]
}

# =========================
# HANGMAN ASCII ART
# =========================
hangman_art = [

  """
    😀
    
    
    ❤️ ❤️ ❤️ ❤️ ❤️ ❤️
    """,

    """
      😐
      |
    
    ❤️ ❤️ ❤️ ❤️ ❤️
    """,

    """
      😟
     \\|
    
    ❤️ ❤️ ❤️ ❤️
    """,

    """
      😨
     \\|/
    
    ❤️ ❤️ ❤️
    """,

    """
      😰
     \\|/
      |
    
    ❤️ ❤️
    """,

    """
      😵
     \\|/
      |
     /
    
    ❤️
    """,

    """
      💀
     \\|/
      |
     / \\
    
    GAME OVER
    """
]

# =========================
# TKINTER WINDOW
# =========================
root = tk.Tk()
root.title("🎮 Hangman Game")
root.geometry("750x900")
root.config(bg="#031127")

# =========================
# GAME VARIABLES
# =========================
secret_word = ""
display_word = []
guessed_letters = []
attempts_left = 6
score = 0

# =========================
# START GAME FUNCTION
# =========================
def start_game():

    global secret_word
    global display_word
    global guessed_letters
    global attempts_left
    global score

    selected_category = category_var.get()

    if selected_category == "Select Category":
        messagebox.showwarning(
            "Category Missing",
            "Please select a category first!"
        )
        return

    # Reset variables
    guessed_letters = []
    attempts_left = 6
    score = 0

    # Choose word
    secret_word = random.choice(
        word_categories[selected_category]
    ).upper()

    display_word = ["_"] * len(secret_word)

    # Enable input again
    guess_button.config(state="normal")
    entry.config(state="normal")

    # Update UI
    category_label.config(
        text=f"Category: {selected_category}"
    )

    word_label.config(
        text=" ".join(display_word)
    )

    guessed_label.config(
        text="Guessed Letters: "
    )

    attempts_label.config(
        text=f"Attempts Left: {attempts_left}"
    )

    score_label.config(
        text=f"Score: {score}"
    )

    art_label.config(
        text=hangman_art[0]
    )

# =========================
# GUESS LETTER FUNCTION
# =========================
def guess_letter():

    global attempts_left
    global score

    # Check if game started
    if secret_word == "":
        messagebox.showwarning(
            "Start Game",
            "Please select a category and start the game!"
        )
        return

    guess = entry.get().upper()
    entry.delete(0, tk.END)

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning(
            "Invalid Input",
            "Enter only ONE alphabet letter!"
        )
        return

    # Already guessed
    if guess in guessed_letters:
        messagebox.showinfo(
            "Already Guessed",
            "You already guessed that letter!"
        )
        return

    guessed_letters.append(guess)

    # =========================
    # CORRECT GUESS
    # =========================
    if guess in secret_word:

        for i, letter in enumerate(secret_word):

            if letter == guess:
                display_word[i] = guess
                score += 10

        word_label.config(
            text=" ".join(display_word)
        )

        score_label.config(
            text=f"Score: {score}"
        )

        # WIN CONDITION
        if "_" not in display_word:

            messagebox.showinfo(
                "YOU WIN 🎉",
                f"Congratulations!\n\n"
                f"Word: {secret_word}\n"
                f"Final Score: {score}"
            )

            # Disable after win
            guess_button.config(state="disabled")
            entry.config(state="disabled")

    # =========================
    # WRONG GUESS
    # =========================
    else:

        attempts_left -= 1

        attempts_label.config(
            text=f"Attempts Left: {attempts_left}"
        )

        art_label.config(
            text=hangman_art[6 - attempts_left]
        )

        # LOSE CONDITION
        if attempts_left == 0:

            art_label.config(
                text=hangman_art[6]
            )

            messagebox.showerror(
                "GAME OVER 💀",
                f"The word was: {secret_word}"
            )

            # Disable after losing
            guess_button.config(state="disabled")
            entry.config(state="disabled")

    # Update guessed letters
    guessed_label.config(
        text="Guessed Letters: " + ", ".join(guessed_letters)
    )

# =========================
# TITLE
# =========================
title_label = tk.Label(
    root,
    text="🎮 HANGMAN GAME",
    font=("Arial", 28, "bold"),
    bg="#031127",
    fg="#FFD369"
)

title_label.pack(pady=15)

# =========================
# CATEGORY DROPDOWN
# =========================
category_var = tk.StringVar()
category_var.set("Select Category")

dropdown = tk.OptionMenu(
    root,
    category_var,
    *word_categories.keys()
)

dropdown.config(
    font=("Arial", 13),
    bg="#00ADB5",
    fg="white",
    width=20
)

dropdown.pack(pady=10)

# =========================
# START BUTTON
# =========================
start_button = tk.Button(
    root,
    text="Start Game",
    font=("Arial", 14, "bold"),
    bg="#00FFAA",
    fg="black",
    padx=20,
    pady=10,
    command=start_game
)

start_button.pack(pady=10)

# =========================
# CATEGORY LABEL
# =========================
category_label = tk.Label(
    root,
    text="Category: ",
    font=("Arial", 16, "bold"),
    bg="#031127",
    fg="#00FFAA"
)

category_label.pack()

# =========================
# HANGMAN ART DISPLAY
# =========================
art_label = tk.Label(
    root,
    text=hangman_art[0],
    font=("Courier", 14),
    justify="left",
    bg="#031127",
    fg="white"
)

art_label.pack()

# =========================
# WORD DISPLAY
# =========================
word_label = tk.Label(
    root,
    text="",
    font=("Arial", 30, "bold"),
    bg="#031127",
    fg="#EEEEEE"
)

word_label.pack(pady=20)

# =========================
# ATTEMPTS LABEL
# =========================
attempts_label = tk.Label(
    root,
    text="Attempts Left: 6",
    font=("Arial", 14),
    bg="#031127",
    fg="#FF6B6B"
)

attempts_label.pack()

# =========================
# SCORE LABEL
# =========================
score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Arial", 14, "bold"),
    bg="#031127",
    fg="#00FFAA"
)

score_label.pack(pady=5)

# =========================
# GUESSED LETTERS
# =========================
guessed_label = tk.Label(
    root,
    text="Guessed Letters: ",
    font=("Arial", 12),
    bg="#031127",
    fg="white"
)

guessed_label.pack(pady=10)

# =========================
# INPUT FRAME
# =========================
input_frame = tk.Frame(root, bg="#031127")
input_frame.pack(pady=20)

# INPUT BOX
entry = tk.Entry(
    input_frame,
    font=("Arial", 20),
    width=5,
    justify="center"
)

entry.grid(row=0, column=0, padx=10)

# GUESS BUTTON
guess_button = tk.Button(
    input_frame,
    text="Guess",
    font=("Arial", 14, "bold"),
    bg="#00ADB5",
    fg="white",
    padx=20,
    pady=8,
    command=guess_letter
)

guess_button.grid(row=0, column=1, padx=10)

# =========================
# INSTRUCTIONS
# =========================
instructions = tk.Label(
    root,
    text="Choose a category and guess the hidden word!",
    font=("Arial", 11),
    bg="#031127",
    fg="#BBBBBB"
)

instructions.pack(pady=10)

# =========================
# RUN GAME
# =========================
root.mainloop()