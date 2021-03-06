local function private()
    print("in private function")
end

local function foo()
    print("Hello World!")
end

local function bar()
    private()
    foo() -- do not prefix function call with module
end

return {
  foo = foo,
  bar = bar,
}
