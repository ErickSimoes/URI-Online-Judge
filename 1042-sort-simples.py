# -*- coding: utf-8 -*-

n = list(map(int, input().split()))
m = n.copy()
n.sort()

for i in n:
  print(i)

print()

for i in m:
  print(i)
