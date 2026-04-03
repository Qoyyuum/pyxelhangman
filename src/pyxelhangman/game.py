import pyxel
from .quotes import get_quote
import textwrap

MAX_WIDTH = 26

class Game:
    def __init__(self):
        pyxel.init(170, 130, "Pyxel Hangman")
        self.reset()
        pyxel.run(self.update, self.draw)
        print(f"{self._letter_keys()=}")
    
    def reset(self):
        self.quote = get_quote().strip().upper()
        self.correct = set()
        self.wrong = set()
        self.lives = 6
        self.guess_color = 7
        self.game_over = False

    def update(self):
        self.quit_game()
        self.restart_game()
        if self.game_over:
            return
        self.handle_keys()
        
    def quit_game(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
    
    def restart_game(self):
        if pyxel.btnp(pyxel.KEY_F5):
            self.reset()

    def handle_keys(self):
        for key_code, letter in self._letter_keys():
            if pyxel.btnp(key_code):
                self.handle_guess(letter)
    
    def handle_guess(self, letter):
        if letter in self.correct or letter in self.wrong:
            return

        if letter in self.quote:
            self.correct.add(letter)
            self.game_over = self._all_letters_revealed()
        else:
            self.wrong.add(letter)
            self.lives -= 1
            self.game_over = self.lives <= 0
    
    def display_masked_quote(self, reveal_all=False):
        result = []
        for character in self.quote:
            if not character.isalpha():
                # Always show spaces, punctuations and numbers
                result.append(character)
            elif character in self.correct:
                result.append(character)
            else:
                result.append("_")
        masked_quote = "".join(result)
        if reveal_all:
            masked_quote = self.quote
        return masked_quote
    
    def masked_lines(self, reveal_all=False):
        masked = self.display_masked_quote(reveal_all=reveal_all)
        return textwrap.wrap(masked, width=MAX_WIDTH)
    
    def _all_letters_revealed(self):
        needed = {character for character in self.quote if character.isalpha()}
        return needed.issubset(self.correct)
    
    def show_game_over(self):
        if self.game_over:
            if self.lives > 0:
                pyxel.text(50,10,"YOU WIN!", 11)
            else:
                pyxel.text(50,10,"YOU LOSE!",8)
                self.guess_color = 8
    
    def draw_gallows(self):
        pyxel.line(120, 90, 140, 90, 7)
        pyxel.line(130, 90, 130, 40, 7)
        pyxel.line(130, 40, 145, 40, 7)
        pyxel.line(145, 40, 145, 45, 7)

    def draw_head(self):
        pyxel.circ(145, 50, 4, 7)
    
    def draw_body(self):
        pyxel.line(145, 54, 145, 65, 7)
        
    def draw_left_arm(self):
        pyxel.line(145, 58, 139, 61, 7)
        
    def draw_right_arm(self):
        pyxel.line(145, 58, 151, 61, 7)
        
    def draw_left_leg(self):
        pyxel.line(145, 65, 140, 72, 7)
        
    def draw_right_leg(self):
        pyxel.line(145, 65, 150, 72, 7)

    def draw_hangman(self):
        self.draw_gallows()
        hangman_shape = {
            "head" : self.draw_head,
            "body" : self.draw_body,
            "left arm" : self.draw_left_arm,
            "right arm" : self.draw_right_arm,
            "left leg" : self.draw_left_leg,
            "right leg" : self.draw_right_leg
        }

        draw_order = list(hangman_shape.keys())

        wrong = len(self.wrong)
        for body_part in range(wrong):
            hangman_shape[draw_order[body_part]]()

    
    def _letter_keys(self):
        for i in range(26):
            key_code = pyxel.KEY_A + i
            letter = chr(ord("A") + i)
            yield key_code, letter
    
    def display_guesses(self):
        pyxel.text(115,10, f"Wrong: {''.join(sorted(self.wrong))}", 8)

    def display_lives(self):
        pyxel.text(130,20, f"Lives: {self.lives}", 10)

    def draw(self):
        pyxel.cls(1)
        pyxel.text(10,10,"HANGMAN!",7)
        lines = self.masked_lines(reveal_all=self.lives == 0)
        line_height = 10 # Not sure how to make this more dynamically sized in pyxel
        for line_number, line in enumerate(lines):
            pyxel.text(5, 20 + line_number * line_height, line, self.guess_color)
        self.display_guesses()
        self.display_lives()
        self.draw_hangman()
        self.show_game_over()
        pyxel.text(10,100,"Type any letter from A-Z to guess", 6)
        pyxel.text(10,110,"Restart F5\nQuit ESC", 6)
