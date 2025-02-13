class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        i=0
        for j in range (0,len(nums)):

            if val != nums[j]:
                count =count+1
                j=j+1
                
        while i<len(nums):
            if nums[i]==val:
                nums.pop(i)
            else:
                i=i+1

            
        # print(nums)
        # print(count)
        return count
