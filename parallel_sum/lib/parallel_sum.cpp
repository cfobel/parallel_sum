#include <thrust/host_vector.h>
#include <thrust/device_vector.h>
#include <thrust/generate.h>
#include <thrust/reduce.h>
#include <thrust/functional.h>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;


extern "C"
int demo_parallel_sum(void) {
    // generate random data serially
    //thrust::host_vector<int> h_vec(100);
    std::vector<int> h_vec(100);
    std::generate(h_vec.begin(), h_vec.end(), rand);

    // transfer to device and compute sum
    thrust::device_vector<int> d_vec = h_vec;
    return thrust::reduce(d_vec.begin(), d_vec.end(), 0, thrust::plus<int>());
}
