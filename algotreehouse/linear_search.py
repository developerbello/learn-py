def linear_search(lst, target):
  
  """
  Return the position of the target if found, else return None
  """

  for i in range(0, len(lst)): # constant time to runthrough each value on the list
    if lst[i] == target:
      return i

  return None

def verify(index):
  """
  Verify the linear search algorithm
  """
  if index is not None:
    print("Index found at index: ", index)
  else:
    print("Index not found in the list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = linear_search(numbers, 11)
verify(result)

result2 = linear_search(numbers, 6)
verify(result2)