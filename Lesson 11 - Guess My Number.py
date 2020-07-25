import time
min = 0
max = 100
print("Please, pick a number between",min,"and",max)
time.sleep(5)
guess = (min + max) // 2
state = "wrong"
count = 0
while state != "correct" and state != "error":
    state = input("I guess "+str(guess)+"\nIs my guess correct? [y/n]: ").strip().lower()
    count += 1
    while state != "y" and state != "n":
        state = input("Please, enter y for yes and n for no: ").strip().lower()
    if state == "y":
        state = "correct"
    else:
        state = input("Is your number higher or lower? [h/l]: ").strip().lower()
        while state != "h" and state != "l":
            state = input("Please, enter h for higher and l for lower: ").strip().lower()
        if min == max:
            state = "error"
        if state == "h":
            min = guess + 1
        else:
            max = guess - 1
        guess = (min + max) // 2
if state == "correct":
    print("I guessed your number in ",count," guess","es"*count != 1,"!",sep="")
else:
    print("Something went wrong!")