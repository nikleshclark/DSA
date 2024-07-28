#User function Template for python3
class Solution:

    def rowWithMax1s(self,arr):
        # code here
        def firstOccurance(arr):
            low , high = 0, len(arr)-1
            while(low<=high):
                mid = (low + high)//2
                if((arr[mid]==1 and arr[mid-1]!=1) or (mid==0 and arr[mid]==1)):
                    return mid
                elif(arr[mid]==1 and arr[mid-1]==1):
                    high = mid-1
                else:
                    low = mid+1
            return len(arr)
        res,index,n = 0,-1, len(arr[0])  
        
        for i in range(len(arr)):
            count = n-firstOccurance(arr[i])
            if(count>res):
                res = count
                index = i
        
        return index
print( Solution().rowWithMax1s([[0, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]])   )
            
## Time Complexity: O(nlogm)
## Space Complexity: O(1)
## Author: Niklesh Nallapaneni