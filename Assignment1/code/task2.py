import csv
import random
import time


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
     for i in range(1, len(data)):
      
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
        for j in range(n - i - 1):
            if int(data[j][field]) > int(data[j + 1][field]):
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped=True
        if not swapped:
            print("DONE WITH BUBBLE SORT")
            return 
    print("DONT WITH BUBBLE SORT")
# # =====================================================================================
def partition(data, field, low, high):
    if low < high:
        pivot_index = partition(data, field, low, high)
        quick_sort(data, field, low, pivot_index-1)
        quick_sort(data, field, pivot_index + 1, high)


# # Function to partition the data for quick sort
def quick_sort(data, field, low, high):
    pivotindex = random.randint(low,high)
    pivot = int(data[pivotindex][field])
    left = low+1
    end = high
    while left<=end:
        while left<=end and int(data[left][field]) < pivot:
            l+=1
        while data[end]>pivot and int(data[end][field]) > pivot:
            end-=1
        if left<end:
            temp = data[l]
            data[l] = data[end]
            data[end] = temp
    temp = pivot
    data[pivotindex] = data[end]
    data[end] = temp
    return end

    # while True:
    #     while int(data[left][field]) < pivot:
    #         left += 1
    #     while int(data[right][field]) > pivot:
    #         right -= 1
    #     if left >= right:
    #         return right
    #     data[left], data[right] = data[right], data[left]
    #     left += 1
    #     right -= 1
    
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
starttime = time.time()
# b = partition(a, "VAERS_ID", 0, len(a)-1)
# print("THE TOTAL TIME FOR QUICK SORT TO RUN FOR " ,len(a)," MANY DATA IS "+ str(time.time()-starttime))
b = insertion_sort(a, "VAERS_ID")
# print("THE TOTAL TIME FOR INSERTION SORT TO RUN FOR " ,len(a)," MANY DATA IS "+ str(int(time.time()-starttime)))
# b = bubble_sort(a, "VAERS_ID")

# # write_sorted_csv(b, "SORTEDSYMPTOM.CSV")
# # {'VAERS_ID': '0902418', 'AGE_YRS': '56.0', 'SEX': 'F', 'VAX_NAME': 'COVID19 (COVID19 (PFIZER-BIONTECH))', 'RPT_Date': '', 'SYMPTOM': 'Hypoaesthesia', 'DIED': '', 'DATEDIED': '', 'SYMPTOMS TEXT': 'Patient experienced mild numbness traveling from injection site up and down arm that subsided over 20 minutes.'}