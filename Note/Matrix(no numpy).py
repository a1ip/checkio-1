# sum of column
col_sum = []
for col in zip(*matrix):
  col_sum.append(sum(col))
