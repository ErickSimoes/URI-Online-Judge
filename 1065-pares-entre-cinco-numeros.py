par = 0

for _ in range(5):
  num = int(input('insert'))
  if num % 2 == 0:
    par += 1

print(par, 'valores pares')
