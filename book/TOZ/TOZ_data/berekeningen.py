import sympy as sym

F, L1, L2, EI, EA, L3 = sym.symbols('F L1 L2 EI EA L3')

F = sym.Integer(30)

L1 = 4
L2 = 2

L3 = 5

EI = 56000

EA = 4500

B_h = sym.symbols('B_h')

w = F * L1**3 / EI / 3 + F * L1**2 / EI /2 * L2 + B_h * L3 / EA

B_h_sol = sym.solve(sym.Eq(w, 0), B_h)[0]

print(B_h_sol)

V = F + B_h_sol

print(V)

print(w.subs(B_h, B_h_sol)-B_h_sol*L3/EA)