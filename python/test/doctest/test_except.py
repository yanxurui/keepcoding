"""compute the square of an integer

>>> square(1)
1
>>> square(2)                                                                                                     
4
>>> square(-2)
4
>>> square('2')                                                                                                   
Traceback (most recent call last):
  ...
TypeError: an integer is required
"""

def square(a):
	if type(a) is not int:
		raise TypeError('an integer is required')
	return a*a;
