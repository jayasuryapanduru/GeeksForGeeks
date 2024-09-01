//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
// User function template for C++
#include <algorithm>
class Solution {
  public:
    int findKRotation(vector<int> &arr) {
        // Code Here
        int ind=1;
        bool sort = is_sorted(arr.begin(),arr.end());
        if (sort)
        {
            return 0;
        }
        int a  = *max_element(arr.begin(),arr.end());
         for (int i=0;arr[i]!=a;i++)
         {
             ind++;
         }
        // cout << ind << endl;
         int c=0;
       
       for (int j = ind;j<arr.size();j++)
       {
           c++;
       }
       return arr.size()-c;
    }
    
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input1;
        getline(cin, input1);
        stringstream ss1(input1);
        int number1;
        while (ss1 >> number1) {
            arr.push_back(number1);
        }
        Solution ob;
        int res = ob.findKRotation(arr);
        cout << res << endl;
    }
}
// } Driver Code Ends