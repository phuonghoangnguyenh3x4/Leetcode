class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for s in strs:
            count = Counter(s)
            hash[frozenset(count.items())].append(s)
        return list(hash.values())
