# check whether the given string is present or not 

t = input("Enter the first string :")
p = input("enter the second string :")
count = 0
for i in range(0,len(t)-len(p)+1) :
    if (p[0:len(p)]==t[i+0:i+len(p)]) :
        count +=1

print(f"second string present in {count} times")