#User function Template for python3
from collections import Counter

def isSubset(a1, a2, n, m):
    # Create counters for both arrays
    a1_counter = Counter(a1)
    a2_counter = Counter(a2)
    
    # Check if each element in a2 is present in a1 with at least the same frequency
    for element in a2_counter:
        if a2_counter[element] > a1_counter[element]:
            return "No"
    
    return "Yes"


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends