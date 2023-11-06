class Node: 
    def __init__(self, data):
        self.data = data 
        self.right_child = None 
        self.left_child = None 


n1 = Node(10)

n2 = Node(6)
n3 = Node(15)

n4 = Node(4)
n5 = Node(8)
n6 = Node(12)
n7 = Node(17)

n8 = Node(3)
n9 = Node(5)
n10 = Node(7)
n11 = Node(9)
n12 = Node(16)
n13 = Node(18)


n1.left_child = n2
n1.right_child = n3

n2.left_child = n4 
n2.right_child = n5

n3.left_child = n6 
n3.right_child = n7

n4.left_child = n8 
n4.right_child = n9

n5.left_child = n10 
n5.right_child = n11


n7.left_child = n12
n7.right_child = n13





