def advanced_input(message,conversion=lambda x: x,*funcs):
    counter = 1
    while True:
        try:
            if counter != 1:
                print("Attempt {}:".format(counter))
            print(message)
            result = conversion(input())
            for function in funcs:
                assert function(result)
        except:
            print("Please, try again")
        else:
            return result
        finally:
            counter += 1

x = advanced_input("Input a number between 1 and 10",int,lambda x: x <= 10, lambda x: x >= 1)
print("x + 1 = {}".format(x+1))