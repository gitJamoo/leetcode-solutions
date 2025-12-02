class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedArray = sorted(nums)
        answer = []

        print(sortedArray)

        for _, num in enumerate(nums):
            answer.append(sortedArray.index(num))

        return answer