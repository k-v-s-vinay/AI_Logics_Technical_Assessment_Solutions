# code for entering the linked list 1
n1 = int(input("Enter no.of values for first linked list:"))
l1 = []
for i in range(1,n1+1):
  l = int(input(f'Enter number {i}: '))
  l1.append(l)

# code for entering the linked list 1
n2 = int(input("Enter no.of values for Second linked list:"))
l2 = []
for i in range(1,n2+1):
  l = int(input(f'Enter number {i}: '))
  l2.append(l)

# for checking the lists are correctly stored or not
print(l1)
print(l2)

# sort the list
l1 = l1[::-1]
l2 = l2[::-1]

# for storing the reverse list elements
t1 = ''
t2 = ''

# code for storing the elements
for i in l1:
  t1 += str(i)
for i in l2:
  t2 += str(i)

# code for storing the resultant value
r = int(t1)+int(t2)

# code for reverse the resultant value 
rs = []
for i in str(r):
  rs.append(i)
rs = rs[::-1]

# code for final output display
for i in rs:
  print(int(i),end = " ")
