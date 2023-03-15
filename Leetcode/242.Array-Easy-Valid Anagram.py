from collections import Counter


"""


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
# Solution
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


# Solution
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)

"""
Time Complexity:

The time complexity of this solution is O(n log n), where n is the length of the longer string. This is because we sort 
both strings, which has an average time complexity of O(n log n).
Space Complexity:

The space complexity of this solution is O(n), where n is the length of the longer string. This is because we create 
two sorted versions of the strings, which both require O(n) space.
"""