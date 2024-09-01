# Determine the  grade based on score

mark = int(input("Enter the marks : "))

if (mark>90 and mark<100) :
  print(" A+ Grade ")
elif (mark > 80) :
  print(" A Grade ")
elif (mark > 70) :
  print(" B+ Grade ")
elif (mark > 60) :
  print(" B Grade ")
elif (mark > 50) :
  print(" C+ Grade ")
elif (mark > 40) :
  print(" C Grade ")
else :
  print(" Fail ")