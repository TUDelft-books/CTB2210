import sympy
#P1=random(5,10,0.1) #L1

#P2=random(10,20,0.1) #L2

#P3=random(1000,10000,100) #EI

#P4=random(5,10,0.1) #Q1

#P5=random(10,20,0.1) #Q2

#P6=random(100,200,1) #F

P1, P2, P3, P4, P5, P6 = sympy.symbols('P1 P2 P3 P4 P5 P6')

P1 = sympy.Integer(4)
P2 = sympy.Integer(6)
P3 = sympy.Integer(20000)
P5 = sympy.Integer(28*3)
P4 = sympy.Integer(7*6*1.5)
P6 = sympy.Integer(150)

print(P1, P2, P3, P4, P5, P6)

ans_3648164 = sympy.Rational(1, 8) * (2*P1**3*P4+P2**3*P5)/(P2+2*P1)
ans_9284846 = sympy.Rational(1, 8) * (2*P1**3*P4+P2**3*P5)/(P2+2*P1)/P1 + sympy.Rational(1, 8) * (2*P1**3*P4+P2**3*P5)/(P2+2*P1)/P2 + sympy.Rational(1, 2) * P4 * P1 + sympy.Rational(1, 2) * P5 * P2 + P6
ans_4866014 = sympy.Rational(1, 16) * (2*P1**3*P4+P2**3*P5)/(P2+2*P1) - sympy.Rational(1, 8) * P4 * P1**2
ans_5219473 = sympy.Rational(1, 16) * (2*P1**3*P4+P2**3*P5)/(P2+2*P1) - sympy.Rational(1, 8) * P5 * P2**2

print(ans_3648164)
print(ans_9284846)
print(ans_4866014)
print(ans_5219473)