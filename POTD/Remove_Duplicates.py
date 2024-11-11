# Write a program to remove duplicates from a string
class Solution:
    def removeDups(self, str):
        # code here
        string = ""
        hmap = {}
        for i in str:
            if(i in hmap):
                continue
            else:
                string += i
                hmap[i] = 1
        return string

print(Solution().removeDups("geeksforgeeks"))
# Time Complexity: O(N)
# Space Complexity: O(N)
# N = Length of the string

