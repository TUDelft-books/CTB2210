# COZ opgave 3.2

::::::{note}
Deze opgave kan in ANS gemaakt worden.
:::{todo}
[Toevoegen link naar ANS toets.](https://github.com/TUDelft-books/CTB2210/issues/90)
:::
::::::

% https://ans.app/repo_questions/32111362/generator

Gegeven is de volgende constructie:

```{figure-start} ./COZ2_data/constructie.svg
---
align: center
number:
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/COZ_balk_dubbel
---

```

$$ EI = 50 \, \rm{MNm}^2 $$

```{figure-end}
```

::::{admonition} Opgave
:class: exercise

Bepaal het moment in $\rm{B}$.

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

De constructie is 3-voudig statisch onbepaald. Er wordt gekozen voor de volgende statisch bepaalde constructie om de statisch onbepaalde oplegreacties te vinden:

```{figure} ./COZ2_data/FBD1.svg
---
align: center
number:
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/COZ_balk_dubbel
---

```
Voor vormveranderingsvoorwaarde van $\rm{u_B=0}$ geldt de volgende vergelijking:

$$
\begin{align*}
u_{\rm{B}} &=0 \\
\cfrac{B_{\rm{h}} \cdot 12}{EA} &= 0 \\
B_{\rm{h}} &= 0
\end{align*}
$$

Voor het oplossen van $\rm{M_B}$ en $\rm{B_v}$ wordt de statisch bepaalde constructie gesplitst in vier losse belastingsgevallen:

```{figure} ./COZ2_data/Superpositie.svg
---
align: center
number:
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/COZ_balk_dubbel
---

```

Dit geeft de volgende twee vergelijkingen:

$$
\varphi_{\rm{B}} \ = \varphi_{\rm{C,1}} + \varphi_{\rm{D,2}} + \varphi_{\rm{B,3}} - \varphi_{\rm{B,4}} = 0
$$

$$
w_{\rm{B}} = w_{\rm{C,1}} + 6 \cdot \varphi_{\rm{C,1}} + w_{\rm{D,2}} + 4 \cdot \varphi_{\rm{D,2}} + w_{\rm{B,3}} - w_{\rm{B,4}} = 0
$$

Voor belastingsgevallen 1 en 2, blijft het gedeelte balk recht na de puntlast. De waarde van $\varphi$ verandert dus niet meer en het 'kwispeleffect' moet worden meegenomen als bijdrage voor $w_{\rm{B}} = 0$. De bekende vergeet-me-nietjes voor een uitkragende ligger kunnen worden gebruikt, wat de volgende vergelijkingen geeft:

$$
\begin{align*}
\varphi_{\rm{B}} = \cfrac{1}{2} \cdot \cfrac{38.88 \cdot 6^2}{50000} + \cfrac{1}{2} \cdot \cfrac{77.76 \cdot 8^2}{50000} + \cfrac{M_{\rm{B}} \cdot 12}{50000} - \cfrac{1}{2} \cdot \cfrac{B_{\rm{v}} \cdot 12^2}{50000} &= 0 \\[2mm]
w_{\rm{B}} = \cfrac{1}{3} \cdot \cfrac{38.88 \cdot 6^3}{50000} + 6 \cdot \cfrac{1}{2} \cdot \cfrac{38.88 \cdot 6^2}{50000} + \cfrac{1}{3} \cdot \cfrac{77.76 \cdot 8^3}{50000} + 4 \cdot \cfrac{1}{2} \cdot \cfrac{77.76 \cdot 8^2}{50000} + \cfrac{1}{2} \cdot \cfrac{M_{\rm{B}} \cdot 12^2}{50000} - \cfrac{1}{3} \cdot \cfrac{B_{\rm{v}} \cdot 12^3}{50000} &= 0
\end{align*}
$$

$$
\begin{align*}
1) \quad 0.0637632 + 2.4 \cdot 10^{-4} \, M_{\rm{B}} - 0.001443 \, B_{\rm{v}} &= 0 \\
2) \quad 0.6044544 + 0.00144 \, M_{\rm{B}} - 0.01152 \, B_{\rm{v}} &= 0
\end{align*}
$$

Het oplossen van deze twee vergelijkingen geeft:

$$
M_{\rm{B}} = 196.56 \ \rm{kNm} \, (⌢) \qquad B_{\rm{v}} = 77.04 \ \rm{kN} \, (\uparrow)
$$
::::

% solution_end

::::{admonition} Opgave
:class: exercise

Bepaal de verticale oplegreactie in $\rm{A}$.

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Verticaal evenwicht geeft:

$$ \sum F_{\rm{v}} = A_{\rm{v}} - 77.76 - 38.88 + 77.04 = 0 \rightarrow A_{\rm{v}} = 39.62 \ \rm{kN} (\uparrow)$$

::::

% solution_end
