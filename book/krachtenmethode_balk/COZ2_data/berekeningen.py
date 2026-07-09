import numpy
import sympy
#P1=random(2,4,0.1) #b

#P2=random(3,5,0.1) #c

#P3=random(50,100,1) F1

# P4=random(100,200,1) F2

# P5=random(1000,10000,1) EI

P1, P2, P3, P4, P5 = sympy.symbols('P1 P2 P3 P4 P5')

P1 = sympy.Integer(2)
P2 = sympy.Integer(4)
a = P1+P2
P4 = sympy.N(9*27*32/100)
P3 = sympy.N(27*32*4.5/100)

print(P1, P2, P3, P4, P5, a)

ans_3224427 = (P1**2*P2*P4+2*P1*P2*P4*a+P1*P3*a**2+P2*P3*a**2+P2*P4*a**2)/(P1**2+2*P1*P2+2*a*P1+P2**2+2*a*P2+a**2)
ans_4816139 = (a*P1**2*P3*3+a*P1*P2*P3*6+a*3*P2**2*P3+3*a*P2**2*P4+P1**3*P3+3*P1**2*P2*P3+3*P1*P2**2*P3+3*P1*P2**2*P4+P2**3*P3+P2**3*P4)/(a**2+2*a*P1+2*a*P2+P1**2+2*P1*P2+P2**2)/(a+P1+P2)
ans_5520747 = sympy.Rational(1, 8) * (-sympy.Rational(1, 4) * sympy.Abs((2*P2**3*P3+75*P1**2*P4)/(5*P1+P2))+P3*P2**2)

print(ans_3224427, ans_3224427.evalf())
print(ans_4816139, ans_4816139.evalf())
print(ans_5520747, ans_5520747.evalf())