class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        for i, n in enumerate(nums):
            hash[n] = i
        for i, n in enumerate(nums):
            n2 = target - n
            if n2 in hash and hash[n2] != i:
                return [i, hash[n2]]
        
