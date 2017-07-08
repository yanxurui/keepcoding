-- N行M列的全零矩阵
mt = {}          -- create the matrix
for i=1,N do
  mt[i] = {}     -- create a new row
  for j=1,M do
    mt[i][j] = 0
  end
end

-- 用一维数组创建同样的矩阵
mt = {}          -- create the matrix
for i=1,N do
  for j=1,M do
    mt[i*M + j] = 0
  end
end
