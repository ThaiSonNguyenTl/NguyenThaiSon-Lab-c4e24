from random import *
def evaluate(x,y,pt):
    if pt == "+":
        r = x + y 
    elif pt == "-":
        r = x - y
    elif pt == "*":
        r = x * y
    elif pt == "/":
        if y == 0:
            return False
        else:
            r = x/y
    return r
def generate_quiz():
    # Hint: Return [x, y, op, result]
    phtoan = ["+","-","*","/"]
    op = choice(phtoan)
    #1 sinh bieu thuc
    x = randint(0,9)
    y = randint(0,9)
    error = randint(-1,1)
    r = evaluate(x,y,op) + error
    print(f"{x} {op} {y} = {r}")
    return [x, y, op, r]

def check_answer(x, y, op, result, user_choice):
    print(op)
    r =evaluate(x,y,op)
    if user_choice == True:
        if r == result:
            return True
        else:
            return False
    else:
        if r == result:
            return False
        else:
            return True