import sympy as sym

F, L1, L2, EI, EA, L3 = sym.symbols('F L1 L2 EI EA L3')

F = sym.Integer(30)
L1 = sym.Integer(4)
L2 = sym.Integer(2)
L3 = sym.Integer(5)
EI = sym.Integer(56000)
EA = sym.Integer(4500)

B_h = sym.symbols('B_h')

w = F * L1**3 / EI / 3 + F * L1**2 / EI /2 * L2 - B_h * (L1 + L2) **3 / EI / 3 - B_h * L3 / EA 

B_h_sol = sym.solve(sym.Eq(w, 0), B_h)[0]

print(B_h_sol,B_h_sol.evalf())

V = F + B_h_sol

print(V)

#print(w.subs(B_h, B_h_sol)-B_h_sol*L3/EA)

N_BC = (F * L1**2 / EI * (L1/3 + L2/2)) / ( (L1 + L2)**3 / EI / 3 + L3 / EA)

print(N_BC)

print((N_BC - B_h_sol).simplify())

w2 = F * L1**3 / EI / 3 + F * L1**2 / EI /2 * L2 - B_h * (L1 + L2) **3 / EI / 3

B_h_sol_2 = sym.solve(sym.Eq(w2, 0), B_h)[0]

print(B_h_sol_2,B_h_sol_2.evalf())

V_2 = F + B_h_sol_2

print(V_2,V_2.evalf())
