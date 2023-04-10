import random
from words import easy_words, medium_words, hard_words


class GetWord:

    def __init__(self, difficulty: str):
        self.easy_w = easy_words
        self.medium_w = medium_words
        self.hard_w = hard_words
        self.difficulty = difficulty

    def choose_word(self):
        chosen_word = str()
        if self.difficulty == "easy":
            chosen_word = random.choice(self.easy_w)
        elif self.difficulty == "medium":
            chosen_word = random.choice(self.medium_w)
        elif self.difficulty == "hard":
            chosen_word = random.choice(self.hard_w)

        decrypted_word = str()
        for letter in chosen_word:
            decrypted_word += chr(ord(letter) + 3)

        return decrypted_word
