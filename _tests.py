d={(0, 1): 3.0, (1, 0): 2.914213562373095}

print(min(d, key=d.get))
print(d.keys())




ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)