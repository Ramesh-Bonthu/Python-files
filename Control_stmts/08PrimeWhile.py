# check wheather given numbers is prime or not

num = int(input(" Enter the number : "))
temp=0
i = 2
#i = range(2,num-1,1) 
while (i < num) :
  if (num % i==0):
    temp +=1
    break
  i += 1

if temp==0 :
  print(" prime")
else :
  print(" not prime")

