rough_age = int(input("How old does the person look?\n"))
if rough_age > 25:
    print("You are allowed in.")
elif rough_age > 16:
    real_age = int(input("What does their id say?\n"))
    if real_age >= 18:
        print("You are allowed in.")
    else:
        print("You are not allowed in.")
else:
    print("You are not allowed in.")