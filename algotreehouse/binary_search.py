def binary_search(lst, target): 

  first = 0
  last = len(lst) - 1

  while first <= last:
    midpoint = (first + last) // 2

    if lst[midpoint] == target:
      return midpoint
    elif lst[midpoint] < target:
      first = midpoint + 1
    else:
      last = midpoint - 1
  return None

numbers = [1, 2, 3 ,4 , 5, 6, 7, 8 ,9, 10]
print(binary_search(numbers, 2))
