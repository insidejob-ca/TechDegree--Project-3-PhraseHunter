from phrasehunter.phrase import Phrase
import random

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase('try try till'), 
                        Phrase('play to win'), 
                        Phrase('learning python is'), 
                        Phrase('lion is king'), 
                        Phrase('let and let live')]
        self.active_phrases = None
        self.guesses = []
    
    
    def start(self):
        self.welcome()
        self.active_phrases = self.get_random_phrase()
        while self.missed < 5 and self.active_phrases.check_complete(self.guesses) == False:
            print(f"Incorrect guesses : {self.missed}")
            self.active_phrases.display(self.guesses)
            print("\n")
#            self.handle_guess()
            user_guess = self.get_guess()
            self.guesses.append(user_guess) # append user guess to the guesses list
            self.active_phrases.check_letter(user_guess)
#            self.handle_guess()
            if not self.active_phrases.check_letter(user_guess):
#                self.missed += 1
                print(f"Incorrect guesses: {self.missed}")
        print('The phrase was:', self.active_phrases.phrase.upper())        
        self.game_over()
        self.continue_playing()
    
    def get_random_phrase(self):
        return random.choice(self.phrases)
        
    

    def welcome(self):
        welcome_title = 'WELCOME TO PHRASEHUNTING GAME'
        print( '=' * len(welcome_title), '{}'.format(welcome_title),'=' * len(welcome_title))
        
        
    def get_guess(self):
        user_guess = input("Enter the guessing letter for guessing the guess phrase?  ")
        user_guess = user_guess.lower()
        while True:
            if user_guess.isalpha():
                if len(user_guess) == 1:
                    break
                else:
                    print("Game accepts only one letter per chance for guessing the letter. Please try again with the single valid letter.")
                    user_guess = self.get_guess()
                    continue
            else:
                print("Your guess can only contain a letter, symbols & spaces and any other option is invalid for this game.\nPlease try again with the valid letter.")
                user_guess = self.get_guess()
                continue                
        if user_guess in self.guesses:
            print(f'You already guessed `{user_guess}`')
        else:
            self.guesses.append(user_guess)
            if self.active_phrases.check_letter(user_guess):
                self.active_phrases.display(self.guesses)
                print('\n')
            else:
                print("You have guessed an incorrect letter. Please Try again with a new letter.")
                self.missed += 1
                print("You are left with {} out of 5 chances to win this round!".format((5 - self.missed)))
#        self.display()      
        return user_guess            
            
    def handle_guess(self):
        try:
            result = self.active_phrases.check_letter(self.get_guess())
            if result is False:
                self.missed += 1
        except ValueError as err:
            print(err)    
    
    def game_over(self):
        if self.missed == 5:
            print('All the chances are over for guessing the phrase, GAME OVER!') 
        else: 
            print('Congrats, You guessed it right!!!')
            
            
    def continue_playing(self):
        user_continuing = input('Would you like to continue playing(Y(es)/N(o)?  ')
        if user_continuing.lower() == 'y':
            self.active_phrases.reset()
            print('\n')
            new_game = Game()
            new_game.start()
        else:
            print('Thanks for playing PHASEHUNTER GAME, byeee for now!')
        
