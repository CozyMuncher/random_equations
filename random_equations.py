"""A progrm to get a random equation based on its result and length"""
import random
import sys
import pyfiglet

# Some variables to make life easier for me
functions = ["+", "-", "*", "/", "**", "%"]

# PEMDAS stuff
pedmas = ['*', '/', '%']

# Stores the euqation
equation = ''

# Stores the last symbol
lastsym = ''

# Contains some stuff for pemdas
symbols = []
numbers = []

# Internals
loop = 0
maxsize = sys.maxsize

# UI
print(pyfiglet.figlet_format("Random Equations"))

result = input("What is the result?")
length = input("How long do you want the equation to be?")



def power():
    """Function to power a number"""

    global equation, loop, numbers

    # Debug Logs
    if loop != 0:
        print("Power Repeat")
    else:
        print("Power Start")

    # Removes te power as powering the number makes it too large
    if loop == 5:
        equation = equation[:-1]
        equation = equation[:-1]
        symbols.pop()

        return False

    # Checks if number is too large and 
    # stops powering the number if its too large
    if eval(equation[:-2]) > 1000000:
        equation = equation[:-1]
        equation = equation[:-1]
        symbols.pop()

        return False

    # Creates the number to use to raise the power
    new_number = random.randint(1,9)
    equation += str(new_number)

    # tries to power the equation
    try:
        eval(equation)

    # Number too large
    except OverflowError:

        # Breaks from the equation
        equation = equation[:-1]
        loop += 1
        power()

    # Number too large after powering
    # Causes weird problems in code if number is too large
    if eval(equation) > 1000000:
        equation = equation[:-1]
        loop +=1
        power()

    # Found a suitable number to use as the power
    loop = 0
    numbers.append(new_number)
    print(f"Added: {new_number}")
    print(F"New equation: {equation}")
    print(f"New value: {eval(equation)}")

    return True

def divide():
    """Function to divide a number"""

    global equation, numbers

    print("Divide Start")

    value = pemdas_check()
    print(f"Value: {value}")

    try:
        if value.isdigit() is False:
            value = eval(value)
    except AttributeError:
        pass

    # Checks if value is too large - takes too long
    try:
        if (value) > 1000000:
            equation = equation[:-1]
            return False
    except TypeError:
        if eval(value) > 1000000:
            equation = equation[:-1]
            return False

    # Get factors
    factors = prime_factors(abs(int(value)))
    print(f"Factors: {factors}")

    # Checks if factor is a prime
    if len(factors) == 2:
        equation = equation[:-1]
        print("Number is prime")
        return False

    factors_chosen = random.choice(factors)
    print(f"Factor chosen: {factors_chosen}")

    equation += str(factors_chosen)
    numbers.append(factors_chosen)

    print(f"New Equation: {equation}")
    print(f"New value: {eval(equation)}")
    return True



def checker(success, i):
    print("End")
    if success is True:
        return i
    else:
        return i-1

def check_negative(s):
    try:
        f = float(s)
        if f < 0:
            return True
        # Otherwise return false
        return False
    except ValueError:
        return False

def prime_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    return factors

def checK_range(number):
    if number > maxsize:
        return False
    else: return True

def pemdas_check():
    temp_eqn = ''
    print(symbols)
    print(numbers)

    for i in range(2, len(symbols)):
        if symbols[-i] in pedmas:
            print(f"Symbol: {symbols[-i]}")
            print("Symbol in pemdas")
        else:
            if i == 2:
                return numbers[-1]
            else:
                for n in range(i-1, 0, -1):
                    temp_eqn += str(numbers[-n])
                    temp_eqn += symbols[-n]

                print(f"temp_eqn: {temp_eqn}")
                temp_eqn = temp_eqn[:-1]
                if temp_eqn[-1] == '*': 
                    temp_eqn = temp_eqn[:-1]
                return temp_eqn
    if len(symbols) == 1:
        return numbers[-1]
    return numbers[-1]

def get_equation():
    """Functions that generates the equation"""

    global equation, lastsym, length, symbols, numbers

    for i in range(int(length)+1):
        if lastsym == '**':
            if symbols[-1] == "/":
                equation = equation[:-1]
                equation = equation[:-1]
                symbols.pop()
                checker(False, 1)
            else:
                i = checker(power(), i)
        elif lastsym == "/":
            i = checker(divide(), i)
        else:
            try:
                eval(equation[:-len(lastsym[-1])])
            except SyntaxError:
                new_number = random.randint(1,999)
                equation += str(new_number)
                numbers.append(new_number)
            except IndexError:
                new_number = random.randint(1,999)
                equation += str(new_number)
                numbers.append(new_number)
            else:
                if eval(equation[:-len(lastsym[-1])]) > 1000000 or \
                   eval(equation[:-len(lastsym[-1])]) < -1000000:
                    if lastsym == "**":
                        equation = equation[:-2]
                    else:
                        equation = equation[:-1]
                    symbols.pop()

                    choice = random.randint(1,2)

                    if choice == 1:
                        symbols.append('/')
                        equation += '/'
                        i = checker(divide(), i)
                    elif choice == 2:
                        symbols.append('-')
                        equation += "-"
                        new_number = random.randint(1,999)
                        equation += str(new_number)
                        numbers.append(new_number)
                else:
                    new_number = random.randint(1,999)
                    equation += str(new_number)
                    numbers.append(new_number)

            print(f"Added {new_number}")

        print(f"Current Equation: {equation}")
        print(f"Current value {eval(equation)}")
        print(f"Symbols: {symbols}")
        print(f"Numbers: {numbers}")

        lastsym = functions[random.randint(0,5)]
        equation += lastsym
        symbols.append(lastsym)

        print(f"Added {lastsym}")


# Gets equation
get_equation()

for i in range(1):
    if lastsym == '**':
            if symbols[-1] == "/":
                equation = equation[:-1]
                equation = equation[:-1]
                symbols.pop()
                checker(False, 1)
            else:
                i = checker(power(), i)
    elif lastsym == "/":
        i = checker(divide(), i)
    else:
        try:
            eval(equation[:-len(lastsym[-1])])
        except SyntaxError:
            new_number = random.randint(1,999)
            equation += str(new_number)
            numbers.append(new_number)
        except IndexError:
            new_number = random.randint(1,999)
            equation += str(new_number)
            numbers.append(new_number)
        else:
            if eval(equation[:-len(lastsym[-1])]) > 1000000 or \
               eval(equation[:-len(lastsym[-1])]) < -1000000:
                if lastsym == "**":
                    equation = equation[:-2]
                else:
                    equation = equation[:-1]
                symbols.pop()

                choice = random.randint(1,2)

                if choice == 1:
                    symbols.append('/')
                    equation += '/'
                    i = checker(divide(), i)
                elif choice == 2:
                    symbols.append('-')
                    equation += "-"
                    new_number = random.randint(1,999)
                    equation += str(new_number)
                    numbers.append(new_number)
            else:
                new_number = random.randint(1,999)
                equation += str(new_number)
                numbers.append(new_number)

extra = (int(result)) - eval(equation)

print(extra)
print(eval(equation))

if extra < 0 and str(format(extra, 'f'))[0] != '-':
    equation += '-'
else:
    equation += '+'
equation += str(extra)

print("The equation is:")
print(equation)
print(f"Result: {eval(equation)}")
