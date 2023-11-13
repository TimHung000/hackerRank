// #include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int isPalindrome(string& s, int leftIndex, int rightIndex) {
    while(leftIndex < rightIndex) {
        if(s[leftIndex] != s[rightIndex])
            return false;
        ++leftIndex;
        --rightIndex;
    }
    return true;
}


int palindromeIndex(string s) {
    int leftPtr = 0;
    int rightPtr = s.size() - 1;
    while(leftPtr <= rightPtr) {
        if(s[leftPtr] != s[rightPtr]) {
            if(isPalindrome(s, leftPtr, rightPtr-1))
                return rightPtr;
            if(isPalindrome(s, leftPtr+1, rightPtr))
                return leftPtr;
        }
        ++leftPtr;
        --rightPtr;
    }
    return -1;
}

int main() {
    int n;
    vector<string> inputs;
    cin >> n;
    for(int i = 0; i < n; ++i) {
        string tmp;
        cin >> tmp;
        inputs.push_back(tmp);
    }
    vector<int> res;
    for(int i = 0; i < n; ++i)
        cout << palindromeIndex(inputs[i]) << "\n";
    return 0;
}