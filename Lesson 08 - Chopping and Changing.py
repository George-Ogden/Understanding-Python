string1 = "b"+"a"+"l"*2
print(string1)#'ball'
list1 = ["b"] + ["a"] + 2 * ["l"]
print(list1)#['b', 'a', 'l', 'l']
string1[1] = "e"#TypeError: 'str' object does not support item assignment
string1 = "bell"
list1[1] = "e"
print(list1)#['b', 'e', 'l', 'l']
list1 = ["b","a","l","l"]
string1 = "ball"
string1 = string1 + "et"
print(string1)#'ballet'
list1 = list1 + ["e","t"]
print(list1)#['b', 'a', 'l', 'l', 'e', 't']
list1[1] = "i"
list1[0] = "f"
print(list1)#['f', 'i', 'l', 'l', 'e', 't']
string1 = "fillet"
list1.pop()#'t'
print(list1)#['f', 'i', 'l', 'l', 'e']
list1.remove()#TypeError: remove() takes exactly one argument (0 given)
list1.remove("e")
print(list1)#['f', 'i', 'l', 'l']
list1.pop(0)#'f'
print(list1)#['i', 'l', 'l']
list1.insert(0,"b")
print(list1)#['b', 'i', 'l', 'l']
list2 = list1
print(list1)#['b', 'i', 'l', 'l']
print(list2)#['b', 'i', 'l', 'l']
list1[0] = "m"
print(list1)#['m', 'i', 'l', 'l']
print(list2)#['m', 'i', 'l', 'l']
list3 = list2.copy()
list2[-1] = "e"
print(list1)#['m', 'i', 'l', 'e']
print(list2)#['m', 'i', 'l', 'e']
print(list3)#['m', 'i', 'l', 'l']
list3[0] = "t"
print(list3)#['t', 'i', 'l', 'l']
list4 = list("dis")
print(list4)#['d', 'i', 's']
print(str(4))#'4'
print(str(list4))#"['d', 'i', 's']"
str(*list)#TypeError: type object argument after * must be an iterable, not type
str(*list4)#TypeError: decoding str is not supported
list4.extend(list3)
print(list4)#['d', 'i', 's', 't', 'i', 'l', 'l']
print(list3)#['t', 'i', 'l', 'l']
list4.append("e")
list4.append("d")
print(list4)#['d', 'i', 's', 't', 'i', 'l', 'l', 'e', 'd']
list4.clear()
print(list4)#[]
