"""
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curr = head
        lst=[]
        while curr:
            lst.append(curr.val)
            curr = curr.next
        if lst == lst[::-1]:
            return True
        else:
            return False