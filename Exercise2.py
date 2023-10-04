from collections import defaultdict


hasmap = defaultdict(list)
a = [1,2,3,4,1,2,3,4,12,3,5]
for x in a:
    hasmap[a].append("Hello")
print(len(hasmap))
