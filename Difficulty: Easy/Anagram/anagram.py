#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
             #Unequal Length strings cannot be anagrams
        if len(a) != len(b):
            return False
        
        #sort the first string
        first = sorted(a)
        #sort the second string
        second = sorted(b)
        
        #check if both the strings are the same
        if first == second:
            return True
        else:
            return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends