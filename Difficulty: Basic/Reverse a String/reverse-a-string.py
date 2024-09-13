#User function Template for python3
class Solution:
    def revStr (self, s : str) -> str :
        # code here 
        a = list(s)
        a.reverse()
        b = ""
        for i in a:
            b+=i
        return b


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        s = input()
        
        ob = Solution()
        print(ob.revStr(s))
# } Driver Code Ends