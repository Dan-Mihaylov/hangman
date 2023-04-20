from tkinter import *

from create_image import CreateImage
from get_word import GetWord
from score import *
from create_menu import *


root = Tk()
root.title("Hangman")
root.geometry("800x800+600+150")
root.resizable(False, False)
root.iconbitmap("images/logo.ico")

current_user = str()
difficulty = str()
graphics = list()
current_word = list()
hidden_word = list()
graphic_label = Label()   # this will be to update graphic images
word = LabelFrame    # this one is a label for the hidden word _ _ _ _ _ _
letter = Entry()
choices_frame = LabelFrame()
current_index = 0    # shows you the image you have to display and the mistakes you can make.
bg_color = "#1f7a63"
fg_color = "#cccccc"
abg_color = "#258e74"
afg_color = "white"
change_user = False


# Creating the game frame, where all will be stored
game_frame = LabelFrame(root, height=800, width=800, bg=bg_color)
options_frame = LabelFrame(game_frame, bg=bg_color)

# will store used letters here
used_letters = list()
used_letters_label = Label(game_frame, bg=bg_color)


# to reset user
def reset_user():
    global current_user
    current_user = str()


# create a list of images for the various stages of the game. 0 is starting image, 7 is the game over image.
def create_graphics():
    for i in range(9):
        path = f"images/{i}.png"
        img = CreateImage(path)
        graphics.append(img.create_img())


create_graphics()


# Creating the first page of the game
def main_menu():
    global game_frame, main_menu_image, menu_image, options_frame, difficulty, change_user, current_user

    # creating a function here to get the username of the player and display the second options window,
    # where difficulty will be chosen.
    def get_name():
        global current_user, options_frame, game_menu
        if not current_user:
            username = user_entry.get()
            current_user = username
            game_menu.update_user(current_user)

        options_frame.destroy()

        options_frame = LabelFrame(game_frame, bg=bg_color)
        options_frame.pack(pady=20)
        name = Label(options_frame, text=current_user, font="Helvetica, 24 bold", bg=bg_color, fg=fg_color)
        name.grid(row=0, column=0, padx=10)

        options = Label(options_frame, text="Select Difficulty:", font="Helvetica, 24", bg=bg_color, fg=fg_color)
        options.grid(row=1, column=0, pady=10)

        easy_btn = Button(options_frame, text="Easy Words", font="Helvetica, 20", width=30,
                          command=lambda: start_game("easy"), bg=bg_color, fg=fg_color, activebackground=abg_color,
                          activeforeground=afg_color)
        easy_btn.grid(row=2, column=0)

        medium_btn = Button(options_frame, text="Medium Words", font="Helvetica, 20", width=30,
                            command=lambda: start_game("medium"), bg=bg_color, fg=fg_color, activebackground=abg_color,
                            activeforeground=afg_color)
        medium_btn.grid(row=3, column=0)

        difficult_btn = Button(options_frame, text="Hard Words", font="Helvetica, 20", width=30,
                               command=lambda: start_game("hard"), bg=bg_color, fg=fg_color, activebackground=abg_color,
                               activeforeground=afg_color)
        difficult_btn.grid(row=4, column=0)

    # if change_user:
    #     current_user = ""
    #     change_user = False

    game_frame.destroy()
    game_frame = LabelFrame(root, height=800, width=800, bg=bg_color)
    game_frame.pack(fill=BOTH, expand=True)

    game_name = Label(game_frame, text="--HANGMAN--", font="Helvetica, 20", bg=bg_color, fg=fg_color)
    game_name.pack(pady=10)

    main_menu_image = CreateImage("images/hangman_main.png")
    menu_image = main_menu_image.create_img()
    img_label = Label(game_frame, image=menu_image)
    img_label.pack(anchor="center")

    options_frame = LabelFrame(game_frame, bg=bg_color)

    # If there is a user already, we go straight to the menu that chooses difficulty of word, otherwise we create
    # the entry box to get the username.
    if current_user:
        get_name()
    else:
        user_label = Label(options_frame, text="Enter Username:", font="Helvetica, 16", bg=bg_color, fg=fg_color)
        user_label.grid(row=0, column=0, padx=10)
        user_entry = Entry(options_frame, font="Helvetica, 16", bg=abg_color, fg=fg_color, justify="center")
        user_entry.grid(row=0, column=1, padx=10)
        get_user_btn = Button(options_frame, text="Enter", font="Helvetica, 16", command=get_name, bg=bg_color,
                              fg=fg_color, activebackground=abg_color,activeforeground=afg_color)
        get_user_btn.grid(row=0, column=2, padx=10)
        options_frame.pack(pady=20)


game_menu = DisplayMenu(root, main_menu, reset_user)
game_menu.display_menu()


