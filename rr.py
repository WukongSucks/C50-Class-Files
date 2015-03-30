import random

def roulettegame(numberTry,EvenorOdd,colorTried):
    blackList = [2,4,6,8,10,11,13,15,17,20,22,24,26,20,31,33,35]
    redList= [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    greenList = [0,37]
    number = random.randint(0,37) 
    actualColor = ''
    actualEvenOrOdd = ''
    if number in blackList:
        actualColor = "Black"
    elif number in redList:
        actualColor = "Red"
    elif number in greenList:
        actualColor ="Green"
        
    if number % 2 == 0 and number not in greenList:
        actualEvenOrOdd = 'Even'
    elif number % 2 == 1 and number not in greenList:
        actualEvenOrOdd = 'Odd'
    else:
        actualEvenOrOdd = 'ZERO'
    print actualColor
    print actualEvenOrOdd
    print number
    
    if number == numberTry and actualColor == colorTried:
        print "Winner"
    else:
        print "Loser"
                                                            
                                                            ###check to see if number == number they guessed
                                                            #check to see if actualColor == color they guessed
                                                            #check to see if actualEvenOrOdd = evenOrOddGuess
                                                            #let player know what bets they won
    

    

        
    
     
    
