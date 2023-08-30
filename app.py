import intro
import numGenerator
from time import sleep

intro
numGenerator
random_number = numGenerator.random_number

print("")
print("DONE!")
print("")
sleep(.2)
user_input = int(input("Now Guess The Number ;D : "))


while user_input != random_number:
    if user_input > random_number:
        sleep(.2)
        print("")
        print("Aish! Too high")
        user_input = int(input("Guess again!: "))
    if user_input < random_number:
        sleep(.2)
        print("")
        print("Tsk! Too low")
        user_input = int(input("Guess again!: "))

print("")
print("SUPER! You Win")




