# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        node1 = self.head
        i = 0
        while node1.next_node:
            j = 0
            node2 = self.head
            if node1.value % 2 != 0:    ##if odd
                pass
            else:   ##if find even
                for k in range(i + 1):  ##from next value
                    j += 1
                    node2 = node2.next_node   
                while node2:
                    if node2.value % 2 == 0:    ##if even
                        pass
                    else:   ##if find odd
                        odd = node2.value
                        for p in range(j - i):
                            node3 = self.head
                            node4 = self.head
                            
                            for m in range(j - p - 1):
                                node4 = node4.next_node
                            former = node4.value
                            
                            for n in range(j - p):
                                node3 = node3.next_node
                            node3.value = former    ##later one = former one
                            
                        node1.value = odd   ##change into odd
                        break
                        
                    j += 1
                    node2 = node2.next_node

            i += 1
            node1 = node1.next_node

    
    
    
