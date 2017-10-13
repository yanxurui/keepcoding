execute
```
python -m pkg.B.b
```
see: [How to fix “Attempted relative import in non-package” even with __init__.py](https://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py/27876800#27876800)

forget about `__package__`
```
> tree pkg
pkg
├── A
│   ├── __init__.py
│   ├── a.py
├── B
│   ├── __init__.py
│   └── b.py
├── __init__.py


> cat pkg/A/a.py           
def say(whatever):
	print(whatever)


> cat pkg/B/b.py
# import pkg

if __name__ == '__main__' and __package__ is None:
    __package__ = 'pkg.B'

from ..A import a

a.say('hello world')


> PYTHONPATH=. python pkg/B/b.py 
Traceback (most recent call last):
  File "pkg/B/b.py", line 4, in <module>
    from ..A import a
SystemError: Parent module 'pkg' not loaded, cannot perform relative import

```