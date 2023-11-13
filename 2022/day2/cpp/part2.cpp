#include <fstream>
#include <iostream>

using namespace std;

int main() {
    char x, z;
    int score{};
    ifstream f("input.txt");
    while (f >> x) {
        f >> z;
        if (z == 'X') {
            if (x == 'A')
                score += 3;
            if (x == 'B')
                score += 1;
            if (x == 'C')
                score += 2;
        }
        if (z == 'Y') {
            if (x == 'A')
                score += 4;
            if (x == 'B')
                score += 5;
            if (x == 'C')
                score += 6;
        }
        if (z == 'Z') {
            if (x == 'A')
                score += 8;
            if (x == 'B')
                score += 9;
            if (x == 'C')
                score += 7;
        }
    }
    cout << score << endl;
}