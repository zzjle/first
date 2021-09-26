def bubbleSort(array):
    i = 0
    j = 0
    while j < len(array):
        j += 1
        while i < len(array)-j:
            if array[i] < array[i+1]:
                i += 1
            elif array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                i += 1
            else:
                i += 1
    else:
        print(array)


array1 = input("用逗号分隔的数组").split(",")

bubbleSort(array1)
