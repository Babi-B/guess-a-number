# Guess A Number Game

## Summary

- This program generates a number and then  prompts the user to guess what the number is
- It provides **hints** like *too hight* or *too low* to guide the user in guessing the actual number

## How the Program Functions

- First of it is a console program 
- It takes two values from the user which serve as the upper and lower range within which the random integer is to be generated
    - There must be a difference of 10 between the lower and upper limits else, the user is prompted to enter an appropriate upper limit which MUST satisfy this condition
    - The user enters a float, the programs typecasts it to an int
- Once the random number is generated, the user is then prompted to guess what it is
    - The number generated will ALWAYS fall within the range the user specified
    - If the number guessed by the user is less than the random number, the user is told *"Too low"* and then prompted to guess again
    - If the number, however, is greater than the random number, the user is told "*Too high"* and then prompted to guess again
    - If the user guesses the correct number, they are declared the winner and the game ends

## Project Structure

- This project is broken down to 3 modules

### The *intro* module

This intro module just prints out text to welcome the user and give the user some insights into what the game is and the rules to the game.

### The *numGenerator* module

In this module, the lower and upper limits are gotten from the user and used to generate the random number needed for the game.

This module also ensures that the difference between the upper and lower limits is 10

### The *app* module

This module imports the aforementioned two (app and numGenerator) modules and combines them to make the body of the game.

## Cool Widgets

- The ***sleep()*** method from the ***time*** module is used to create a delay effect so it seems like some background work is being done.

- a ***for loop*** was built to create a cool loading animation on the console when the random the number is being generated.

### Aside

Thank you for taking interest in my work. I am open to new contributions you might have.

**Thanks!**

***Babi B***