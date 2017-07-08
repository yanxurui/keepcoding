function Set (list)
  local set = {}
  for _, l in ipairs(list) do set[l] = true end
  return set
end

-- 如果函数的参数只有一个，并且是字面值字符串或constructor，那么函数的小括号可以省略
-- 例如，print [[hello]]
reserved = Set{"while", "end", "function", "local", }


identifiers = {"begin", "global", "local"}
for _, w in ipairs(identifiers) do
  if reserved[w] then
    print(w, "is a reserved word")
  end
end
