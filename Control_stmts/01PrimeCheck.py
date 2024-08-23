# check wheather given numbers is prime or not

num = int(input(" Enter the number : "))
temp=0
i = 2
#i = range(2,num-1,1) 
for i in range(2,num-1) :
  if (num % i==0):
    temp +=1
    break

if temp==0 :
  print(" prime")
else :
  print(" not prime")