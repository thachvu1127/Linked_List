class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        current = self.head
        while current != None:
            print(current.val)
            current = current.next


    def insertBeg(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            # we assign the "next" attribute of the new node to point to the previous first node
            node.next = self.head
            # this code assigns the new head attribute to now the new node we just created
            self.head = node

    def insertEnd(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node



    def insertBetween(self, prev_node, value):
        if prev_node is None:
            return
        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node


    def removenode(self, key):
        cur_node = self.head

        if cur_node is not None:
            if cur_node.val == key: # if head node itself holds the key to be deleted
                self.head = cur_node.next # setting the head to be the next element since the previous head
                                          # node contains the key to be deleted
                cur_node = None #freeing up the head node which contains the key to be deleted
                return
        prev = None
        while cur_node and cur_node.val != key:
            prev = cur_node
            cur_node = cur_node.next # this line allows us to loop through the linked list

        if cur_node == None: # this line means that we went through the entire list and did not fine any nodes that contains the data that matches up with the key to be deleted
            return

        prev.next = cur_node.next # this step allows A to skip over B and points to C
        cur_node = None


    def DeleteAtPosition(self, position):
        cur_node = self.head
        if position == 0:
            self.head = cur_node.next
            cur_node = None
            return
        i = 1 # set it equal to 1 since we already took care of cases where position = 0
        while i != position and cur_node:
            prev = cur_node
            cur_node = cur_node.next
            i += 1

        if cur_node is None:
            return
        
        prev.next = cur_node.next
        cur_node = None

    def swap(self, key1, key2):
        if key1 == key2:
            return
        prev1 = None
        cur1 = self.head
        while cur1 and cur1.val != key1:
            prev1 = cur1
            cur1 = cur1.next

        prev2 = None
        cur2 = self.head
        while cur2 and cur2.val != key2:
            prev2 = cur2
            cur2 = cur2.next

        if not cur1 or not cur2:
            return

        if prev1:
            prev1.next = cur2
        else:
            self.head = cur2

        if prev2:
            prev2.next = cur1
        else:
            self.head = cur1

        cur1.next, cur2.next = cur2.next, cur1.next

# list = SLinkedList()
# list.insertBeg("A")
# list.insertEnd("B")
# list.insertEnd("C")
# list.insertEnd("D")
# list.swap("E", "E")
#
#
# list.listprint()


class Queues:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        new_node = Node(val)

        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = self.head = new_node


    def dequeue(self):
        if self.head is None:
            return
        val_deleted = self.head.val
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return val_deleted

    def display(self):
        cur = self.head
        if cur is None:
            print("Queue is empty")
        while cur:
            print(cur.val)
            cur = cur.next

    def peek(self):
        if self.head is None:
            return
        return self.head.val








""" 
1) Since each node contains a data and a reference point(link) to the next node in sequence, it allows for dynamic memory allocation and efficient insertion and deletion operations
2) LL is a linear data structure in which elements are not stored at a contiguous location
3) Doubly linked list allows for traversal in both forward and backward directions, but requires additional memory


Advantages of LL:
1) Dynamic Size: LL can grow or shrink dynamically, as memory allocation is done at runtime
2) Insertion and Deletion is efficient
3) Flexibility LL can be easily reorganized and modified without requiring a contiguous block of memory


Disadvantages of LL:
1) Random Access: LL do not allow direct access to elements by index, traversal is required to reach a specific node
2) Extra memory: LL require additional memory for storing the pointer



INSERT AT BEGINNING
- Make the first node of LL linked to the new node
- Remove the head from the original first node 
- Make the new node as the head of the LL
O(1)


INSERT AFTER A GIVEN NODE
- Check if the given node exists of not
    - if it do not exist, terminate the process
    - if given node exists
        - make the element to be inserted as a new node
        - change the next pointer of given node to the new node
        - shift the original next pointer of given node to the next pointer of new node
O(1) since prev_node is given as argument in a method, no need to iterate over list to find prev_node


INSERT AT END
- Go to the last node of LL
- Change the next pointer of last node from NULL to new node
- Make the next pointer of new node as NULL
O(N) since there is a loop from head to end
- This can be O(1) by keeping an extra pointer to the tail of linked list
"""

# comment to delete through another branch