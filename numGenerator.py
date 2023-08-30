import random
from time import sleep

# Get lower and upper limits from the user

print("")
print("Note! The difference between the lower and the upper limits must be atleast 10")
sleep(.5)
print("")
lower_limit = int(input("Enter your lower limit: "))
print("")
sleep(.5)
upper_limit = int(input("Enter your upper limit: "))
print("")

# Upper limit should be greater than lower limit by 10

while (upper_limit - lower_limit < 10 ):
    sleep(.5)
    print("Please, the difference between the lower and the upper limits must be atleast 10")
    print("")
    sleep(.5)
    upper_limit = int(input("Enter your upper limit: "))
    print("")

# Generate random number

print ("Generating a random number.")
sleep(1)
print ("  This might take a while... ", end="\r")

# spinning animation
animation = "|/-\\"
idx = 0

for letter in "spinning animation":
    print(animation[idx % len(animation)], end="\r")
    idx += 1
    sleep(0.3)


random_number = random.randint(lower_limit, upper_limit)

