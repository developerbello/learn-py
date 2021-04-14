def recursive_binary_search(lists, target, start=0, end=None):
  if end is None:
    end = len(lists) - 1
  if start > end:
    return None

  while start <= end:
    midpoint = (start + end) // 2

    if lists[midpoint] == target:
      return midpoint

    elif target < lists[midpoint]:
      return recursive_binary_search(lists, target, start, midpoint-1)
    else:
      return recursive_binary_search(lists, target, midpoint+1, end)


def verify(index):
  if index is not None:
    print("Index Found: ", index)
  else:
    print("Index not Found")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = recursive_binary_search(numbers, 5)
verify(result)
result2 = recursive_binary_search(numbers, 11)
verify(result2)