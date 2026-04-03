class Hangman:
    def load_words(self):
        return ["I", "am", "Batman"]

    def blank_the_word(self, word: str) -> str:
        word_split = "".join(["_" for _ in word])
        return word_split

    def blank_all_words(self, words: list) -> list:
        return [self.blank_the_word(word) for word in words]

    def validate_user_guess(self, user_input: str) -> bool:
        return len(user_input) <= 0 or user_input is None or len(user_input) > 1

    def check_user_guess_against_word(
        self, user_guessed_letter: str, word: str
    ) -> bool:
        return (
            self.validate_user_guess(user_guessed_letter)
            and user_guessed_letter in word
        )

    def find_matched_letters(self, user_guessed_letter: str, word: str) -> list:
        return [
            index for index, letter in enumerate(word) if letter == user_guessed_letter
        ]

    def reveal_letter_in_word(
        self, user_guessed_letter: str, word: str, matched_indexes: list
    ) -> str:
        word_split = list(word)
        for index in matched_indexes:
            word_split[index] = user_guessed_letter
        return "".join(word_split)

    def ask_user_for_a_guess(self, words: list) -> str:
        user_guess = input("I am thinking of a sentence. Can you guess a letter? ")
        try:
            new_words = []
            for word in words:
                if self.check_user_guess_against_word(user_guess, word):
                    new_words.append(
                        self.reveal_letter_in_word(
                            user_guess,
                            word,
                            self.find_matched_letters(user_guess, word),
                        )
                    )
                else:
                    raise ValueError()
            return "".join(new_words)
        except ValueError:
            print("Try again. I just need 1 letter from you.")
            return self.ask_user_for_a_guess(words)

    def check_for_new_guesses(self, blanked_words: list):
        return "_" in blanked_words


if __name__ == "__main__":
    game = Hangman()
    print(game.blank_all_words(game.load_words()))
