local mod = require 'simple_module'

mod.pub_func()
-- foo=hello
-- bar=1
-- baz[a]=1
print()

mod.bar = 2
mod.baz['a'] = 2
mod.pub_func()
-- foo=hello
-- bar=1
-- baz[a]=2
