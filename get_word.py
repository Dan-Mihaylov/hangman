import random
from words import easy_words, medium_words, hard_words


class GetWord:

    def __init__(self, easy_w: list, medium_w: list, hard_w: list, difficulty: str):
        self.easy_w = easy_w
        self.medium_w = medium_w
        self.hard_w = hard_w
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


some = GetWord(easy_words, medium_words, hard_words, "hard")
print(some.choose_word())
