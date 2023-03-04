class Node:
    def __init__(self,name,link):
        self.name=name
        self.next=link
    def __str__(self):
        return self.name
node3=Node('node3',None)
node2=Node('node2',node3)
node1=Node('node1',node2)
s=node1
for i in range(3):
    print(s)
    s=s.next