import csv
import random
import time


def read_csv(filename):
    data = []
    r= open("./SYMPTOMDATA.csv", "r", encoding="ISO-8859-1")
    reader = csv.DictReader(r)
    
    for x in reader:
        data.append(x)
    print(len(data))
    return data
a = read_csv("./SYMPTOMDATA.csv")
# ========================================================================================================================
def insertion_sort(data, field):
     for i in range(1, len(data)):
        print(i)
        pivot = int(data[i][field])
        j = i - 1
        while j >= 0 and pivot < int(data[j][field]):
             data[j + 1] = data[j]
             j -= 1
        data[j + 1][field] = pivot
     
# =========================================================================================================================
    
def bubble_sort(data, field):
    n = len(data)
    for i in range(n - 1):
        swapped=False
        print(i)
        for j in range(n - i - 1):
            if int(data[j][field]) > int(data[j + 1][field]):
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped=True
        if not swapped:
            print("DONE WITH BUBBLE SORT")
            return 

# # =====================================================================================
def partition(data, field, low, high):
    if low < high:
        pivot_index = quick_sort(data, field, low, high)
        partition(data, field, low, pivot_index-1)
        partition(data, field, pivot_index + 1, high)


# # Function to partition the data for quick sort
def quick_sort(data, field, l, r):
        pivotindex = random.randint(l,r)
        data[l], data[pivotindex] = data[pivotindex], data[l]
        pivotelement = int(data[l][field])
        l=l+1
        while l<=r:
            
            while l<=r and int(data[l][field])<=pivotelement:
                l+=1
            while l<=r and int(data[r][field])>=pivotelement:
                r-=1
            if l<=r:
                temp = data[l]
                data[l] =data[r]
                data[r] = temp
        temp = data[r]
        data[r] = pivotelement
        data[pivotindex] = temp
        return r
    
# =================================================================================================================
def write_sorted_csv(data, filename):
    r= open(filename, 'w', newline='')
    fieldnames = data[0].keys()
    writer = csv.DictWriter(r, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
# ========================================================================================================================

a = read_csv("./SYMPTOMDATA.csv")[20000:100000]
starttime = time.time()
print("DOING INSERTION SORT")
# b = partition(a, "VAERS_ID", 0, len(a)-1)
# print("DONE WITH QUICK SORT")
# print("THE TOTAL TIME FOR QUICK SORT TO RUN FOR " ,len(a)," MANY DATA IS "+ str(time.time()-starttime))
# b = insertion_sort(a, "VAERS_ID")
# print("THE TOTAL TIME FOR INSERTION SORT TO RUN FOR " ,len(a)," MANY DATA IS "+ str(int(time.time()-starttime)))
b = bubble_sort(a, "VAERS_ID")

# # write_sorted_csv(b, "SORTEDSYMPTOM.CSV")
# # {'VAERS_ID': '0902418', 'AGE_YRS': '56.0', 'SEX': 'F', 'VAX_NAME': 'COVID19 (COVID19 (PFIZER-BIONTECH))', 'RPT_Date': '', 'SYMPTOM': 'Hypoaesthesia', 'DIED': '', 'DATEDIED': '', 'SYMPTOMS TEXT': 'Patient experienced mild numbness traveling from injection site up and down arm that subsided over 20 minutes.'}