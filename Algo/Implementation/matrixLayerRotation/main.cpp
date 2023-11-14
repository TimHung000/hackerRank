#include <bits/stdc++.h>
#include <functional>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);
void fillCircularIdx(int rowTop, int rowDown, int colLeft, int colRight, vector<pair<int, int>>& circularIdx);
/*
 * Complete the 'matrixRotation' function below.
 *
 * The function accepts following parameters:
 *  1. 2D_INTEGER_ARRAY matrix
 *  2. INTEGER r
 */

void matrixRotation(vector<vector<int>> matrix, int r) {
    vector<vector<int>> res(matrix.size(), vector<int>(matrix[0].size()));
    int rowTop = 0;
    int rowDown = matrix.size()-1;
    int colLeft = 0;
    int colRight = matrix[0].size()-1;
    while(rowDown > rowTop && colRight > colLeft) {
        vector<pair<int, int>> circularIdx;
        fillCircularIdx(rowTop, rowDown, colLeft, colRight, circularIdx);
        for(int i = 0; i < circularIdx.size(); ++i) {
            pair<int, int> current = circularIdx[i];
            pair<int, int> pointTo = circularIdx[(i+r)%circularIdx.size()];
            res[pointTo.first][pointTo.second] = matrix[current.first][current.second];
        }
        ++rowTop;
        --rowDown;
        ++colLeft;
        --colRight;
    }

    for(int i = 0; i < res.size(); ++i) {
        for(int j = 0; j < res[i].size(); ++j) {
            cout << res[i][j] << " ";
        }
        cout << "\n";
    }
}

void fillCircularIdx(int rowTop, int rowDown, int colLeft, int colRight, vector<pair<int, int>>& circularIdx) {
    int curRow = rowTop;
    int curCol = colLeft;
    // traverse down
    while ( curRow <= rowDown) {
        circularIdx.push_back(make_pair(curRow, curCol));
        ++curRow;
    }

    curRow = rowDown;
    curCol = colLeft + 1;
    // traverse  right
    while ( curCol <= colRight ) {
        circularIdx.push_back(make_pair(curRow, curCol));
        ++curCol;
    }

    curRow = rowDown - 1;
    curCol = colRight;
    // traverse up
    while( curRow >= rowTop ) {
        circularIdx.push_back(make_pair(curRow, curCol));
        --curRow;
    }

    curRow = rowTop;
    curCol = colRight - 1;
    // traver left
    while( curCol > colLeft ) {
        circularIdx.push_back(make_pair(curRow, curCol));
        --curCol;
    }
}

int main()
{
    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

    int m = stoi(first_multiple_input[0]);

    int n = stoi(first_multiple_input[1]);

    int r = stoi(first_multiple_input[2]);

    vector<vector<int>> matrix(m);

    for (int i = 0; i < m; i++) {
        matrix[i].resize(n);

        string matrix_row_temp_temp;
        getline(cin, matrix_row_temp_temp);

        vector<string> matrix_row_temp = split(rtrim(matrix_row_temp_temp));

        for (int j = 0; j < n; j++) {
            int matrix_row_item = stoi(matrix_row_temp[j]);

            matrix[i][j] = matrix_row_item;
        }
    }

    matrixRotation(matrix, r);

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
