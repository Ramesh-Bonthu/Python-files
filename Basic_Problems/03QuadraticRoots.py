# to find the roots of a quadratic equation

a = int(input("Enter a value : "))
b = int(input("Enter b value : "))
c = int(input("Enter c value : "))

det = b**2 - 4 * a * c

root1 = (-b + (det**0.5))/(2*a)
root2 = (-b - (det**0.5))/(2*a)

print(f"Roots:{root1,root2}")