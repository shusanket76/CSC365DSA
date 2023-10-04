import csv
import random


def read_csv(filename):
    data = []
    r= open("./SYMPTOMDATA.csv", "r", encoding="ISO-8859-1")
    reader = csv.DictReader(r)
    
    for x in reader:
        data.append(x)
    return data
a = read_csv("./SYMPTOMDATA.csv")
# ========================================================================================================================
def insertion_sort(data, field):
     a = 1
     for i in range(1, len(data)):
        print(a)
        
      
        pivot = int(data[i][field])
        j = i - 1
        while j >= 0 and pivot < int(data[j][field]):
             data[j + 1] = data[j]
             j -= 1
        data[j + 1][field] = pivot
        a+=1
# =========================================================================================================================
    
def bubble_sort(data, field):
    n = len(data)
    a=0
    for i in range(n - 1):
        print(a)
        swapped=False
        for j in range(n - i - 1):
            if int(data[j][field]) > int(data[j + 1][field]):
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped=True
        if not swapped:
            return 
        a+=1
    print("DONT WITH BUBBLE SORT")
# # =====================================================================================
def quick_sort(data, field, low, high):
    if low < high:
        print(high-low)
        pivot_index = partition(data, field, low, high)
        quick_sort(data, field, low, pivot_index)
        quick_sort(data, field, pivot_index + 1, high)

# # Function to partition the data for quick sort
def partition(data, field, low, high):
    # index = (high-low)
    pivot = int(data[low][field])
    left = low
    right = high

    while True:
        while int(data[left][field]) < pivot:
            left += 1
        while int(data[right][field]) > pivot:
            right -= 1
        if left >= right:
            return right
        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1
# =================================================================================================================
def write_sorted_csv(data, filename):
    r= open(filename, 'w', newline='')
    fieldnames = data[0].keys()
    writer = csv.DictWriter(r, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
# ========================================================================================================================
a = read_csv("./SYMPTOMDATA.csv")
print(len(a))
b = quick_sort(a, "VAERS_ID", 0, len(a)-1)
b = insertion_sort(a, "VAERS_ID")
# b = bubble_sort(a[0:500], "VAERS_ID")

# # write_sorted_csv(b, "SORTEDSYMPTOM.CSV")
# # {'VAERS_ID': '0902418', 'AGE_YRS': '56.0', 'SEX': 'F', 'VAX_NAME': 'COVID19 (COVID19 (PFIZER-BIONTECH))', 'RPT_Date': '', 'SYMPTOM': 'Hypoaesthesia', 'DIED': '', 'DATEDIED': '', 'SYMPTOMS TEXT': 'Patient experienced mild numbness traveling from injection site up and down arm that subsided over 20 minutes.'}