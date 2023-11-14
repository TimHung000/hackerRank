#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'insertionSort' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */
long long helper(vector<long long>&arr, long long start, long long end)
{
    if(start >= end)
        return 0;
    long long mid = (start + end) / 2;
    long long leftRes = helper(arr, start, mid);
    long long rightRes = helper(arr, mid+1, end);
    long long res = leftRes + rightRes;



    vector<long long> leftArr(arr.begin()+start, arr.begin()+mid+1);    
    vector<long long> rightArr(arr.begin()+mid+1, arr.begin()+end+1);
    long long leftPtr = 0;
    long long rightPtr = 0;
    long long resPtr = start;
    while(leftPtr < leftArr.size() && rightPtr < rightArr.size())
    {
        if(leftArr[leftPtr] <= rightArr[rightPtr])
        {
            arr[resPtr] = leftArr[leftPtr];
            ++leftPtr;
            ++resPtr;
        }
        else
        {
            arr[resPtr] = rightArr[rightPtr];
            res = res + ((rightPtr+mid+1) - resPtr);
            ++rightPtr;
            ++resPtr;
        }
    }

    while(leftPtr < leftArr.size())
        arr[resPtr++] = leftArr[leftPtr++];
    while(rightPtr < rightArr.size())
        arr[resPtr++] = rightArr[rightPtr++];
    return res;
}

long long insertionSort(vector<long long> arr) {

    return helper(arr, 0, arr.size()-1);
}

int main()
{
    // ofstream fout(getenv("OUTPUT_PATH"));

    string t_temp;
    getline(cin, t_temp);

    long long t = stoll(ltrim(rtrim(t_temp)));

    for (long long t_itr = 0; t_itr < t; t_itr++) {
        string n_temp;
        getline(cin, n_temp);

        long long n = stoll(ltrim(rtrim(n_temp)));

        string arr_temp_temp;
        getline(cin, arr_temp_temp);

        vector<string> arr_temp = split(rtrim(arr_temp_temp));

        vector<long long> arr(n);

        for (long long i = 0; i < n; i++) {
            long long arr_item = stoll(arr_temp[i]);

            arr[i] = arr_item;
        }

        long long result = insertionSort(arr);

        cout << result << "\n";
    }

    // fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
