importantItems = [7,3.14159,True,"Python",print]
importantItems[0] = 2357
importantItems[-1] = len
print("My important items are:",*importantItems,sep="\n")
print("There are",len(importantItems),"items that are important in this list.")