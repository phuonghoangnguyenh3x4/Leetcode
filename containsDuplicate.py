def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    isVisited = set()
    for n in nums:
        if n in isVisited:
            return True
        isVisited.add(n)
    return False
