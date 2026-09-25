n = int(input('Enter n: '))
l = []
for i in range(1,n+1):
  n1 = int(input(f'Enter number {i}: '))
  l.append(n1)
print(l)

k = int(input('Enter K: '))

length = 0
pos = 0
for i in range(0,len(l)):
  if i+1 < len(l):
    d = l[i] - l[i+1] 
    if d <= k and d >= 0:
      length += 1
    else:
      p = l[i+1]
      break
print(length,pos)