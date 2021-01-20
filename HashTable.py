class HashTable:
    def __init__(self,values):
        self.table= [37]
        self.values=[]
    def hash(self,string):
        h=37
        total=0
        for i in range(0,len(string)):
            total+=h*total+ord(string[i])
            
        total%=len(self.table)
        return int(total)
   
    #def showDistro():
     #   for key in self.table:
    def put(self,data):
        position=self.hash(data)
        self.table[position]=data
    def get(self,key):
        return self.table[self.hash(key)],key

hashTable=HashTable(["Hola"])
hashTable.put("Mundo")
data,key=hashTable.get("Mundo")
print("data[",key,"]=",data)
            