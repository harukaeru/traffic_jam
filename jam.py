import random
import time
N = 100
A = [0] * N

# 0: 空間
# 1: 停止
density = 0.2
car = '🚗' 
space = '  '
for i in range(N):
  A[i] = car if random.random() <= density else space

t = 0
while True:
  print(f't:{t:08d} ', end='')
  print(''.join(reversed(A)))
  i = 0
  while i < N:
    if A[i] == car:
      if A[(i + 1) % N] == space:
        A[i] = space
        A[(i + 1) % N] = car
        i += 1
      else:
        A[i] = car
    else:
      A[i] = space

    i += 1
  time.sleep(0.05)
  t += 1