#include <fstream>
#include <iostream>
#include <sstream>

using namespace std;

int main() {
    string s;
    ifstream f("../input.txt");
    int count{};
    while (getline(f, s)) {
        stringstream ss(s);
        int a, b, c, d;
        char x;
        ss >> a >> x >> b >> x >> c >> x >> d;
        if (a <= d && b >= c)
            ++count;
        else if (c <= b && d >= a)
            ++count;
    }
    cout << count << endl;
}
