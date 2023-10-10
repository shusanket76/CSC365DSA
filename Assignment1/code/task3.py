import csv
def read_csv(filename):
    data = []
    r = open(filename, "r", encoding="ISO-8859-1")
    reader = csv.DictReader(r)
    
    for x in reader:
        
        data.append(x)
  
            
    return data

a = read_csv("./SYMPTOMDATA.csv")
# a = read_csv("./VAERS_COVID_DataAugust2023.csv")

ageRset = {
    "NO AGE":[-1,-1],
    "<1 year": [0, 1],
    "1-3 years": [1, 4],
    "4-11": [4, 12],
    "12-18": [12, 19],
    "19-30": [19, 31],
    "31-40": [31, 41],
    "41-50": [41, 51],
    "51-60": [51, 61],
    "61-70": [61, 71],
    "71-80": [71, 81],
    "> 80": [81, float("inf")],
}

ageGroups = {
    "NO AGE":[],
    "<1 year": [],
    "1-3 years": [],
    "4-11": [],
    "12-18": [],
    "19-30": [],
    "31-40": [],
    "41-50": [],
    "51-60": [],
    "61-70": [],
    "71-80": [],
    "> 80": []
}
blank=0

for x in a:
    
    if x["AGE_YRS"]=="":
        ageGroups["NO AGE"].append(x)

    else:
        age = float(x["AGE_YRS"])
        for c,d in ageRset.items():
            if d[0]<=age and d[1]>=age:
                ageGroups[c].append(x)

# ========================================================================
def insertion_sort(data, field):
    a=0
    for i in range(1, len(data)):
        pivot = float(data[i][field])
        j = i - 1
     
        while j >= 0 and pivot < float(data[j][field]):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1][field] = pivot
        a+=1
    
def insertion_sortWords(data, field):
    a=0
    for i in range(1, len(data)):
        
       
        pivot = data[i][field]
        j = i - 1
     
        while j >= 0 and pivot < data[j][field]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1][field] = pivot
        a+=1
 
# for z in ageGroups:
#     if z=="NO AGE":
#         continue

#     insertion_sort(ageGroups[z], "AGE_YRS")
# print("DONEEEEEE")
# for i in ageGroups:
#     insertion_sortWords(ageGroups[i], "SEX")
# for k in ageGroups:
#     insertion_sortWords(ageGroups[k], "VAX_NAME")

# ==========================================DEATHS COUNTS======================================================================================
unique = set()
a=0
b=0
count=0
res = []
for j in ageGroups:
    d = 0
    for l in ageGroups[j]:
        count+=1
        # print(str(a)+"============================================================"+str(b))
        if l["DIED"]=="Y" and l["VAERS_ID"] not in unique:
            d+=1
            unique.add(l["VAERS_ID"])
        
    res.append(d)
print(res)
res1=0
for sh in res:
    res1+=sh
print(res1)

# MANY DATA WHERE THE THERE IS NO DATA IN THE AGE FIELD
# NO AGE GROUP    12267
# <1 year         7
# 1-3 years,      7
# 4-11,           46
# 12-18,          188
# 19-30,          480
# 31-40,          660
# 41-50,          1157
# 51-60,          2358
# 61-70,          4734
# 71-80,          6437
# > 80),          7739
# [12267, 7, 7, 46, 188, 480, 660, 1157, 2358, 4734, 6437, 7739]
# 36080
