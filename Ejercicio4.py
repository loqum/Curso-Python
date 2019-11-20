def run():
  x = 17
  y = 19

  x = 12 if (x == y) else 15

  print("x: ", x, "\ny: ", y)

  if y < x:
    y = 12
  else:
    x = 5
 
  print("\nx: ", x, "\ny: ", y)
