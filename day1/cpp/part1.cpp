#include <fstream>
#include <iostream>

using namespace std;

int main() {
    ifstream f("input.txt");
    string s;
    int sum{};
    int mx{};
    while (getline(f, s)) {
        if (s != "") {
            sum += stoi(s);
            if (sum > mx)
                mx = sum;
        } else
            sum = 0;
    }
    cout << mx << endl;
    f.close();
}