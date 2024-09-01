# fibonacci series up to nth number

num = int(input(" Enter the number for fibo : "))

n1 = 0
n2 = 1
#n3 = n1 + n2
 
for i in range(num) :
  n3 = n1 + n2 
  print(n3)
  n1 = n2
  n2 = n3