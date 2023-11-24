#include <fstream>
#include <iostream>

using namespace std;

int main() {
    ifstream f("../input.txt");
    char x, z;
    int score{};
    while (f >> x) {
        f >> z;
        if (z == 'X') {
            ++score;
            if (x == 'A')
                score += 3;
            if (x == 'C')
                score += 6;
        } else if (z == 'Y') {
            score += 2;
            if (x == 'A')
                score += 6;
            if (x == 'B')
                score += 3;
        } else if (z == 'Z') {
            score += 3;
            if (x == 'B')
                score += 6;
            if (x == 'C')
                score += 3;
        }
    }
    cout << score << endl;
}
