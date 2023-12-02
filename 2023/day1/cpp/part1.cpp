#include <ranges>
#include <string>
#include <chrono>
#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <utility>

using namespace std;

int main() {
    ifstream file("../input.txt");
    string s;
    int acc{};

    while (file >> s) {
        string temp;
        int l = 0, r = s.length() - 1;
        while (!isdigit(s[l]) && l < r) ++l;
        while (!isdigit(s[r]) && r > 0) --r;
        temp += s[l];
        temp += s[r];
        acc += stoi(temp); 
    }

    cout << acc << endl;
    return 0;
}
