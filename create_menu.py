from tkinter import *
from score import *


class DisplayMenu:

    def __init__(self, root: Tk, to_main, reset_user):
        self.my_menu = Menu
        self.root = root
        self.file_menu = Menu
        self.to_main = to_main
        self.reset_user = reset_user

    def display_menu(self):
        # Creating drop_down menu items
        self.my_menu = Menu(self.root)
        self.root.configure(menu=self.my_menu)
        self.file_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label="Game", menu=self.file_menu)
        self.my_menu.add_cascade(label="Change User", command=self.change_user)
        self.my_menu.add_command(label="Exit", command=self.root.destroy)

    def update_user(self, current_user):
        self.display_menu()
        self.file_menu.add_command(label="Get User Score", command=lambda: check_score(current_user))

    def change_user(self):
        self.reset_user()
        self.to_main()



