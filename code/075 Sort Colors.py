class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i,j=0,0
        for k in range(len(nums)):
            tmp=nums[k]
            nums[k]=2
            if tmp<2:
                nums[j]=1
                j+=1
            if tmp==0:
                nums[i]=0
                i+=1