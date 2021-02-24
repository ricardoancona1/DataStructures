class BubbleSort:
    inputList = []
    sortedList = []

    def inputData():
        size = int(input("Please input number of elemets "))
        BubbleSort.inputList = [None]*size
        BubbleSort.sortedList = [None]*size
        for i in range(0, size):
            element = input("Input element ")
            BubbleSort.inputList[i] = element
            BubbleSort.sortedList[i] = element
        BubbleSort.sort(size)

    def sort(size):#[4,22,13]
        print("size = ",size)
        for i in range(1, size):
            for j in range(0, size-1):
                k=j+1
                currentValue=int(BubbleSort.sortedList[j] )
                nextValue=int(BubbleSort.sortedList[j+1])
                if currentValue> nextValue:
                    
                    print("sortedList[",j,"](",BubbleSort.sortedList[j],") > sortedList[",k,"](",BubbleSort.sortedList[k],") =true")
                    aux = BubbleSort.sortedList[j]
                    BubbleSort.sortedList[j] = BubbleSort.sortedList[j+1]
                    BubbleSort.sortedList[j+1] = aux
                else:
                     print("sortedList[",j,"](",BubbleSort.sortedList[j],") > sortedList[",k,"](",BubbleSort.sortedList[j+1],") =false")
        print("input list", BubbleSort.inputList)
        print("Sorted list", BubbleSort.sortedList)


BubbleSort.inputData()
