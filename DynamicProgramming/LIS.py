def lengthOfLIS(self, nums: List[int]) -> int:
    if not nums:
        return 0
    m = len(nums)
    dpArray = [1]*m
    for i in range(1,m):
        for j in range(i):
            if (nums[j] < nums[i]):
                dpArray[i] = max(dpArray[j]+1, dpArray[i])
    return(max(dpArray))
