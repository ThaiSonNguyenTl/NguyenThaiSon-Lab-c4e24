a = int(input("Enter a:"))
b = int(input("Enter b:"))
from calc import evaluate

# print()
# if ptoan == "+":
#     n = a + b   
# elif ptoan == "-":
#      n = a - b
# elif ptoan == "*":
#     n =a*b
# else:
#     n =a/b
pt = input("pt: ")
n = evaluate(a,b,pt )

print(n)