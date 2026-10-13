class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        PrevMap = {} # val -> index 

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in PrevMap:
                return [PrevMap[diff], i]
            else:
                PrevMap[nums[i]] = i 