#include <iostream>
using namespace std;

bool isPalindrome(int x) {
    if (x < 0) {
        return false;
    }

    int reverse = 0;
    int num = x;

    while (num) {
        int lastdigit = num % 10;
        reverse = reverse * 10 + lastdigit;
        num = num / 10;
    }

    bool hasil = (reverse == x);
    cout << "\nHasil = " << reverse << " || " << x << " -> " << hasil << "\n" << endl;
    return hasil;
}

int main() {
    int x;
    cout << "Masukkan Angka: ";
    cin >> x;
    isPalindrome(x);
    return 0;
}
