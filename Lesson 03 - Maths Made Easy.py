print(3 == 3)#True
print(3 == 4)#False
print("a" == "a")#True
print("3" == 3)#False
print(4 > 2)#True
print(4 < 2)#False
print(3 >= 3)#True
print(3 >= 4)#False
print("a" > "b")#False
print("a" < "b")#True
print("A" < "B")#True
print("a" < "B")#False
print("z" > "A")#True
print(3 < "3")#TypeError: '<' not supported between instances of 'int' and 'str'
print("32" < "255")#False
print(3==3 and 4==4)#True
print(3==3 and 4==5)#False
print(3==3 or 4==4)#True
print(3==3 or 4==5)#True
print(not 3==3)#False
print(3==3 not 4==4)#SyntaxError: invalid syntax
print(3==3 and not 4==3)#True
print((3==4 and 5==5) or (3==3 and not 4==2))#True
print(3+5)#8
print(5*25)#125
print(79/3)#26.333333333333332
print(26.333333333333332 * 3)#79.0
print(8-5)#3
print(5-8)#-3
print(5--8)#13
print(5-(-8))#13
print(79//3)#26
print(25//5)#5
print(79%3)#1
print(5%5)#0
print(-5%1)#0
print(-5%2)#1
print(-55%-2)#-1
print(3**4)#81
print(3*3*3*3)#81
print(5**1/2)#2.5
print((5**1)/2)#2.5
print(5**(1/2))#2.23606797749979
print(2**.5)#1.4142135623730951
print((5+5)==10)#True
print(5+5 < 6)#False