def make_tea(milk=False,sugar=0):
    print("Pouring in milk\n"*int(milk),end="")
    print("Adding",sugar,"sugars")
    return "We made tea with "+str(int(milk)*"milk and ")+str(sugar)+" sugars."

tea1 = make_tea(True,0)
tea2 = make_tea(False,2)
tea3 = make_tea(True)
tea4 = make_tea(True)

print(tea1,tea2,tea3,tea4,sep="\n")