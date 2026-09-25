# Begeleide oefening

```{figure-start} ./lesoefening1_data/constructie.svg
:align: center
:source: source files on https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/matrix_2
:number:
:figclass: sticky-margin
```

- $EI = 4 \ \rm{MNm^2}$
- $EA \gg EI$

```{figure-end}
```

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[\begin{pmatrix} 4000 & 2000 \\\ 2000 & 4000 \end{pmatrix}]
^^^
? Bepaal de ingevulde elementstijfheidsmatrix $\mathbf{K}^{(e)}$ voor een element. Merk op dat alle elementen dezelfde lengte en stijfheid hebben. Gebruik de functie 'Insert Matrix'.

$\mathbf{K}^{(e)} = $ {gap}

---

::::


Ga uit van de verplaatsingsvector $ \mathbf{u} =  \begin{bmatrix}  \varphi_{\rm{A}} \\  \varphi_{\rm{B}} \\ \varphi_{\rm{C}} \\ \varphi_{\rm{D}} \\ \varphi_{\rm{E}} \end{bmatrix} $

::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

---

M[\begin{bmatrix} 4000 & 2000 & 0 & 0 & 0 \\\ 2000 & 12000 & 2000 & 2000 & 0 \\\ 0 & 2000 & 8000 & 0 & 2000 \\\ 0 & 2000 & 0 & 4000 & 0 \\\ 0 & 0 & 2000 & 0 & 4000 \end{bmatrix}] Bepaal de globale stijfheidsmatrix $\mathbf{K}$. Gebruik wederom de functie 'Insert Matrix'.

---

::::


::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

---

M[\begin{pmatrix} M_A \\\ 0 \\\ 73 \\\ 0 \\\ 0 \end{pmatrix}] Bepaal de krachtvector $\mathbf{F}$. Gebruik wederom de functie 'Insert Matrix'.

---
::::



::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[0]
M[-2]
M[11]
M[1]
M[-5.5]
^^^
? Bepaal de waarde van de vrijheidsgraden $\varphi_{\rm{B}}$, $\varphi_{\rm{C}}$, $\varphi_{\rm{D}}$ en $\varphi_{\rm{E}}$.

- $\varphi_{\rm{A}} = ${gap}$ \rm{mrad} $
- $\varphi_{\rm{B}} = ${gap}$ \rm{mrad} $
- $\varphi_{\rm{C}} = ${gap}$ \rm{mrad} $
- $\varphi_{\rm{D}} = ${gap}$ \rm{mrad} $
- $\varphi_{\rm{E}} = ${gap}$ \rm{mrad} $ 
---
::::

