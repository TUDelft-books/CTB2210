import sympy as sym

L1, L2, L3, L4, L5, EI, EA, F, w_0 = sym.symbols('L1 L2 L3 L4 L5 EI EA F w_0')
a = sym.symbols('a')

L5 = 4
L1 = 2
L2 = 2
L3 = 2
L4 = 3
F = sym.nsimplify(33)
print(F)
#w_0 = sym.nsimplify(0.2)
EA = 1000

N_DG = sym.symbols('N_DG')

N_EH = (- N_DG * (L1 + L2 + L3) + F * (L1 + L2))/ L1
print('N_EH=',N_EH.expand(),'=',N_EH.evalf())
w_H = sym.Integer(0)
print('w_H=',w_H.expand(),'=',w_H.evalf())
w_E = w_H + N_EH * L4 / EA * a
print('w_E=',w_E.subs(a,1).expand(),'=',w_E.subs(a,1).evalf())
w_G = w_E / L1 * (L1 + L2 + L3)
print('w_G=',w_G.subs(a,1).expand(),'=',w_G.subs(a,1).evalf())
w_D = w_G - N_DG * L4 / EA
print('w_D=',w_D.subs(a,1).expand(),'=',w_D.subs(a,1).evalf())

eq1 = sym.Eq(w_D, 0)
N_DG_sol = sym.solve(eq1, N_DG)[0]

print('EA = inf ',N_DG_sol.subs(a,0),'=',N_DG_sol.subs(a,0).evalf())
print('EA = normal ',N_DG_sol.subs(a,1),'=',N_DG_sol.subs(a,1).evalf())

N_DG_sol2 = F * (L1 + L2) / (L1 + L2 + L3)
print('EA = 0',N_DG_sol2.expand(),'=',N_DG_sol2.evalf())

print('w_E, inf', w_E.subs({N_DG: N_DG_sol.subs(a,0), a:0}).expand(),'=',w_E.subs({N_DG: N_DG_sol.subs(a,0), a:0}).evalf())
print('w_E, normal', w_E.subs({N_DG: N_DG_sol.subs(a,1), a:1}).expand(),'=',w_E.subs({N_DG: N_DG_sol.subs(a,1), a:1}).evalf())
print('w_E, 0', N_DG_sol2 * L4 / EA / 3, '=', (N_DG_sol2 * L4 / EA / 3).evalf())
