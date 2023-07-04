x = int(input("ENter the value:"))
match x:
    case 0:
        print("X is Zero")
    case 4 if x % 2 ==0:
        print("x % 2 == 0 and case is 4")
    case _ if x <10:
        print(x)