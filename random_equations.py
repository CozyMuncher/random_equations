"""A progrm to get a random equation based on its result and length"""
import random
import pyfiglet

functions = ["+", "-", "*", "/", "**", "%"]

print(pyfiglet.figlet_format("Random Equations"))

result = input("What is the result?")
length = input("How long do you want the equation to be?")

equation = ''
lastsym = ''
loop = 0

def power():
    global equation, loop

    if loop == 5:
        equation = equation[:-1]
        return False
    equation += str(random.randint(1,9))
    try: 
        eval(equation)
    except: 
        equation = equation[:-1]
        loop += 1
        power()
    loop = 0
    return True

def checker(success, i):
    if success == True:
        return i
    else:
        return i-1
    
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


for i in range(int(length)):
    if lastsym == '**':
        i = checker(power(), i)
    else:
        equation += str(int(random.randint(1,999)))
    lastsym = functions[random.randint(0,5)]
    equation += lastsym

equation += str(random.randint(1,999))
extra = float(int(result)) - eval(equation)
equation += "+"
equation += format(extra)

# factors = prime_factors(extra)

# for i in factors:
#     equation += i

print("The equation is:")
print(equation)
