# leetcode 19
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
i = 0
listDict = {}
l = head
while l != None:
    listDict[i] = l
    l = l.next
    i += 1
listDict[i] = None
if i == n:
    return head.next
listDict[i - n - 1].next = listDict[i - n + 1]
return head
