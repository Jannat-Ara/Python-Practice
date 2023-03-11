if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    sorted_array = sorted(arr, reverse= True)
    max = sorted_array[0]

    for num in sorted_array:
        if num > max:
            sorted_array.remove(num)
    print (sorted_array)        
