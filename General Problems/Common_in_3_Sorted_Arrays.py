class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        hmap = {}
        result = []
        i,j,k = len(arr1),len(arr2),len(arr3)
        left,right = 0,0
        while(left<i and right<j):
            if(arr1[left]==arr2[right]):
                hmap[arr1[left]] = 1
                left += 1
                right += 1
            elif(arr1[left]<arr2[right]):
                left += 1
            else:
                right += 1
        left,right = 0,0
        while(left<j and right<k):
            if(arr2[left]==arr3[right] and arr2[left] in hmap):
                hmap[arr2[left]] = 2
                left += 1
                right += 1
            elif(arr2[left]<arr3[right]):
                left += 1
            else:
                right += 1
        for i in arr1:
            
            if(i in hmap and hmap[i]==2):
                result.append(i)
                hmap[i]= 0
        return [i for i in result] if len(result) > 0 else [-1]
    
# Time complexity: O(n)
# Space complexity: O(n)
# Approach: Use two pointer approach to find the common elements in 3 sorted arrays.
# n is length of all 3 arrays.