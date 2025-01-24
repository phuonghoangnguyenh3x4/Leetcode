class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        
        bucket = [[] for i in range(len(nums))]
        for n, cnt in freq.items():
            bucket[cnt - 1].append(n)
        ans = []
        for i in range(len(nums) - 1, -1, -1):
            for n in bucket[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
