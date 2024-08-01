class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix):
        # code here
        top,left = 0, 0
        bottom, right = len(matrix)-1, len(matrix[0])-1
        result = []
        while top <= bottom and left <= right:
            # Traverse from left to right along the top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            # Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                # Traverse from right to left along the bottom row
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                # Traverse from bottom to top along the left column
                for i in range(bottom, top - 1 , -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result

print(Solution().spirallyTraverse([[1,2,3],[4,5,6],[7,8,9]]))
# Time Complexity: O(N*M)
# Space Complexity: O(N*M)
# Approach: Traverse the matrix in a spiral manner. Keep track of the top, bottom, left and right boundaries of the matrix.
# Traverse along the top row, right column, bottom row and left column in a spiral manner.