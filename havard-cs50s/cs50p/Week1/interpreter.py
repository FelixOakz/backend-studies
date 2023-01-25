exp = input('Expression: ')
x, y, z = exp.split(' ')
x, z = int(x), int(z)

if '/' in y:
    print(float(x/z))
elif '*' in y:
    print(float(x*z))
elif '+' in y:
    print(float(x+z))
elif '-' in y:
    print(float(x-z))