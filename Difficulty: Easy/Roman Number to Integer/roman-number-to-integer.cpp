//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++
#include<unordered_map>
class Solution {
  public:
    int romanToDecimal(string &str) {
        // code here
        unordered_map<char,int>res
        {
            {'I',1},
            {'V',5},
            {'X',10},
            {'L',50},
            {'C',100},
            {'D',500},
            {'M',1000},
        };
        int total= 0;
        for (int i=0;i<str.size();i++)
        {
            if (i + 1 < str.length() && res[str[i]] < res[str[i + 1]]) {
            total -= res[str[i]];
        } else {
            total += res[str[i]];
        }
        }
        return total;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        Solution ob;
        cout << ob.romanToDecimal(s) << endl;
    }
}
// } Driver Code Ends