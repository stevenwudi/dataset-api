# ======== setup.py ===========
import subprocess
from distutils.core import setup
from distutils.extension import Extension

import numpy
from Cython.Build import cythonize
from Cython.Distutils import build_ext

proc_libs = subprocess.check_output("pkg-config --libs eigen3 egl glew".split())
proc_incs = subprocess.check_output("pkg-config --cflags eigen3 egl glew".split())

libs = [lib.decode('utf-8') for lib in proc_libs.split()]
incs = [inc.decode('utf-8') for inc in proc_incs.split()]

incs_new = []
for inc in incs:
    if '-I' in inc:
        inc = inc[2:]
    incs_new.append(inc)

incs = incs_new
incs = incs + [numpy.get_include()]
libs = libs + ['-lboost_system']

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(Extension("render_egl",
                                    sources=["renderMesh_egl.cpp", "render_egl.pyx"],
                                    language="c++",
                                    include_dirs=incs,
                                    extra_link_args=libs
                                    )
                          )
)
