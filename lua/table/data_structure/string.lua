-- WARNING: bad code ahead!!
local buff = ""
for line in io.lines() do
	buff = buff .. line .. "\n"
end
print(buff)