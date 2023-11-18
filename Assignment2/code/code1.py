import random 

# 3 CLASS = INTERNAL NODE, LEAF NODE, BPLUSTREES
# LEAF NODE IS DOUBLE LINKED LIST


class InternalNode(object):
    # INTERNAL NODE 
    # HOLDS KEYS AND CHILDREN 
    # CAN HOLD N-1 ORDERE KEY AND CAN HOLD N CHILDREN


    def __init__(self, parent=None):
        # INITIALIZING THE PARAMETERS
        self.keys= []
        self.children= []
        self.parent = parent

    
    def find_index(self, key):

        for i, item in enumerate(self.keys):
            if key < item:
                return i

        return len(self.keys)

    def __getitem__(self, item):
        return self.children[self.find_index(item)]

    def __setitem__(self, key, value):
        i = self.find_index(key)
        self.keys[i:i] = [key]
        self.children.pop(i)
        self.children[i:i] = value

    def splitInternalNode(self):

        left = InternalNode(self.parent)

        mid = len(self.keys) // 2

        left.keys = self.keys[:mid]
        left.children = self.children[:mid + 1]
        for child in left.children:
            child.parent = left

        key = self.keys[mid]
        self.keys = self.keys[mid + 1:]
        self.children = self.children[mid + 1:]

        return key, [left, self]



class LeafNode(InternalNode):
    def __init__(self, parent=None, prev_node=None, next_node=None):
        super(LeafNode, self).__init__(parent)
        self.next: LeafNode = next_node
        if next_node is not None:
            next_node.prev = self
        self.prev: LeafNode = prev_node
        if prev_node is not None:
            prev_node.next = self

    def __getitem__(self, item):
        return self.children[self.keys.index(item)]

    def __setitem__(self, key, value):
        i = self.find_index(key)
        if key not in self.keys:
            self.keys[i:i] = [key]
            self.children[i:i] = [value]
        else:
            self.children[i - 1] = value

    def splitLeafNode(self):

        left = LeafNode(self.parent, self.prev, self)
        mid = len(self.keys) // 2

        left.keys = self.keys[:mid]
        left.children = self.children[:mid]

        self.keys: list = self.keys[mid:]
        self.children: list = self.children[mid:]
        return self.keys[0], [left, self]

class BPlusTree(object):
   

    def __init__(self, maximum):
        self.root = LeafNode()
        self.maximum = maximum
        self.minimum = self.maximum-1 // 2
    

    def findLeafNode(self, key) -> LeafNode:
  
        node = self.root
      
        while type(node) is not LeafNode:
            node = node[key]

        return node

    def __getitem__(self, item):
        return self.find(item)[item]


    def __setitem__(self, key, value, leaf=None):

        if leaf is None:
            leaf = self.findLeafNode(key)
        leaf[key] = value
        if len(leaf.keys) > self.maximum-1:
            self.insert_index(*leaf.splitLeafNode())

    def insert_index(self, key, values: list[InternalNode]):
     
        parent = values[1].parent
        if parent is None:
            values[0].parent = values[1].parent = self.root = InternalNode()
            
            self.root.keys = [key]
            self.root.children = values
            return

        parent[key] = values
       
        if len(parent.keys) > self.maximum-1:
            self.insert_index(*parent.splitInternalNode())
  
       
    def show(self, node=None, _prefix="", _last=True):
        f = open("B+TREE_FOR_AUGUST", "a")
        
        
        if node is None:
            node = self.root
        output_string = f"{_prefix}`- " if _last else f"{_prefix}|-"
        f.write(output_string)
        f.write(str(node.keys)+"\n")
        f.close()
        print(_prefix, "`- " if _last else "|- ", node.keys, sep="")
        _prefix += "   " if _last else "|  "

        if type(node) is InternalNode:

            for i, child in enumerate(node.children):
                _last = (i == len(node.children) - 1)
                self.show(child, _prefix, _last)
        



import csv


def read_csv(filename):
    data = []
    r= open(filename, "r", encoding="ISO-8859-1")
    reader = csv.DictReader(r)
    
    for x in reader:
        data.append(x)
    print(len(data))

    return data
a = read_csv("../../Assignment1/code/VAERS_COVID_DataAugust2023.csv")[0:50]



bplustree = BPlusTree(5)

for i in a:
        bplustree[int(i["VAERS_ID"])] = str(i)
    
bplustree.show()




# ADDING SEPTEMBER DATA IN THE SAME BST


# FOR SEPTEMBER
# b = read_csv("../../Assignment1/code/VAERS_COVID_SEPTEMBER2023.csv")
# for j in b:
#         bplustree[int(j["VAERS_ID"])] = str(j)
# bplustree.show()



# node = bplustree.findLeafNode(902446)
# print(node.children)

# UPTO AUGUST
# 1589965
# ONE MILLION FIVE HUNDRED EIGHTY NINE THOUSAND NINE HUNDRED AND SIXTY FIVE
# SEPTEMBER
# 663048
# 2253013
# Two million two hundred fifty-three thousand thirteen


# n = order
# maxchild = n
# maxkey= n-1
# minchild = n/2 ceil
# minkey = (n/2) ceil - 1