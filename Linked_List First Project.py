import sys

class Node : 
    
    def __init__(self, value) : 
        self.value = value 
        self.next = None 
        
class LinkedList: 
    
    def __init__(self) : 
        self.head = None 
            
# Method to calculate Length of LinkedIn List       
    def get_length(self) : 
        count = 0 
        itr = self.head 
        while itr != None : 
            itr = itr.next 
            count += 1 
        return count 
        
# Method to insert Value  at the Beginning        
    def insert_at_beginning(self,value) : 
        
        new_Node = Node(value)
        new_Node.next = self.head
        self.head = new_Node 

# Method for append Value to Linked List    
    def append(self, value) :        
        if self.head is None : 
            self.head = Node(value)        
        else :       
            itr = self.head            
            while itr.next != None : 
                itr = itr.next 
            itr.next = Node(value)

# Method to insert value at certain Index      
    def insert(self, index, value) : 
        if 0 > index > self.get_length() : 
            raise Exception ("Index is out of Range")
        # Insert Value at the beginning 
        if index == 0 : 
            self.insert_at_beginning(self,value)
               
        count = 0
        itr = self.head
        while itr != None :
            if count == index - 1:
                node = Node(value)
                node.next = itr.next
                itr.next = node
                break

            itr = itr.next
            count += 1

# Method to remove element from Linked List 
# at Certain Index 
    def remove(self, index) : 
        if self.head is None : 
            print ("Linked List is Empty") 
       # remove first element 
        elif index == 0 : 
            self.head = self.head.next
       # remove last element
        elif index == -1 : 
            itr = self.head 
            while itr != None: 
                if itr.next.next == None :                    
                    itr.next = None 
                    break
                itr = itr.next 
       # remove element from certain index
        else : 
            count = 0 
            itr = self.head 
            while itr != None : 
                if count == index -1 : 
                    itr.next = itr.next.next
                itr = itr.next
                count += 1 
                        
# Method to print Values
    def print_values(self) : 
        if self.head is None: 
            print ("Linked List is empty")
        
        itr = self.head 
        llstr = "" 
        
        while itr != None : 
            llstr += str(itr.value) + "•••" if itr.next else str(itr.value)
            itr = itr.next 
        print (llstr)
        print ()
        print ()

# creating instance of Linked List Class                                 
ll = LinkedList () 
"""
for i in range (99,0,-1): 
    ll.insert_at_beginning(i)
    
for x in range (100,201):
    ll.append(x)
"""
def ErrorHandling(): 
    pass

# function for insertion at the beginning 
def insert_at_beginning() :       
    value = input("Enter Value : ")       
    ll.insert_at_beginning(value)

# function for appending values at the end.
def append() :  
    value = input("Enter Value : ")        
    ll.append(value) 

# function for insertion at certain index   
def insert() :    
    index = int (input ("Enter Index : "))
    value = input("Enter Value : ")
         
    ll.insert(index, value)

# Delete first element from Linked List 
def remove_first_element() :
    ll.remove(0)

# Delete last element from linked list
def remove_last_element() :
    ll.remove(-1)

# Delete element from certain index   
def remove_element_index() :  
    index = int (input ("Enter Index : "))
    ll.remove(index)

# Linked List action Dictionary 
lldict = {
     '1' : insert_at_beginning, 
     '2' : append,
     '3' : insert,
     '4' : remove_first_element,
     '5' : remove_last_element,
     '6' : remove_element_index,
  'exit' : sys.exit,
}
# infinite loop begins... :)            
while True : 
    print ("You can enter one of this : \n",
           "    1 : Insert Value at the beginning \n",
           "    2 : Insert Value at the end \n",
           "    3 : Insert element at Certain Index \n",
           "    4 : Remove first Element \n",
           "    5 : Remove Last Element\n",
           "    6 : Remove element at Certain Index\n",
           " exit : Exit The Loop \n",
           "print : Print Linked List")
    print ()
    print ()
    
    action = input("Enter Action : ").lower().strip()
    
    if action in lldict :     
        lldict[action]()
        ll.print_values()
        
    elif action == "Print".lower(): 
        ll.print_values()
        
    else : 
        print ("Invalid Choice")
    
