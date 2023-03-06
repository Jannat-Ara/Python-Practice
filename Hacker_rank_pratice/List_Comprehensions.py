if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    new_list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n]
    print(new_list)

    #another way
    x1 = int(input())
    y1 = int(input())
    z1 = int(input())
    n1 = int(input())
    new_list1 =[]

    for i in range(x1+1):
        for j in range(y1+1):
            for k in range(z1+1):
                if (i+j+k)!= n1:
                    new_list1.append([i,j,k])
    print(new_list1)


