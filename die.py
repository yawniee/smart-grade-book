#create a program that rolls 2 die using loops
#importing randint function from random
from random import randint
#Using variable to detect if the user wants to keep playing
Playing = True
#Using while loop
while Playing:
#asking the user if they want to roll the die
    Question = input("Do you want to roll the die?(y/n)").lower().strip()#lower makes the letter lowercase and strip function to remove any whitespace
#if we type y, variable will take 2 random values from 1 to 6 and print them
    if Question == "y":
#2 variables random1 and random2 are given random integer values using randint function and the numbers inside the brackets show the range of numbers
        random1 = randint(1, 6)
        random2 = randint(1, 6)
#these 2 variables will be randomly given an integer through 1 to 6
        print(f"{random1}, {random2}")
#this will print the values of the 2 variables
#if we type n, the program prints a statement and closes
    elif Question == "n":
        print("Thanks for playing!")
        Playing = False
#if anything other than y or n is typed, it will print this error
    else: 
        print("Invalid Error")
