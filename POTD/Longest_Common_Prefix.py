"""
This module contains the implementation for finding the longest common prefix among a list of strings.
"""

class LongestCommonPrefix:
    """
    A class to represent the process of finding the longest common prefix.
    """

    def longest_common_prefix(self, strs):
        """
        Finds the longest common prefix string amongst an array of strings.
        
        Args:
            strs (List[str]): A list of strings.
        
        Returns:
            str: The longest common prefix.
        """
        if not strs:
            return ""
        
        prefix = strs[0]
        for string in strs[1:]:
            while string[:len(prefix)] != prefix and prefix:
                prefix = prefix[:len(prefix)-1]
            if not prefix:
                break
        return prefix

# Example usage
if __name__ == "__main__":
    lcp = LongestCommonPrefix()
    example_strings = ["flower", "flow", "flight"]
    print(lcp.longest_common_prefix(example_strings))
