import sympy as sym

L1, L2 = sym.symbols('L1 L2')
EA, EI, q = sym.symbols('EA EI q')
eps_T = sym.symbols('eps_T')
alpha = sym.nsimplify(10^-5)
A_m = sym.symbols('A_m')

L1 = sym.nsimplify(5)
q = sym.nsimplify(12)
EI = sym.nsimplify(20000)
EA = sym.nsimplify(8000)
L2 = sym.nsimplify(6)

N_BC = sym.nsimplify(- 1 / (1/5 *3 * L1) * (q * L1 **2 /2 - A_m))
print('N_BC=', N_BC)
deltaL_BC = N_BC * L2 / 4 * 5 / EA
print('deltaL_BC=', deltaL_BC)
w_C = - deltaL_BC/3*5
print('w_C=', w_C)

phi_A = q * L1 **3 / (24 * EI) + w_C / L1 - A_m * L1 / (3 * EI)

print('phi_A=', phi_A)

eq = sym.Eq(phi_A, 0)

sol = sym.solve(eq, A_m)
print('A_m=', sol[0])