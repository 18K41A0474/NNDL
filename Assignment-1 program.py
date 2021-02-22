from sympy import *
x = Symbol('x')
y = diff(x**4+3*x**2+10,x)
print(f'First order derivative of function is ')
z = 1.0
itr = 20
learningrate = 0.1
for i in range(0,itr):
    x = symbols('x')
    df = y.subs(x, z)
    df = round(df,2)
    dx = (-1.0)*learningrate*df
    z = z + dx
    x1 = round(z, 2)
print(z)
print(f'minimum value obtained at x = {z} for function')
fn = x**4+3*x**2+10
print(f'value for function(f(x)) at minimum value x = {z} is {fn.subs(x,z)}')