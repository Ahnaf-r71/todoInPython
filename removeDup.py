def removeDuplicates(nums):
    if not nums:
        return 0  
    
    i = 0  

    for j in range(1, len(nums)):  
        if nums[j] != nums[i]:  # Found a new unique element
            i += 1  # Move forward
            nums[i] = nums[j]  # Update the next unique position

    return i + 1  # counting

# Example Usage
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = removeDuplicates(nums)
print(k, nums[:k])


# # incase i=1 as always keep the first number
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         i = 1

#         for j in range(1, len(nums)):
#             if nums[j] != nums[i - 1]:
#                 nums[i] = nums[j]
#                 i += 1
        
#         return i