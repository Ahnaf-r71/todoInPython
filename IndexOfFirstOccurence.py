# leetcode vv
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         index = haystack.find(needle)
#         if index!=-1:
#             return index
#         else:
#             return -1

        
#incase of needle being a substring of a string
def find_first_index(haystack, needle):
    for index in range(len(haystack)):
        if haystack[index:index + len(needle)] == needle:
            return index  
    return -1  


haystack = "substacksub"
needle = "sub"
result = find_first_index(haystack, needle)
print(result)  


# incase of input being a list
def find_first_index(haystack, needle):
    for index, found in enumerate(haystack):
        if needle == found:
            return index  # Return the index of the first occurrence
    return -1  # Return -1 if the needle is not found

# Example usage
haystack = ["a", "b", "c", "d", "b"]
needle = "b"
result = find_first_index(haystack, needle)
print(result)  # Output: 1