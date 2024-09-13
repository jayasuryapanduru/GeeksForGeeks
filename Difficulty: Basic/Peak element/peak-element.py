# your task is to complete this function
# function should return index to the any valid peak element
class Solution:
    def peakElement(self, arr, n):
        # Edge cases
        if n == 1:
            return 0
        if n == 2:
            return 0 if arr[0] > arr[1] else 1
        
        l, h = 0, n - 1
        while l <= h:
            mid = (l + h) // 2
            
            # Check if mid is a peak element
            if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == n - 1 or arr[mid] >= arr[mid + 1]):
                return mid
            # If mid is not a peak and left neighbor is greater, move to the left half
            elif mid > 0 and arr[mid] < arr[mid - 1]:
                h = mid - 1
            # If mid is not a peak and right neighbor is greater, move to the right half
            else:
                l = mid + 1
        
        return -1



#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends