class Solution:
    def isPalindrome(self, s):
        newS= [i.lower() for i in s if i.isalnum()]
        return newS == newS[::-1]
    #return newS[:len(newS)/2] == newS[(len(newS)+1)/2:][::-1]  # This one is better, but too longa