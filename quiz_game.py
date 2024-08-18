print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :) ")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("What does ROM stand for? ").lower()
if answer == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")
print("")
print("You got " + str(score) + " questions correct!")
print("")
print("You got " + str((score/4)*100 )+ "%. ")
print("")
print("Thanks for playing!")    

