// search_tool.cpp
#include <bits/stdc++.h>
using namespace std;

string lower(string s)
{
    for (char &c : s)
        c = tolower(c);
    return s;
}

int main(int argc, char **argv)
{
    if (argc < 3)
        return 0;
    string filepath = argv[1];
    string query = argv[2];
    for (int i = 3; i < argc; i++)
    {
        query += " ";
        query += argv[i];
    } // allow multi-word
    string ql = lower(query);

    ifstream fin(filepath);
    if (!fin.is_open())
        return 0;
    string line;
    while (getline(fin, line))
    {
        string orig = line;
        string name;
        stringstream ss(line);
        getline(ss, name, ',');
        if (lower(name).find(ql) != string::npos)
        {
            // print normalized record
            cout << orig << "\\n";
        }
    }
    fin.close();
    return 0;
}