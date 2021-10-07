# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # get the first values of v1 et v2
        value1 = l1.val
        nextvalue1 = l1.next
        value2 = l2.val
        nextvalue2 = l2.next
        
        # initialize 2 listes which contains only values from l1 and l2
        list1 = [value1]
        list2 = [value2]

        while nextvalue1 != None:
            list1.append(nextvalue1.val)
            nextvalue1 = nextvalue1.next
            
        while nextvalue2 != None:
            list2.append(nextvalue2.val)
            nextvalue2 = nextvalue2.next
        
        # get lenth of the two lists
        len1 = len(list1)
        len2 = len(list2)
        
        # we want to have to equal list so we can add values
        if len1 > len2:
            diff = len1 - len2
            list2.extend([0] * diff)
        elif len2 > len1:
            diff = len2 - len1
            list1.extend([0] * diff)
            
        
        # add values and stored in list3
        list3 = list(map(lambda x,y: x+y, list1, list2))

        
        retenu = 0
        for i in range(len(list3)):
            list3[i] += retenu
            retenu = 0
            if len(str(list3[i])) > 1:
                retenu = int(str(list3[i])[0])
                list3[i] = int(str(list3[i])[1])
                
        if retenu != 0:
            list3.append(retenu)
                
        output = ListNode(list3[-1])
        list3.pop()
        
        for ind, _ in enumerate(list3, 1):
            output = ListNode(list3[-ind], next=output)
            
        return(output)
                
        
        
