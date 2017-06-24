from distutils.core import setup, Extension
from Cython.Build import cythonize

ext_modules=[
    Extension("add_wrapper",
              sources=["add_wrapper.pyx"],
              extra_objects=['libadd.a']
              # ,libraries=["add"],
              # library_dirs=["."]
              # ,runtime_library_dirs=["."]
    )
]

setup(
  name = 'wrapper for libadd',
  ext_modules = cythonize(ext_modules),
)
