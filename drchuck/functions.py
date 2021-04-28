def computepay(hours, rate):
  try:
    hours = int(hours)
    rate  = int(rate)

    if hours >= 40:
      print('Pay: ', ((hours*rate)*1.5))
    else:
      print('Pay: ', (hours*rate))

  except:
    print('Wrong Input(Only Numeric values are required)')

hours = input('Enter Hours : ')
rate = input('Enter Rate : ')

payresult = computepay(hours, rate)