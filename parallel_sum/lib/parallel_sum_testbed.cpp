#include <iostream>
#include "parallel_sum.hpp"

using namespace std;


int main(int argc, char const* argv[]) {
    int x = demo_parallel_sum();
    cout << "sum=" << x << endl;
    return 0;
}
