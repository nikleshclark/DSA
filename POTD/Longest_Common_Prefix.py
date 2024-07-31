# Longest Common Prefix of Strings

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        # Start with the first string as the initial prefix
        prefix = arr[0]
        
        for string in arr[1:]:
            # Update the prefix to match the current string
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return "-1"
        
        return prefix if prefix else "-1"

print(Solution().longestCommonPrefix(["flower","flow","flight"]))
# Time complexity: O(n * m)
# Space complexity: O(1)
# Approach: Start with the first string as the initial prefix and update the prefix to match the current string. If the prefix becomes empty, return
# "-1". Return the final prefix.