def recursive_binary_search(lst, target):
  if len(lst) == 0:
    return None
  else:
    
    midpoint = len(lst) // 2
    if lst[midpoint] == target:
      return True
    elif lst[midpoint] < target:
      return recursive_binary_search(lst[midpoint+1:], target)
    else:
      return recursive_binary_search(lst[:midpoint], target)


def verify(index):
  """
  Verify the recursive binary search algorithm
  """
  if index is not None:
    print("Found: ", index)
  else:
    print("Found", index)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = recursive_binary_search(numbers, 11)
verify(result)

result2 = recursive_binary_search(numbers, 6)
verify(result2)
