from phrasehunter.phrase import Phrase
import random

class Game:
    def __init__(self): # this method sets the defualt values for the attributes 
        self.missed = 0
        self.phrases = [Phrase('try try till'), 
                        Phrase('play to win'), 
                        Phrase('learning python is'), 
                        Phrase('lion is king'), 
                        Phrase('let and let live')]
        self.active_phrase = None
        self.guesses = []
    
    
    def start(self):  # starts the game 
        self.welcome()
        self.active_phrase = self.get_random_phrase()
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            self.active_phrase.display(self.guesses)
            print("\n")
            user_guess = self.get_guess()
            self.guesses.append(user_guess) # append user guess to the guesses list
            self.active_phrase.check_letter(user_guess)
            if not self.active_phrase.check_letter(user_guess):
                print(f"Incorrect guesses: {self.missed}\n")
        self.game_over()
        print('The phrase was:', self.active_phrase.phrase.upper()) 
        self.continue_playing()

    
    def get_random_phrase(self): # to pick a random phrase from the available options for starting the game
        return random.choice(self.phrases)
        
    
    def welcome(self): #welcome message to display when game starts
        welcome_title = 'WELCOME TO PHRASEHUNTING GAME'
        print('\n', '=' * len(welcome_title), '{}'.format(welcome_title),'=' * len(welcome_title), '\n')
        
            
    def get_guess(self):
        #validates the user input for guessing game to make sure valid input and handle exceptions, also counts for user chances left for game to be won
        user_guess = input("Enter the guessing letter for guessing the guess phrase?  ")
#       print('\n')
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
            print(f'You already guessed "{user_guess}" Please Try again with a new letter')
        else:
            self.guesses.append(user_guess)
            if self.active_phrase.check_letter(user_guess):
               print('\n')
            else:
                print("You have guessed an incorrect letter. Please Try again.")
                self.missed += 1
                print("######## You are left with {} out of 5 chances to win this round! ########\n".format((5 - self.missed)))
        return user_guess 
    

    def game_over(self): #controls game result for winning or losing
        self.active_phrase.display(self.guesses)
        if self.missed == 5:
            print('\nAll the chances are over for guessing the phrase, GAME OVER!\n')
        else:
            print('\nCongrats, You guessed it right!!!\n')
            
            
    def continue_playing(self): and #resets the active phrases and restarts the new round if user wants to continue playing
        user_continuing = input('Would you like to continue playing(Y(es)/N(o)?  ')
        if user_continuing.lower() == 'y':
            self.active_phrase = None
            print('\n')
            new_game = Game()
            new_game.start()
        else:
            print('Thanks for playing PHASEHUNTER GAME, byeee for now!')
        
