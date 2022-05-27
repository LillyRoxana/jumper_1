class Puzzle:

    def __init__(self):
        
        self._attempt = 0
        self._guessing = ""


    def get_letter(self, prompt):
        
        return input(prompt)

    def show_letter(self):
        
        print(self._guessing)

    def get_attempt(self):

        if self._attempt == 0:
            self.puzzle()

        elif self._attempt == 1:
            self.puzzle_attempt_one()

        elif self._attempt == 2:
            self.puzzle_attempt_two()

        elif self._attempt == 3:
            self.puzzle_attempt_tree()

        elif self._attempt == 4:
            self.puzzle_attempt_four()

    def puzzle(self):

        print()
        print("      ___      ")
        print("     /___\     ")
        print("     \   /     ")
        print("      \ /      ")
        print("       0       ")
        print("      /|\      ")
        print("      / \      ")
        print()
        print("    ^^^^^^^^^  ")

    def puzzle_attempt_one(self):

        print()
        print("               ")
        print("     /___\     ")
        print("     \   /     ")
        print("      \ /      ")
        print("       0       ")
        print("      /|\      ")
        print("      / \      ")
        print()
        print("    ^^^^^^^^^  ")

    def puzzle_attempt_two(self):

        print()
        print("               ")
        print("               ")
        print("     \   /     ")
        print("      \ /      ")
        print("       0       ")
        print("      /|\      ")
        print("      / \      ")
        print()
        print("    ^^^^^^^^^  ")

    def puzzle_attempt_tree(self):

        print()
        print("               ")
        print("               ")
        print("               ")
        print("      \ /      ")
        print("       0       ")
        print("      /|\      ")
        print("      / \      ")
        print()
        print("    ^^^^^^^^^  ")

    def puzzle_attempt_four(self):

        print()
        print("               ")
        print("               ")
        print("               ")
        print("               ")
        print("       X       ")
        print("      /|\      ")
        print("      / \      ")
        print()
        print("    ^^^^^^^^^  ")
        print("Oh no! Game over")
   
