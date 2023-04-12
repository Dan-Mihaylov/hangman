from tkinter import *
from create_image import CreateImage
from get_word import GetWord


root = Tk()
root.title("Hangman")
root.geometry("800x800+600+150")
root.resizable(False, False)

current_user = str()
difficulty = str()
graphics = list()
current_word = list()
hidden_word = list()
graphic_label = Label   # this will be to update graphic images
word = LabelFrame    # this one is a label for the hidden word
letter = Entry()
choices_frame = LabelFrame
current_index = 0    # shows you the image you have to display and the mistakes you can make.

# Creating the game frame, where all will be stored

game_frame = LabelFrame(root, height=800, width=800)
options_frame = LabelFrame(game_frame)


# create a list of images for the various stages of the game. 0 is starting image, 7 is the game over image.
def create_graphics():
    for i in range(9):
        path = f"images/{i}.png"
        img = CreateImage(path)
        graphics.append(img.create_img())


create_graphics()


# Creating the first page of the game
def main_menu():
    global game_frame, main_menu_image, menu_image, options_frame

    # creating a function here to get the username of the player and display the second options window,
    # where difficulty will be chosen.
    def get_name():
        global current_user, options_frame
        if not current_user:
            username = user_entry.get()
            current_user = username

        options_frame.destroy()

        options_frame = LabelFrame(game_frame)
        options_frame.pack(pady=20)
        name = Label(options_frame, text=current_user, font="Helvetica, 24 bold")
        name.grid(row=0, column=0, padx=10)

        options = Label(options_frame, text="Select Difficulty:", font="Helvetica, 24")
        options.grid(row=1, column=0, pady=10)

        easy_btn = Button(options_frame, text="Easy Words", font="Helvetica, 20", width=30,
                          command=lambda: start_game("easy"))
        easy_btn.grid(row=2, column=0)

        medium_btn = Button(options_frame, text="Medium Words", font="Helvetica, 20", width=30,
                            command=lambda: start_game("medium"))
        medium_btn.grid(row=3, column=0)

        difficult_btn = Button(options_frame, text="Hard Words", font="Helvetica, 20", width=30,
                               command=lambda: start_game("hard"))
        difficult_btn.grid(row=4, column=0)

    game_frame.destroy()
    game_frame = LabelFrame(root, height=800, width=800, background="grey")
    game_frame.pack(fill=BOTH, expand=True)

    game_name = Label(game_frame, text="--HANGMAN--", font="Helvetica, 20")
    game_name.pack(pady=10)

    main_menu_image = CreateImage("images/hangman_main.png")
    menu_image = main_menu_image.create_img()
    img_label = Label(game_frame, image=menu_image)
    img_label.pack(anchor="center")

    options_frame = LabelFrame(game_frame)
    user_label = Label(options_frame, text="Enter Username:", font="Helvetica, 16")
    user_label.grid(row=0, column=0, padx=10)
    user_entry = Entry(options_frame, font="Helvetica, 16")
    user_entry.grid(row=0, column=1, padx=10)
    get_user_btn = Button(options_frame, text="Enter", font="Helvetica, 16", command=get_name)
    get_user_btn.grid(row=0, column=2, padx=10)
    options_frame.pack(pady=20)


def start_game(diff: str):
    global game_frame, current_word, hidden_word, letter, word, graphic_label, choices_frame, current_index

    current_index = 0

    # destroy the game frame and re-create it
    game_frame.destroy()
    game_frame = LabelFrame(root, height=800, width=800, background="grey")
    game_frame.pack(fill=BOTH, expand=True)

    # Generating the word that we have to guess and adding each letter to a list individually.
    generate_word = GetWord(diff)
    current_word = [*generate_word.choose_word().upper()]

    # Displaying the first image
    graphic_label = Label(game_frame, image=graphics[current_index])
    graphic_label.pack()

    user = Label(game_frame, text=current_user, font="Helvetica, 26 bold")
    user.pack(pady=10)

    hidden_word = ["_"] * len(current_word)
    word = Label(game_frame, text="  ".join(hidden_word), font="Helvetica, 30")
    word.pack(pady=10)

    choices_frame = LabelFrame(game_frame)
    choices_frame.pack()

    instructions = Label(choices_frame, text="Enter A Letter: ", font="Helvetica, 20")
    instructions.grid(row=0, column=0, padx=10)

    letter = Entry(choices_frame, font="Helvetica, 20", width=2)
    letter.grid(row=0, column=1, padx=10)

    submit = Button(choices_frame, text="Submit Leter", font="Helvetica, 16", command=try_letter)
    submit.grid(row=0, column=2, padx=10)


def try_letter():
    global letter, hidden_word, word, game_frame, current_index, graphic_label, choices_frame
    char = letter.get().upper()
    letter.delete(0, END)
    print(current_word)

    # check if letter in current word and if it is, iterate over the word to find on which index it is and then
    # re-configure the hidden word to display the letter, and if it isn't add a strike to the player
    # and change photo to the next one.

    if char in current_word:
        for index, cur_letter in enumerate(current_word):
            if cur_letter == char:
                hidden_word[index] = cur_letter
        word.configure(text="  ".join(hidden_word), font="Helvetica, 30")
        if "_" not in hidden_word:
            winner_text = Label(game_frame, text=f"Congratulations {current_user}!\n You Win!", font="Helvetica, 26")
            winner_text.pack()
            choices_frame.destroy()
            graphic_label.configure(image=graphics[8])
            new_game_btn = Button(game_frame, text="New Game", font="Helvetica, 20", width=10, command=main_menu)
            new_game_btn.pack(pady=50)
    else:
        current_index += 1
        graphic_label.configure(image=graphics[current_index])
        # need to check if it is last index and if yes, ask if you want new game





main_menu()
root.mainloop()
