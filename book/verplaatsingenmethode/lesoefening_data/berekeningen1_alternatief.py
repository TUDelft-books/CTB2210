import sympy as sym

EA, m, w, L = sym.symbols('EA m w L')

M_E_EF, M_E_DE = sym.symbols('M_E_EF M_E_DE')

phi = sym.symbols('phi')

N_CF = M_E_EF / (5 / 2)

w_F = N_CF * L / EA

N_AD = sym.nsimplify(1050) - N_CF - N_AD

w_E = sym.nsimplify(1050) * L / EA

eq1 = sym.Eq(phi, - w_F / (5 / 2) - w_E)

print(eq1)

M_E_EF_sol = sym.solve(eq1, M_E_EF)[0]
print(M_E_EF_sol)

N_AD = M_E_DE / (5 / 2)

w_D = N_AD * L / EA

eq2 = sym.Eq(phi, w_D / (5 / 2) - w_E)

M_E_DE_sol = sym.solve(eq2, M_E_DE)[0]
print(M_E_DE_sol)

eq3 = sym.Eq(M_E_EF_sol, M_E_DE_sol)

phi_sol = sym.solve(eq3, phi)[0]
print(phi_sol)

N_CF_sol = N_CF.subs({M_E_EF: M_E_EF_sol, M_E_DE: M_E_DE_sol, phi: phi_sol})
print(N_CF_sol)

#wrong