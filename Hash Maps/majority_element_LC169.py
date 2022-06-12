"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2"""

#Time: O(n)
#Space: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numDict = {}
        majorityAppearance = 0
        for num in nums:
            if num not in numDict:
                numDict[num] = 1
            else:
                numDict[num] += 1
        for k in numDict:
            if numDict[k] > majorityAppearance:
                majorityAppearance = numDict[k]
                majorityElement = k
        return majorityElement