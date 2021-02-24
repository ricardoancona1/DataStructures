def reverseStrng(string):
    i=len(string)-1
    reversedString=""
    while(i!=-1):
        reversedString+=string[i]
        i=i-1
    return reversedString
#inputString=input("Please input a string to reverse :")
#reversedStr=reverseStrng(inputString)
#print("This is the reversed string",reversedStr)

def find_missing():
    A1=[1,2,3,4,5]
    A2=[1,2,4,5]
    size=len(A1)+1
    missing=[]
    for i in range(0,len(A1)-1):     
        found=False
        for j in range(0,len(A2)-1):
            if A1[i]==A2[j]:
                found=True
        if found==False:
            missing.append(A1[i])
    
    print(missing)
find_missing()
    
