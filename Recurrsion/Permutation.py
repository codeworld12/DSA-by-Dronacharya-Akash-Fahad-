class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            
        def fun(i):
            if i == len(nums) - 1:
                res.append(nums[:])
                return
            
            for j in range(i, len(nums)):
                swap(i, j)
                fun(i+1)
                swap(i, j)
        fun(0)
        return res
        
        