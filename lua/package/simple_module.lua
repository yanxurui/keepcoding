local _M = {}

local foo = 'hello'
local bar = 1
local baz = {a=1}
local function priv_func()
	print('foo='..foo)
	print('bar='..bar)
	print('baz[a]='..baz['a'])
end

local function pub_func()
	priv_func()
end

-- public fields

_M = {
  bar=bar,
  baz=baz,
  pub_func=pub_func
}

return _M