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

    def sort(size):
        for i in range(1, size):
            for i in range(0, size-1):
                if BubbleSort.sortedList[i] > BubbleSort.sortedList[i+1]:
                    aux = BubbleSort.sortedList[i]
                    BubbleSort.sortedList[i] = BubbleSort.sortedList[i+1]
                    BubbleSort.sortedList[i+1] = aux
        print("input list", BubbleSort.inputList)
        print("Sorted list", BubbleSort.sortedList)


BubbleSort.inputData()
