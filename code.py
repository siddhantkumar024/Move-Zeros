class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        nz=0
        for i in range(n):
            if nums[i]!=0:
                nums[nz]=nums[i]
                nz+=1
        for i in range(nz,n):
            nums[i]=0
            
        
