import random

def loadWord():
    
    ''' Populate each list with at least 10 different items.  Create a variable called secretWord that is assigned a random word from one of the lists. 
    
    return a tuple in the following format:  (secretWord, list the secretWord is from)   
    
    Hint:  You will need to randomly choose one of the lists, and THEN choose a random word from that list.
    '''
    persons = ['Felipe', 'James', 'Pro', 'Garland', 'Willie', 'Shamori']
    places = ['Ocala', 'Florida', 'USA', 'Home']
    things = ['ball', 'doll', 'bag']
    listOfLists = [persons, places, things]
    randomListChoice = random.choice(listOfLists)
    
    hint = ''
    secretWord = random.choice(randomListChoice)
    
    if randomListChoice == persons:
        hint = 'person'
    elif randomListChoice == places:
        hint = 'places'
    else:
        hint = 'thing'
        
    return (secretWord, hint)
    
hangmanPics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']    
    

def isWordGuessed(secretWord, lettersGuessed):
   for letter in secretWord:
       if letter not in lettersGuessed:
           return False
   return True
   

        
    

def getGuessedWord(secretWord, lettersGuessed):
     printedWord = ''
    
     for letter in secretWord:
         if letter in lettersGuessed:
            printedWord += letter + ' '
         else:
            printedWord += '_ '
     return printedWord
    



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lettersAvailable = ''
    
    for letter in alphabet:
        if letter not in lettersGuessed:
            lettersAvailable += letter + ' '
    return lettersAvailable
    
    

def hangman():
    
    
     loaded = loadWord()
     secretWord = loaded[0]
     hint = loaded[1]
     alphabet = 'abcdefghijklmnopqrstuvwxyz'
     secretWord = secretWord.lower()                               #make sure they are passing you a lowercase letter
     wrongGuesses = 0
     lettersGuessed = []
     
     print "Welcome to hangman!  I'm thinking of a " + hint + '.'
     
     
     while wrongGuesses < 6:
         if isWordGuessed(secretWord, lettersGuessed) == True:
            return "You Win!"
         else:
              print getAvailableLetters(lettersGuessed)
              guess = raw_input("Please guess a letter:     ")
              guess = guess.lower()
              while len(guess) != 1 or guess not in alphabet or guess in lettersGuessed:
                  print getAvailableLetters(lettersGuessed)
                  guess = raw_input("Invalid guess!  Please pick one available letter:    ")                                                                                                          									#is not a lett                                                              
              
         
         
         
         
              if guess not in secretWord:
                 wrongGuesses += 1
                 "Sorry thats a wrong guess!"
              else:
                print "Good Guess!"
              
              lettersGuessed.append(guess)
              print getGuessedWord(secretWord, lettersGuessed)
              print hangmanPics[wrongGuesses]
              
     return "HANGED BOY"
        
        
     
     
      