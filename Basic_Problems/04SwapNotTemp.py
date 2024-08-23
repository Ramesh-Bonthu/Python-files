# Swap the values of two variables without temporary variable

a = int(input("Enter a value : "))
b = int(input("Enter b value : "))

a = a + b
b = a - b
a = a - b
print(f"a={a}",f"b={b}")