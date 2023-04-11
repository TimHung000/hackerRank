#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

struct node
{
    vector<int> index;
    vector<int> value;
    node* next[26];
};

class score_tree
{
public:
    node* root;
public:
    score_tree(vector<string>& genes, vector<int>& helth)
    {
        root = new node();
        for(int i = 0; i < genes.size(); ++i)
        {
            string gene = genes[i];
            node* current = root;
            for(int j = 0; j < gene.size(); ++j)
            {
                char c = gene[j];
                if(current->next[c-'a'] == NULL)
                    current->next[c-'a'] = new node();
                current = current->next[c-'a'];

                if(j == gene.size()-1)
                {
                    current->index.push_back(i);
                    current->value.push_back(helth[i]);
                }
            }
        }
    }
    long calculate_score(string& strand, int start, int end)
    {
        node* curNode;
        long score = 0;
        for(int i = 0; i < strand.size(); ++i)
        {
            int cur = i;
            curNode = root;
            while(cur < strand.size() && curNode->next[strand[cur]-'a'])
            {
                curNode = curNode->next[strand[cur]-'a'];
                // add value
                for(int j = 0; j < curNode->index.size(); ++j)
                {
                    if(curNode->index[j] >= start && curNode->index[j] <= end)
                        score += curNode->value[j];
                }
                ++cur;
            }
        }
        return score;
    }

    void deleteNode(node* curr)
    {
        for(int i = 0; i < 26; ++i)
        {
            if(curr->next[i])
                deleteNode(curr->next[i]);
        }
        delete curr;
    }

    ~score_tree()
    {
        if(root)
            deleteNode(root);
    }
};



void determineDNAHealth(vector<tuple<string, int, int>>& strands, vector<string>& genes, vector<int>& health_map)
{
    score_tree tree = score_tree(genes, health_map);
    long minScore = LONG_MAX;
    long maxScore = LONG_MIN;
    long curScore = 0;
    for(int i = 0; i < strands.size(); ++i)
    {
        curScore = tree.calculate_score(get<0>(strands[i]), get<1>(strands[i]), get<2>(strands[i]));
        if(curScore > maxScore)
        {
            maxScore = curScore;
        }
        if(curScore < minScore)
        {
            minScore = curScore;
        }

    }

    cout << minScore << " " << maxScore;
}


int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string genes_temp_temp;
    getline(cin, genes_temp_temp);

    vector<string> genes_temp = split(rtrim(genes_temp_temp));

    vector<string> genes(n);

    for (int i = 0; i < n; i++) {
        string genes_item = genes_temp[i];

        genes[i] = genes_item;
    }

    string health_temp_temp;
    getline(cin, health_temp_temp);

    vector<string> health_temp = split(rtrim(health_temp_temp));

    vector<int> health(n);

    for (int i = 0; i < n; i++) {
        int health_item = stoi(health_temp[i]);

        health[i] = health_item;
    }

    string s_temp;
    getline(cin, s_temp);

    int s = stoi(ltrim(rtrim(s_temp)));
    vector<tuple<string, int, int>> strands;
    vector<int> strandHealth(s, 0);
    for (int s_itr = 0; s_itr < s; s_itr++) {
        string first_multiple_input_temp;
        getline(cin, first_multiple_input_temp);

        vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

        int first = stoi(first_multiple_input[0]);

        int last = stoi(first_multiple_input[1]);

        string d = first_multiple_input[2];
        strands.push_back(make_tuple(d, first, last));
    }

    determineDNAHealth(strands, genes, health);
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
