## Q5
# Create a class called Upper which has two methods called get_word and print_word.
    # the get_word method should accept a string from the user
    # the print_word method prints the string in upper case.

class Upper:
    pass

    def get_word(self):
        self.word = input("What is your word? ")
        self.print_word() # pass the input from itself to METHOD called print_word (below)

    def print_word(self):
        print(self.word.upper()) # print whatever is passed from get_word in Uppercase

Upper().get_word()