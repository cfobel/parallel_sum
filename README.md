Overview
========

This package demonstrates the usage of [Thrust][1] for reduction sum.

__NB__ While originally developed for [CUDA][2], Thrust can be used on a system
without CUDA, by compiling with one of the [OpenMP][3] or [_Threading Building
Blocks (TBB)_][4] [backends][5].


Build
=====

To build the Thrust `parallel_sum` example object, from within the
`parallel_sum/lib` directory, run:

    icc -fast -o parallel_sum.o -c parallel_sum.cpp -DTHRUST_DEVICE_SYSTEM=THRUST_DEVICE_SYSTEM_OMP -openmp -lpthread -lgomp -static-intel

To build the Cython extension, from the root of the repository, run:

    CC="icc -static-intel -fast -vec-report" CXX=icc CFLAGS="-g" python setup.py build_ext


[1]: https://github.com/thrust/thrust
[2]: http://en.wikipedia.org/wiki/CUDA
[3]: http://openmp.org/wp
[4]: http://en.wikipedia.org/wiki/Threading_Building_Blocks
[5]: https://github.com/thrust/thrust/wiki/Device-Backends
