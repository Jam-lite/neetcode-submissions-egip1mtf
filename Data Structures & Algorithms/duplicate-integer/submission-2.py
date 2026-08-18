class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_counter = set()

        for num in nums:
            set_counter.add(num)
        
        if len(set_counter) == len(nums):
            return False
        else:
            return True
        