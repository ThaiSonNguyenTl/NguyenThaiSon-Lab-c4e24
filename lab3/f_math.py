from random import randint,choice
from calc import evaluate
phtoan = ["+","-","*","/"]
op = choice(phtoan)
#1 sinh bieu thuc
x = randint(0,9)
y = randint(0,9)
error = randint(-1,1)
r = evaluate(x,y,op) + error
print(f"{x} {op} {y} = {r}")
#2 
user_answer = input("(Y/N)?").upper()
if user_answer == "Y":
    if error == 0:
        print("Yay")
    else:
        print("You're Wrong")
else :
    if error == 0:
        print("You're Wrong")
    else:
        print("yay")