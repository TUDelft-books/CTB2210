import sympy as sym

EA, m, w, L = sym.symbols('EA m w L')

M_E_EF = sym.symbols('M_E_EF')

Bv, Cv = sym.symbols('Bv Cv')

N_CF = EA * w / L

N_CF_2 = sym.symbols('N_CF_2')

N_BE = sym.nsimplify( (1050 * 5 / 2 - N_CF_2 * 5) / (5/2))

print('N_BE = ', N_BE)

N_AD = sym.nsimplify(1050 - N_BE - N_CF_2)

print('N_AD = ', N_AD)

w_D = N_AD * L / EA

w_E = N_BE * L / (EA * 5)

w_F = w_D + (w_E - w_D)

print('w_F = ', w_F)

eq1 = sym.Eq(w_F, w)

N_F_2 = sym.solve(eq1, N_CF_2)[0]
print('N_F = ', N_F_2)

eq2 = sym.Eq(N_F_2, N_CF)
print(eq2)

w_sol = sym.solve(eq2, w)[0]
print('w = ', w_sol)

print('N_CF = ', N_CF.subs(w, w_sol))