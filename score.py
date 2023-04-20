import re
from tkinter import *
from tkinter import messagebox


text = str()
user = str()
bg_color = "#1f7a63"
fg_color = "#cccccc"
abg_color = "#258e74"
afg_color = "white"


def open_window():
    new_window = Toplevel()
    new_window.overrideredirect(True)
    new_window.geometry("400x200+800+400")
    new_window.configure(background=bg_color)

    name_label = Label(new_window, text=user, font="Helvetica, 30", bg=bg_color, fg=fg_color)
    name_label.pack(pady=10)
    new_label = Label(new_window, text=text, font="Helvetica, 20", bg=bg_color, fg=fg_color)
    new_label.pack(pady=10)
    close_btn = Button(new_window, text="Close Window", font="Helvatica, 16", width=15, command=new_window.destroy,
                       bg=bg_color, fg=fg_color, activebackground=abg_color, activeforeground=afg_color)
    close_btn.pack(pady=10)


def add_score(username: str, score: int):
    # Check if user not already in the text file

    users = open(f"temp/users.txt", "r")
    if username not in users.read():
        users.close()
        users = open(f"temp/users.txt", "a")
        users.write(f"{username}\n")

    won = "win"
    if score < 0:
        won = "lose"

    current = open(f"temp/{username}.txt", "a")
    current.write(f"points:{score},{won}\n")
    current.close()


# Returns a string, so can be added to label and displayed in the game.
def check_score(username: str):
    global text, user

    pattern = r"points:(?P<pts>-*[0-9]+),(?P<res>[a-z]+)"
    try:
        current = open(f"temp/{username}.txt", "r")
        total_score = 0
        for line in current.readlines():
            matches = re.finditer(pattern, line)
            for match in matches:
                total_score += int(match["pts"])
        if total_score < 0:
            current.close()
            current = open(f"temp/{username}.txt", "w")
            current.write("")
            current.close()
            text = "Your Score Has Been Reset To 0"
        else:
            user = username
            text = f"Your Total Points Are --{total_score}--"
            open_window()
        print(total_score)
        return total_score
    except FileNotFoundError:
        messagebox.showerror("Score", f"{username} Hasn't Got Score Yet")


# Returns the points to be added to the text file with the current username
def get_points(len_hidden_word: int, missing_letter: int):
    if missing_letter > 0:
        return missing_letter * -20
    else:
        return len_hidden_word * 10

