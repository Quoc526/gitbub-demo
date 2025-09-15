import math 

nhapvao = input()
nhapvao2 = input()

a = int(nhapvao) 
b = int(nhapvao2)

def func(a,b):
    result = 0

    if a == 0: result = b**2
    elif a == 1: result = math.sqrt(b)
    elif a == 2: result = b

    return result

y = func(a,b)

u1 = b**2 * y
u2 = math.sqrt(b) * y
u3 = b * y

print(u1," ",u2," ",u3)
//linhhjjffhipfp
result = 1e1000
print(result)
