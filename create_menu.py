from tkinter import *
from score import *


class DisplayMenu:

    def __init__(self, root: Tk):
        self.my_menu = Menu
        self.root = root
        self.file_menu = Menu

    def display_menu(self):
        # Creating drop_down menu items
        self.my_menu = Menu(self.root)
        self.root.configure(menu=self.my_menu)
        self.file_menu = Menu(self.my_menu)
        self.my_menu.add_cascade(label="Game", menu=self.file_menu)
        self.my_menu.add_command(label="Exit", command=self.root.destroy)

    def update_user(self, current_user):
        self.file_menu.add_command(label="Get User Score", command=lambda: check_score(current_user))


