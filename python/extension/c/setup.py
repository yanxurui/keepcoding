from distutils.core import setup, Extension

module1 = Extension('demo',
                    sources = ['demomodule.c'],
                    extra_compile_args = ['-O0', '-g']
                    )

setup (name = 'a demo extension module',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])
