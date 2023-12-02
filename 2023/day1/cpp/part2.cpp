#include <ranges>
#include <string>
#include <chrono>
#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <utility>

using namespace std;

unordered_map<string, string> m{
    {"one", "1"}, {"two", "2"}, {"three", "3"}, {"four", "4"}, {"five", "5"},
    {"six", "6"}, {"seven", "7"}, {"eight", "8"}, {"nine", "9"}
};

const vector<std::string> numberWords = {
    "zero", "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine"
};

pair<size_t, std::string> find_pos(const string& str) {
    size_t pos = string::npos;
    string ret;
    for (const auto& word: numberWords) {
        const size_t curr = str.find(word);
        if (curr != string::npos && curr < pos) {
            pos = curr;
            ret = word;
        }
    }

    return {pos, ret};
}

pair<size_t, std::string> find_rev(const string& str) {
    size_t pos = 0;
    int actual = -1;
    string ret;
    for (auto& numberWord: ranges::reverse_view(numberWords)) {
        const size_t curr = str.rfind(numberWord);
        if (curr != string::npos && (int) curr > actual) {
            actual = curr;
            ret = numberWord;
        }
    }
    actual > -1 ? pos = actual : pos = string::npos;
    return {pos, ret}; 
}

int main() {
    ifstream file("../input.txt");
    string s;
    int acc{};

    while (file >> s) {
        string temp;
        int l = 0, r = s.length() - 1;
        while (!isdigit(s[l]) && l < r) ++l;
        while (!isdigit(s[r]) && r > 0) --r;
        auto [left_index, left_word] = find_pos(s);
        auto [right_index, right_word] = find_rev(s);
        if (left_index != string::npos) {
            l < left_index ? temp += s[l] : temp += m[left_word];
        } else {
            temp += s[l];
        }
        if (right_index != string::npos) {
            r > right_index ? temp += s[r] : temp += m[right_word];
        } else {
            temp += s[r];
        }
        acc += stoi(temp);
    }
    cout << acc << endl;
    return 0;
}
