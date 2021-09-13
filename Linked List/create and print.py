class Node:
    def __init__(self, data):
        self.data= data
        self.next = None

class Linkedlist:
    def __init__(self):
        
        self.head= None

    def PrintList(self):
        temp= self.head
        while(temp):
            print(temp.data)
            temp=temp.next

if __name__ == '__main__' :
    my_list= Linkedlist()

    my_list.head= Node(1)
    second= Node(2)
    third= Node(3)

    my_list.head.next= second 
    second.next= third


    my_list.PrintList()
