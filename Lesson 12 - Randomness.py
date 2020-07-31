import random
print(random.random())#0.8415640773870189
print(random.random())#0.1696140275959741
print(random.randrange(10))#6
print(random.randrange(10))#2
print(random.randint(1,10))#5
print(random.randrange(5,15,2))#11
print(["a","b","c","d"])#['a', 'b', 'c', 'd']
print(random.choice(["a","b","c","d"]))#'c'
print(random.choice(range(10)))#8
print(random.shuffle(["a","b","c","d"]))#None
list = ["a","b","c","d"]
random.shuffle(list)
print(list)#['d', 'b', 'a', 'c']
