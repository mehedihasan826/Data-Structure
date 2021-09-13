class Node:
    def __init__(self,data):
        self.data= data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head= None

    def push(self,data):
        new_node= Node(data)
        if self.head == None:
            self.head = new_node
            return

        last_node=self.head
        while(last_node.next):
            last_node=last_node.next
        last_node.next= new_node

    def firstnode(self, data):
        new_node = Node(data)

        new_node.next=self.head
        self.head= new_node

    def InNode(self,previous_data,data):
        if self.head==None:
            print('Node is empty')
            return
        new_node = Node(data)
        new_node.next = previous_data.next
        previous_data.next= new_node

    def printlist(self):
        temp=self.head
        while (temp):
            print(temp.data),
            temp=temp.next

    def len(self):
        check=self.head
        a=0
        while(check):
            a= a+1
            check=check.next
        return a


if __name__ == '__main__':
    my_list= LinkedList()

    #my_list.InNode(7,10) 
    my_list.push(5)
    my_list.push(10)
    my_list.firstnode(4)
    my_list.push(20)
    my_list.InNode(my_list.head.next,15)
    my_list.InNode(my_list.head.next,3)
    my_list.push(100)
    my_list.firstnode(1)
    my_list.InNode(my_list.head.next, 50)

    my_list.printlist()


    print("Lenth of the linked list is {}" .format(my_list.len()) )
    
    
    