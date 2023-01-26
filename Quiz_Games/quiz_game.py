print("Welcome to my quiz!")

playing = input("Would you like to begin?")

if playing != "yes":
    quit()

print("Okay! Let's play.")
score = 0

#-----Begin Quiz-----#
answer = input("What is five plus one?")
if answer == "six":
    print('Correct!')
    score += 1
else:
    print("Incorrect.")



answer = input("What colors are apples?")
if answer == "Red":
    print('Correct!')
    score += 1
else:
    print("Incorrect.")


answer = input("hi")
if answer == "hi":
    print('Correct! Quiz over.')
    score += 1
    
else:
    print("Incorrect.")

print("Your score was " + str(score))