total = 0
count = 0
averge = 0

while True:
  value = input('Enter a number > ')
  
  try:
    number = eval(value)

    total += number
    count += 1
    average = total / count

  except:
    if value == 'done':
      print(total, count, average)
      break
    
    print('Not a number')
    continue


store = []

while True:
  try:
    number = eval(input('Enter a number > '))

    store.append(number)
  except:
    print('No a number')
    break

check = 0

for data in store:
  if data >= check:
    check = data
  
print(check)
