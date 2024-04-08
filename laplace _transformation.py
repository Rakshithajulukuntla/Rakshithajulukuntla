from sympy import laplace_transform, exp, symbols
t, s = symbols('t s')
f = exp(-2*t)
F, _, _ = laplace_transform(f, t, s)
print("Laplace Transform of exp(-2*t):", F)
