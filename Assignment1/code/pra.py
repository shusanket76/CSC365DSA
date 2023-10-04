# # # INSERTION SORT

# # arra= [43,23,12,32,45,54,34,45,45,43,54,6,78,98,87,5]

# # # def inserSort(array):

# # #     for x in range(len(arra)):
       
# # #         pivot = arra[x]
# # #         j=x-1
# # #         while j>=0 and arra[j]>pivot:
# # #             arra[j+1]=arra[j]
        
# # #             j=j-1
# # #         arra[j+1] = pivot
# # #     print(arra)
# # # a = inserSort(arra)

# # age_ranges = {
# #     "<1 year": [0, 1],
# #     "1-3 years": [1, 4],
# #     "4-11": [4, 12],
# #     "12-18": [12, 19],
# #     "19-30": [19, 31],
# #     "31-40": [31, 41],
# #     "41-50": [41, 51],
# #     "51-60": [51, 61],
# #     "61-70": [61, 71],
# #     "71-80": [71, 81],
# #     "> 80": (81, float("inf")),
# # }
# # for x in age_ranges.values():

# #     if x[0]<=34 and x[1]>=34:
# #         print(x)
# def insertion_sortWords(data, field):
#     a=0
#     for i in range(1, len(data)):
#         print(a)
       
#         pivot = data[i]
#         j = i - 1
     
#         while j >= 0 and pivot < data[j]:
#             data[j + 1] = data[j]
#             j -= 1
#         data[j + 1] = pivot
#         a+=1
#     return data
# # a = ["ram","shyam","gasha","arsenak","ksajskajs","a"]

# # print(insertion_sortWords(a,a))

# a = {1:2, 3:4, 5:6}
# for x in a:
#     print(x)

from collections import defaultdict


hasmap = defaultdict(list)
a = [1,2,3,4,1,2,3,4,12,3,5]
for x in a:
    hasmap[x].append("Hello")
print(len(hasmap))
