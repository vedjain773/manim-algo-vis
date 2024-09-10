#array = [1, 4, 2, 3, 1, 2, 5]
array = [5,4,3,2,1]

def isSorted(aTC: list):
            flag = 0
            for i in range(len(aTC) - 1):
                if aTC[i] > aTC[i + 1]:
                    flag = 1

            if flag == 1:
                return False
            else:
                return True

def swap(i1, i2, array: list):
            current = array[i1]
            next = array[i2]

            array[i1] = next
            array[i2] = current

def bubbleSort():
        while (isSorted(array) == False):
            for i in range(len(array) - 1):
                if array[i] > array[i + 1]:
                    swap(i, i + 1, array)
                print(array)

def selectionSort():
    start= 0
    while (isSorted(array) == False):
        smallest = array[start]
        index_to_swap = array.index(smallest)
        for i in range(start, len(array)):
            if array[i] < smallest:
                  smallest = array[i]
                  index_to_swap = i

        print(start, index_to_swap)
        swap(start, index_to_swap, array)
        start += 1

        print(array)    

def insertionArr():
    while (isSorted(array) == False):
        for i in range(len(array) -1):
            if array[i+1] < array[i]:
                swap(i, i+1, array)
                print("i", array)

                for j in range(i, 0, -1):
                    print(j)
                    if array[j] < array[j-1]:
                        swap(j, j-1, array)
                        print("j", array)

            print(array)

insertionArr()
