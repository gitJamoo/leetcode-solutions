from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Use a set for O(1) average time complexity membership checking
        num_set = set()
        duplicate = -1
        
        # 1. Find the duplicate
        for num in nums:
            if num in num_set:
                duplicate = num
            num_set.add(num)
            
        # 2. Find the missing number using summation
        
        # The sum of numbers from 1 to n (if no errors)
        # Formula for sum of an arithmetic series: n * (n + 1) / 2
        expected_sum = n * (n + 1) // 2
        
        # The actual sum of the numbers in the list
        actual_sum = sum(nums)
        
        # The difference between the expected sum and the actual sum is 
        # (Missing Number) - (Duplicate Number)
        # (1 + 2 + ... + N) - (Actual Sum) = Missing - Duplicate
        missing = expected_sum - actual_sum + duplicate
        
        return [duplicate, missing]