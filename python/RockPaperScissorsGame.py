#!/usr/bin/python2.7 
'''
Created on Jul 15, 2012
Create a simple Rock, Paper, Scissors game.
@author: MNickey
'''
import random
from random import randint

def compPlayer():
    c = random.randint(0,2)
    if c == 0:
        y = 'rock'
    elif c == 1:
        y = 'paper'
    else:
        y = 'scissors'
    return y

def player():
    x = raw_input("Enter 'rock', 'paper' or 'scissors'")
    return x

def compareHands(y, x):
    if y == 'rock' and x == 'rock': #the computer hand won
        return 0
    elif y == 'rock' and x == 'scissors':
        return -1
    elif y == 'rock' and x == 'paper':
        return 1
    elif y == 'scissors' and x == 'rock':
        return 1
    elif y == 'scissors' and x == 'scissors':
        return 0
    elif y == 'scissors' and x == 'paper':
        return -1
    elif y == 'paper' and x == 'rock':
        return 1
    elif y == 'paper' and x == 'scissors':
        return 1
    elif y == 'paper' and x == 'paper':
        return 0

def game():
    for i in xrange(999):
        computerHand = compPlayer()
        playerHand = player()
        result = compareHands(computerHand, playerHand)
        if computerHand == 'rock':
            print 'The computer chose rock'
        elif computerHand == 'paper':
            print 'The computer chose paper'
        elif computerHand == 'scissors':
            print 'The computer chose scissors'
        
        if result == -1:
            print 'You Lose!'
        elif result == 0:
            print "It's a Tie!"
        elif result == 1:
            print "You win!"
            
        again = raw_input("Do you want to play again?\nEnter y to play again.")
        if again == 'y' or again == 'Y':
            print
        else: 
            print "Thanks for playing!"
            break
    
if __name__ == '__main__':
    game()
