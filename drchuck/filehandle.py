# fhand = open('./data/bigdata.txt')

# for line in fhand:
#   line = line.upper()
#   print(line)

import re

fname = input('Enter the file name: ')
count = 0
total = 0

try:
  fhand = open(fname)

  for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
      dec = re.findall('\d*\.?\d+', line)
      count += 1
      total += eval(dec[0])
except:
  print(fname, "File doesn't exit")

    
avgspam = total / count

print(avgspam)
