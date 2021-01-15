class Stack:
    stack=[None]*5 #Define array lenght of 5
    top=-1

    def printStack():
        print(Stack.stack)

    def pushElementToStack():
        inputValue=input("Please input a value ")
        if  Stack.top==-1:
            Stack.top=Stack.top+1
            Stack.stack[Stack.top]=inputValue
        elif Stack.top==4:
            print("Sorry, stack is full")
        else:
            Stack.top=Stack.top+1
            Stack.stack[Stack.top]=inputValue


    def popElementOfStack():
        if Stack.top==-1:
            print("Sorry, stack is empty, nothing to pop out")
        else:
            poppedElement=Stack.stack[Stack.top]
            Stack.stack[Stack.top]=None
            Stack.top=Stack.top-1
            print("Value %s has been popped out of the stack"%poppedElement)
            
    def printMenu():
        print("Please input \n0.-Print stack \n1.-Push \n2.-Pop \n3.-Exit")
        inputOption=input()
        return int(inputOption)
print("Welcome to the stack software")
while True:
    inputOption=Stack.printMenu()
    if inputOption==0:
        Stack.printStack()
    elif inputOption==1:
        Stack.pushElementToStack()
    elif inputOption==2:
        Stack.popElementOfStack()    
    elif inputOption==3:
        print("bye, come back anytime :)")
        break
    else:
        print("Sorry wrong input")



#print(Stack.stack)
#Stack.printMenu()