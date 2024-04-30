class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        mark = [0] * len(nums)
        # print(haf)
        def fun(i, haf = []):
            if len(haf) == len(nums):
                if haf not in res:
                    res.append(haf[:])
                    return
            for j in range(len(nums)):
                if mark[j] != 1:
                    haf.append(nums[j])
                    mark[j] = 1
                    fun(j+1, haf)
                    haf.pop()
                    mark[j] = 0
            return res

        return fun(0)
        