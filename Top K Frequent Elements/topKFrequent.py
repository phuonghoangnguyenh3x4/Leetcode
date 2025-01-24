class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        
        bucket = [[] for i in range(len(nums))]
        for n, cnt in freq.items():
            bucket[cnt - 1].append(n)
        ans = []
        for i in range(len(nums) - 1, -1, -1):
            j = 0
            while bucket[i] and k > 0 and j < len(bucket[i]):
                ans.append(bucket[i][j])
                j += 1
                k -= 1
        return ans
            
