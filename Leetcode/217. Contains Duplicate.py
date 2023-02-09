"""Given an integer array nums, return true if any value appears at least twice in the array,
 and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109"""


# Solution
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))


""" This solution uses the built-in set data structure to check for duplicates in the input list.


Here's how it works:

- set(nums) creates a new set from the input list nums. This set only contains unique elements from nums.

- len(nums) != len(set(nums)) then checks if the length of the input list nums is equal to the length of the set created
 from nums. If the lengths are not equal, it means that there were duplicate in the input list, and the function
  returns True.

-If the lengths are equal, it means there were no duplicates, and the function returns False.

This solution has a time complexity of O(n) where n is the number of elements in the input list nums.
"""