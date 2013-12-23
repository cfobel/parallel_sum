#!/usr/bin/env python
import sys
from distutils.core import setup, Extension
from Cython.Build import cythonize

include_dirs = [] #cyplace.get_includes()
sys.path += include_dirs

cython_config = dict(include_dirs=include_dirs, language='c++',
                     libraries=['rt', 'pthread'],
                     extra_link_args=['-openmp'],
                     extra_compile_args=['-O3', '-std=c++0x', '-openmp',
                                         '-Wfatal-errors'])

cython_exts = [Extension('parallel_sum.%s' % v,
                           ['parallel_sum/%s.pyx' % v],
                           extra_objects=['parallel_sum/lib/%s.o' % lib
                                          for lib in ('parallel_sum', )],
                           **cython_config)
                 for v in ('ParallelSum', )]


setup(name = "parallel_sum",
    version = "0.0.1",
    description = "Thrust/C++ reduction sum, with Cython bindings",
    keywords = "thrust c++ reduction sum cython",
    author = "Christian Fobel",
    url = "https://github.com/cfobel/parallel_sum",
    license = "GPL",
    long_description = '''
This package demonstrates the usage of [Thrust][1] for reduction sum.

__NB__ While originally developed for [CUDA][2], Thrust can be used on a system
without CUDA, by compiling with one of the [OpenMP][3] or [_Threading Building
Blocks (TBB)_][4] [backends][5].

[1]: https://github.com/thrust/thrust
[2]: http://en.wikipedia.org/wiki/CUDA
[3]: http://openmp.org/wp
[4]: http://en.wikipedia.org/wiki/Threading_Building_Blocks
[5]: https://github.com/thrust/thrust/wiki/Device-Backends
      '''.strip(),
    packages = ['parallel_sum', ],
    ext_modules=cythonize(cython_exts,
                          pyrex_directives={'embedsignature': True})
)
