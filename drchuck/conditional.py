# Incorrect logic applied ::: To be revisited
try:
  hours = eval(input('Enter Hours : '))
  rate = eval(input('Enter Rate : '))
  
  if hours >= 40:
    print('Pay: ', ((hours*rate)*1.5))
  else:
    print('Pay: ', (hours*rate))

except:
  print('Wrong Input(Only Numeric values are required)')



score = eval(input('Enter numbers between 0.0 and 1.1> '))

if score > 1.1:
  print('Out of range')
else:
  if score >= 0.9 and score <= 1.1:
    print('Grade is > A')
  elif score >= 0.8:
    print('Grade is > B')
  elif score >= 0.7:
    print('Grade is > C')
  elif score >= 0.6:
    print('Grade is > D')
  elif score >= 0.6:
    print('Grade is > E')
  elif score < 0.6:
    print('Grade is > F')
