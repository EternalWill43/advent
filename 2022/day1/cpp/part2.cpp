#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ifstream f("input.txt");
    string s;
    int sum{};
    vector<int> elves;
    while (getline(f, s)) {
        if (s != "") {
            sum += stoi(s);
        } else {
            elves.push_back(sum);
            sum = 0;
        }
    }
    sort(elves.rbegin(), elves.rend());
    cout << elves[0] + elves[1] + elves[2] << endl;
    f.close();
}