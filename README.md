# Hangman
The classic game hangman with Tkinter

### Things I learned doing this project:
- Working with Tkinter library
- Working with the Random module
- Storing the words we are guesing in an encrypted way, so you can't read them in a raw format
- Working with Pillow, creating and displaying images
- File handling, to store the users and their scores (Would consider using SQLite in further improvements)
- Creating Classes and Objects
- Creating cutom modules with classes, methods or just functions and importing them to the main file to access them whenever needed
- Structoring the code in a way that is fairly easy to read

### Main Page

On the Main Page you have an entry box to enter your username.
When you enter your username, It checks if it is an existing one in the users.txt and if it is not, it adds it on there, and create another .txt file with your username as its name to store the users scores later on.

![Mainpage](https://github.com/Dan-Mihaylov/hangman/assets/123562461/793a6618-af8a-4ff1-8b1c-b2842d6044fc)


### Difficulty Page

On this page you are givven the option to chose your words difficulty


![difficulty page](https://github.com/Dan-Mihaylov/hangman/assets/123562461/e8b068b4-bf4c-4c4d-858b-c8c5a982243a)

### The Game Page

On the game page you have the graphics of the place you hang the man. With each wrong guess, there is an element of the mans body added to the graphic. You have your Username displayed, followed by _ underscores in the length of the guessing word. An entry box where you can type a single letter you would like to submit as an answer, a submit button and finally an used letters section, where you can see all the letters you have used. Every correct letter you guess, will appear in its rightful place, instead of the _ . 



![game page](https://github.com/Dan-Mihaylov/hangman/assets/123562461/14375185-1e15-4c6a-ab90-a89c38793ccc)


### Winner Page

You get this page when you guess the entire word correctly. Again you have some winners graphics, the Username, the uncovered word, the used letters, and a congratulating message that also tells you how many points, you have won. They have been added to your username's .txt file in a particular order. You then have the option to change the words difficulty or get the next word.


![winner page](https://github.com/Dan-Mihaylov/hangman/assets/123562461/c3a17e77-ecf3-4a67-9038-1fe6a085780c)


### Menubar

You have a menubar on top, that gives you the option to check the current users score. If there is no current user, that button is unavailable. When you click the button, there is a new toplevel window popping up with the infornation about the username and the total score. There is also the option to change the user in the menubar, which takes you to the very first page and the option to exit the game.



![get score](https://github.com/Dan-Mihaylov/hangman/assets/123562461/5705c8d2-857b-4d05-b59e-4a971f804468)



### Game Over Page

The final page, if you lose the game is the game over page. There you also have the graphics of the final game, some info about the username, the hidden word gets uncovered, your points get calculated and deducted from the total points you have, you get a losing message and finaly have the option to either 
change the difficulty again or get the next word.


![lose](https://github.com/Dan-Mihaylov/hangman/assets/123562461/2c40bed8-0c18-4692-a5ec-5c430b7ec1cf)

