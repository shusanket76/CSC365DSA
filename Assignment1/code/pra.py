# import random
# arra = [21,1,324,35,2,64,1,32,4,35,4,6,4,3,4423,3,24,3,5,46,5,57,6,74,544,34323,23,24,35,45,45,34,34343546,45,343]


# def quick_sort(l,r):
#     pivotindex = l
#     # arra[l], arra[pivotindex] = arra[pivotindex], arra[l]
#     pivotelement = arra[l]
#     # pivotindex=l
#     l=l+1
#     while l<=r:
#         while l<=r and arra[l]<=pivotelement:
#             l+=1
#         while l<=r and arra[r]>=pivotelement:
#             r-=1
#         if l<=r:
#             temp = arra[l]
#             arra[l] =arra[r]
#             arra[r] = temp
#     temp = arra[r]
#     arra[r] = pivotelement
#     arra[pivotindex] = temp
#     return r

# a=1
# def partation(l, r,a):
    
    
#     if l<r:
        
#         pivot_index = quick_sort(l,r)
#         a+=partation(l,pivot_index-1,a)
#         a+=partation(pivot_index+1, r,a)
#     return a
# b= partation(0,len(arra)-1,a)
# print(b)
# print(arra)


a={1:2,3:4,5:6,7:8}
for x in a:
    print(x)