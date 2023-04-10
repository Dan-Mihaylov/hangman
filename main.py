from tkinter import *
from create_image import CreateImage
from get_word import GetWord, easy_words, medium_words, hard_words


root = Tk()
root.title("Hangman")
root.geometry("800x800+600+150")

current_user = str()
difficulty = str()

# Creating the game frame, where all will be stored

game_frame = LabelFrame(root, height=800, width=800)
options_frame = LabelFrame(game_frame)


# Creating the first page of the game

def main_menu():
    global game_frame, main_menu_image, menu_image, options_frame

    # creating a function here to get the username of the player and display the second options window,
    # where difficulty will be chosen.

    def get_name():
        global current_user, options_frame

        username = user_entry.get()
        current_user = username

        options_frame.destroy()

        options_frame = LabelFrame(game_frame)
        options_frame.pack(pady=20)
        name = Label(options_frame, text=current_user, font="Helvetica, 24 bold")
        name.grid(row=0, column=0, padx=10, pady=10)

        options = Label(options_frame, text="Select Difficulty:", font="Helvetica, 24")
        options.grid(row=1, column=0)

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
    global game_frame

    # destroy the game frame and re-create it
    game_frame.destroy()
    game_frame = LabelFrame(root, height=800, width=800, background="grey")
    game_frame.pack(fill=BOTH, expand=True)

    # Generating the word that we have to guess and adding each letter to a list individually.
    generate_word = GetWord(diff)
    current_word = [*generate_word.choose_word()]
    print(current_word)


main_menu()
root.mainloop()
