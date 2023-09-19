# Hangman game  

import random

#list of words for the game

cars = ['Audi', 'Benz', 'Volkswagen', 'BMW', 'Volvo', 'Subaru', 'J5', 'Tesla', 'Ford', 'Lexus']

#Function  to choose a random from cars
def choose_car():
    return random.choice(cars)

# Function to play the Hangman game 
def Hangman():
    word_to_guess = choose_car()
    guessed_letters = []
    attempts = 6
    
    print ('Enjoy the game!')
    
    while attempts > 0:
        display_word = ''
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter
            
            else:
                display_word += "_"
                
        print(f"Word: {display_word}")
        print(f"Guessed Letters: {', '.join(guessed_letters)}")

        
        guess = input ("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        if guess in word_to_guess:
            print('Good guess!')
            if set(word_to_guess) == set(guessed_letters):
                print('Congratulations! You have won!')
                break
            
        else:
            print("Wrong guess.")
            attempts -= 1
            
    else:
        print(f"Sorry, you ran out of attempts. The word was '{word_to_guess}'.")
        
if __name__ == "__main__":
    Hangman()