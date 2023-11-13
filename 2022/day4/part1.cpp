#include <fstream>
#include <iostream>
#include <sstream>

using namespace std;

int main() {
    string s;
    ifstream f("input.txt");
    int count{};
    while (getline(f, s)) {
        stringstream ss(s);
        int a, b, c, d;
        char x;
        ss >> a >> x >> b >> x >> c >> x >> d;
        if (a >= c && b <= d)
            ++count;
        else if (c >= a && d <= b)
            ++count;
    }
    cout << count << endl;
}