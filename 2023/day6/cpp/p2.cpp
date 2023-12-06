#include <iostream>

using namespace std;

int main() {
    unsigned long long time = 40709879;
    unsigned long long score = 215105121471005;
    unsigned int speed = 1;
    int total = 0;
    while (speed < time) {
        unsigned long long distance = speed * (time - speed);
        if (distance > score)
            ++total;
        ++speed;
    }
    cout << total << endl;
}
