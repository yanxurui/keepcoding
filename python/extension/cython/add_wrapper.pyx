"""A wrapper for external C function `add`
"""

cdef extern from "libadd.h":
    cpdef int add(int a, int b)
