from itertools import combinations
import csv

class Task22:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.originaldata=[]
    def readdatafromfile(self):
        datarray= []
        r = open(self.filename)
        reader = csv.DictReader(r)
      

        for x in reader:
            datarray.append(x)
       
        self.originaldata = datarray
        self.data=self.originaldata.copy()
    

    def createuniqueset(self, order):
      
        self.uniqueset=set()
        if order==1:
            for x in self.data:
             
                for a,b in x.items():
                    if b is not None:
                    
                        self.uniqueset.add(b)
            self.combination = self.uniqueset.copy()
        elif order == 2:
            self.combination = list(combinations(self.data.keys(), order))
        else:
            for e,f in self.data.items():
                for d in e:
                    self.uniqueset.add(d)
                
            self.combination = list(combinations(self.uniqueset, order))
       
    
        
    
    def createfrequency(self, order):
        
        self.data = {}
        if order==1:
            for x in self.originaldata:
                for key,value in x.items():
                    if value==None:
                        continue
                    self.data[value] = self.data.get(value, 0)+1
           
        else:
            

            for x in self.originaldata:
                singleset = set(x.values())
                for a in self.combination:
                    if set(a).issubset(singleset):
                        self.data[a] = self.data.get(a,0)+1
        
            

    def purnedata(self, support):
        self.newdata= self.data.copy()
        for x,y in self.data.items():
            if y<support:
                self.newdata.pop(x)
        self.data = self.newdata.copy()
        print(self.data)
        
        
        
    
    def allfun(self, order, support):
        if order==1:
            print('s')
            self.readdatafromfile()
        self.createuniqueset(order)
        self.createfrequency(order)
        self.purnedata(support)
        print("DONE WITH "+ str(order))

a = Task22("./TransactionData3.csv")
a.allfun(1,15000)
a.allfun(2,1000)
a.allfun(3,800)
a.allfun(4,600)
a.allfun(5,600)
a.allfun(6,600)
a.allfun(7,300)
a.allfun(8,100)


                    

        


