import random
import sys

class Node:
    def __init__(self,data,next = None):
        self.mem = random.random()
        self.data = data
        self.next = next

    def __str__(self):
        return f'<{self.data},{self.next:.2f}>'

num_of_list = int(input())
list_of_num = list(map(int , input().split()))
pos_that_last_point_to = int(input())

if(pos_that_last_point_to < 1 or pos_that_last_point_to > num_of_list - 1):
    print(False)
    sys.exit()


NodeList = []
# Creating nodes
for i in range(num_of_list):
    NodeList.append(Node(list_of_num[i]))

# creating links
for i in range(1,num_of_list-1):
    NodeList[i-1].next = NodeList[i].mem
    if i == num_of_list-1:
        NodeList[i].next = NodeList[pos_that_last_point_to + 1].mem

