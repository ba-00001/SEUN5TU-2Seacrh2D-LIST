def search(lst, target):
  num_sublists = 0

  for row in lst:
    if target in row:
      num_sublists += 1

  return num_sublists

l = [[1,2,3], [0,2,3], [0,1,1]]
print(search(l, 1)) # 2

l = [[1,1,1], [2,2,2], [3,3,3]]
print(search(l, 1)) # 1

l = []
print(search(l, 2)) # 0