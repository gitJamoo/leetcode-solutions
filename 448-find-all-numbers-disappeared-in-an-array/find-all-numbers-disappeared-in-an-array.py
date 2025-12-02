class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set()
        missingArray = []

        for _, number in enumerate(nums):
            nums_set.add(number)

        for i in range(1, len(nums)+1):
            if i not in nums_set:
                missingArray.append(i)
            
        return missingArray