def start_game(diff: str):
    global game_frame, current_word, hidden_word, letter, word, graphic_label, choices_frame, current_index, difficulty
    global used_letters_label

    difficulty = diff
    current_index = 0

    # destroy the game frame and re-create it
    game_frame.destroy()
    game_frame = LabelFrame(root, height=800, width=800, bg=bg_color)
    game_frame.pack(fill=BOTH, expand=True)

    # Generating the word that we have to guess and adding each letter to a list individually.
    generate_word = GetWord(diff)
    current_word = [*generate_word.choose_word().upper()]

    # Displaying the first image
    graphic_label = Label(game_frame, image=graphics[current_index], bg=bg_color)
    graphic_label.pack()

    user = Label(game_frame, text=current_user, font="Helvetica, 26 bold", bg=bg_color, fg=fg_color)
    user.pack(pady=10)

    hidden_word = ["_"] * len(current_word)
    word = Label(game_frame, text="  ".join(hidden_word), font="Helvetica, 30", bg=bg_color, fg=fg_color)
    word.pack(pady=10)
    # a frame to add the choices in with a grid system.
    choices_frame = LabelFrame(game_frame, bg=bg_color, fg=fg_color)
    choices_frame.pack()

    instructions = Label(choices_frame, text="Enter A Letter: ", font="Helvetica, 20", bg=bg_color, fg=fg_color)
    instructions.grid(row=0, column=0, padx=10)

    letter = Entry(choices_frame, font="Helvetica, 20", width=2, bg=abg_color, fg=fg_color)
    letter.grid(row=0, column=1, padx=10)

    submit = Button(choices_frame, text="Submit Leter", font="Helvetica, 16", command=try_letter, bg=bg_color,
                    fg=fg_color, activebackground=abg_color,activeforeground=afg_color)
    submit.grid(row=0, column=2, padx=10)

    used_letters_label = Label(game_frame, bg=bg_color, fg=fg_color)
    used_letters_label.pack()


def try_letter():
    global letter, hidden_word, word, game_frame, current_index, graphic_label, choices_frame, difficulty, used_letters
    global used_letters_label
    char = letter.get().upper()
    letter.delete(0, END)
    # print(current_word)
    used_letters.append(char)
    used_letters_label.configure(text=f"Used Letters: {', '.join(used_letters)}", font="Helvetica, 16", bg=bg_color,
                                 fg=fg_color)
    used_letters_label.pack(pady=10)

    # check if letter in current word and if it is, iterate over the word to find on which index it is and then
    # re-configure the hidden word to display the letter, and if it isn't add a strike to the player
    # and change photo to the next one.

    def generate_buttons():
        # generate the buttons for new game or new word
        new_game_btn = Button(game_frame, text="Choose Difficulty", font="Helvetica, 16", width=16,
                              command=main_menu, bg=bg_color, fg=fg_color, activebackground=abg_color,
                              activeforeground=afg_color)
        new_game_btn.pack(pady=10)
        next_word_btn = Button(game_frame, text="Next Word", font="Helvetica, 16", width=16,
                               command=lambda: start_game(difficulty), bg=bg_color, fg=fg_color,
                               activebackground=abg_color,activeforeground=afg_color)
        next_word_btn.pack(pady=10)

    if char in current_word:
        for index, cur_letter in enumerate(current_word):
            if cur_letter == char:
                hidden_word[index] = cur_letter
        word.configure(text="  ".join(hidden_word), font="Helvetica, 30", bg=bg_color, fg=fg_color)
        if "_" not in hidden_word:
            used_letters.clear()
            winner_text = Label(game_frame, text=f"Congratulations {current_user}!\n You Win!", font="Helvetica, 26",
                                bg=bg_color, fg=fg_color)
            winner_text.pack()
            choices_frame.destroy()
            graphic_label.configure(image=graphics[8])
            # calculating the points won and adding them to the curr user text file
            points = get_points(len(hidden_word), 0)
            add_score(current_user, points)
            generate_buttons()
    else:
        current_index += 1
        graphic_label.configure(image=graphics[current_index])
        if current_index >= 7:
            loser_text = Label(game_frame, text=f"{current_user}, You Have Lost!", font="Helvetica, 26", bg=bg_color,
                               fg=fg_color)
            loser_text.pack()
            choices_frame.destroy()
            # calculating the points lost and adding them to curr user text file
            points = get_points(len(hidden_word), hidden_word.count("_"))
            add_score(current_user, points)
            generate_buttons()
            for index, letter in enumerate(current_word):
                hidden_word[index] = letter
                word.configure(text=" ".join(hidden_word), font="Helvetica, 26", foreground="red", bg=bg_color)
            used_letters.clear()


main_menu()
root.mainloop()
