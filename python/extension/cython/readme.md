gcc -c libadd.c
ar rcs libadd.a libadd.o
python setup.py build_ext --inplace
