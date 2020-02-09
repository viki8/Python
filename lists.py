myUniqueList = [ ]
myLeftovers = [ ]
print("empty list:", myUniqueList)

def add(*args):
    print("list of agrs passd:", args)
    for x in args:
        if x not in myUniqueList:
            myUniqueList.append(x)
            print("ading", x, "to the list:", myUniqueList)
            print(bool(x))
        else:
            #x in myUniqueList:
            print("value", x,"not unique adding to global list")
            myLeftovers.append(x)
            print(bool())
    print("my unique list:", myUniqueList)
    print("my leftovers:", myLeftovers)

add(10, 20, 30, 40, 40, 50, 50, 60, 60, 0.95, "hello", "hi", "hi")