from random import randint  # function to get random integer
a = randint(0, 100)
b = randint(0, 100)
c = randint(0, 100)
print("a={} b={} c={}".format(a, b, c))
# here place the code which will print e.g. "Greatest value is stored in variable b" based on actual values

if a>b:
    if a>c:
        print('max in a', a)
    elif a<c:
        print('max in c', c)
    else:
        print('max in a and c', a)
elif b>a:
    if b>c:
        print('max in b', b)
    elif b<c:
        print('max in c', c)
    else:
        print('max in b and c', b)
else:
    if a>c:
        print('max in a and b', b)
    elif a<c:
        print('max in c', c)
    else:
        print('max in a, b and c', a)
        
