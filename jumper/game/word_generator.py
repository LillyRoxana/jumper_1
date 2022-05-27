import random
import os
from game import ROOT_DIR,DATA_DIR
 
class word_list:
        
    def __init__(self):

        # open the word_list.txt and pick a random word
        self._word_list = open(os.path.join(DATA_DIR,'word_list.txt'),'r')
        self._word_list = self._word_list.readlines()
        self._random_word = random.choice(self._word_list)

        words = {
                1: 'wares',
                2: 'soup',
                3: 'mount',
                4: 'extend',
                5: 'brown'
                
            }
        option = random.randint(1, 5)
        self._word = words[option].lower()

    def lets_to_compare_letters(self, _guesser):

        guessing = ""

        for letter in self._word:
            if letter in _guesser._letters:
                guessing += letter
            else:
                guessing += "_"

        return guessing

    def is_found(self, guessed_letters):

        for letter in self._word:
            if letter in guessed_letters:
                pass
            else:
                return True

        return False

    def lets_to_count_attempts(self, _guesser):

        attempt = 0

        for guessed_letter in _guesser._letters:
            if guessed_letter in self._word:
                pass
            else:
                attempt += 1

        return attempt
