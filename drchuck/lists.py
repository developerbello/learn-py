fname = open('./data/romeo.txt')

store = []

for line in fname:
  line = line.split()
  for word in line:
    # if word in store: continue
    
    store.append(word)

print(len(store))