class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            ans += f"{len(s)}#{s}"
        return ans

    def decode(self, s: str) -> List[str]:      
        i = 0
        ans = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            n = int(s[i:j])
            ans.append(s[j+1:j + n + 1])
            i = j + n + 1
        return ans
