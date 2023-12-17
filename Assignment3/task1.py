
import csv
import random
import time



def read_csv(filename):
    data = []
    r =  open( filename, "r", encoding="ISO-8859-1")
    reader = csv.DictReader(r)

    for x in reader:
        data.append(x)
    return data

a = read_csv("../Assignment1/code/VAERS_COVID_NOVEMBER.csv")
a = sorted(a, key=lambda x: int(x["VAERS_ID"]))
b = read_csv("../Assignment1/code/SYMPTOMDATANOVEMBER.csv")
b = sorted(b, key=lambda x: int(x["VAERS_ID"]))
file1counter = 0
file2counter=0
headersymptomnumber = 0
alldata = []

# alldataheader = ["VAERS_ID", "VAX_MANU", ]
alldataheader = ["VAERS_ID", "VAX_MANU", "AGE_YRS", "SEX","DIED","DATE_DIED"]
# alldataheader = ["VAERS_ID", "VAX_MANU", "RECVDATE", "AGE_YRS", "SEX", "DIED","DATE_DIED", "VAX_DATE", "NUMBER_OF_SYMPTOMS"]
ageRset = {
    "NO AGE":[-1,-1],
    "<1 year": [0, 1],
    "1-6years": [1, 6],
    "7-15": [7, 15],
    "16-30": [16, 30],
    "31-48": [31, 48],
    "49-65": [49, 65],
    "> 66": [66, float("inf")],
}

deathcount = 0

while (file1counter<len(a)):
        first = 0
        row = []
 
        if first == 0:
            vaersid = a[file1counter]["VAERS_ID"]
            vaxmanu = a[file1counter]["VAX_MANU"]
            # recvdate = a[file1counter]["RECVDATE"][4:]
            ageyrs = a[file1counter]["AGE_YRS"]
            if ageyrs=="":
                ageyrs="NO AGE"

            else:
                age = float(ageyrs)
                for c,d in ageRset.items():
                        if d[0]<=age and d[1]>=age:
                            ageyrs=c
                            break
            sex = a[file1counter]["SEX"]
            died = a[file1counter]["DIED"]
            datedied = a[file1counter]["DATEDIED"][4:]
            # vaxdate = a[file1counter]["VAX_DATE"][4:]
            first = 1
        symptom = []
        # row= [vaersid, vaxmanu, recvdate, ageyrs, sex, died, datedied, vaxdate]
        row = [vaersid, vaxmanu, ageyrs, sex, died, datedied]
        # row= [vaersid, vaxmanu]
        
        
        numberofsymptom = 0

        
        while file2counter<len(b) and (int(a[file1counter]["VAERS_ID"])==int(b[file2counter]["VAERS_ID"])):
            numberofsymptom+=1
        
            symptom.append(b[file2counter]["SYMPTOM"])
      
    
                 
            file2counter+=1
            if numberofsymptom>headersymptomnumber:
                text = "SYMPTOM_"+str(numberofsymptom)
                headersymptomnumber+=1
                res = b[file2counter]["VAERS_ID"]

                alldataheader.append(text)
                ans =  numberofsymptom
        # symptom.insert(0, numberofsymptom)
        
        withoutheaderdata=row+symptom
        alldata.append(withoutheaderdata)
        vaersSame = False
        file1counter+=1

alldata.insert(0, alldataheader)

outputfilename2 = "TransactionData3.csv"
r2 = open(outputfilename2,"w")
writer = csv.writer(r2)
for row in alldata:
    writer.writerow(row)

