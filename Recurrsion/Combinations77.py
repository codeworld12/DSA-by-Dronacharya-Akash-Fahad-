
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        full = []
        nums=[i for i in range(1, n+1)]

        def fun(i, half):
            
            if len(half) == k:
                full.append(half.copy())
                return 
            if i == len(nums):
                return
            half.append(nums[i])
            fun(i+1, half)
            half.pop()
            return fun(i+1, half)
        fun(0, [])
        return full


        