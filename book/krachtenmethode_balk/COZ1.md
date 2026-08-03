# COZ opgave 3.1

::::::{note}
Deze opgave kan in ANS gemaakt worden.
:::{todo}
[Toevoegen link naar ANS toets.](https://github.com/TUDelft-books/CTB2210/issues/90)
:::
::::::

% https://ans.app/repo_questions/32111228/generator

Gegeven is de volgende constructie:

```{figure} ./COZ1_data/constructie.svg
---
align: center
number:
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/COZ_balk_q
---

```

::::{admonition} Opgave
:class: exercise

Bepaal de het moment in $\rm{B}$.

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Er is gekozen voor de volgende statisch bepaalde constructie.
```{figure} ./COZ1_data/FBD1.svg
---
align: center
number:
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/COZ_balk_q
---

```
De vormveranderingsvoorwaarde geeft nu de volgende vergelijking die kan worden opgelost voor $M_{\rm{B}}$:

$$
\begin{align*}
\cfrac{1}{24}\cfrac{ql^3}{EI} - \cfrac{1}{3}\cfrac{M_{\rm{B}} l}{EI} &= -\cfrac{1}{24}\cfrac{ql^3}{EI} - \cfrac{1}{3}\cfrac{M_{\rm{B}} l}{EI} \\
\cfrac{21}{2500} - 6.67 \cdot 10^{-5} \, M_{\rm{B}} &= -0.0189 + 5 \cdot 10^{-5} \, M_{\rm{B}} \\
0.0084 + 0.0189 &= \left( 5 \cdot 10^{-5} + 6.67 \cdot 10^{-5} \right) M_{\rm{B}} \\
M_{\rm{B}} &= 234 \ \rm{kNm} (⌢)
\end{align*}
$$

::::

% solution_end

::::{admonition} Opgave
:class: exercise

Bepaal de verticale oplegreactie in $\rm{B}$.

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Met de bekende interne kracht $M_{\rm{B}}$ kan met het volgende vrijlichaamsschema $A_{\rm{v}}$ worden bepaald:

```{figure} ./COZ1_data/FBD2.svg
---
align: center
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/COZ_balk_q
---

```

$$
\begin{align*}
\sum \left. M \right| _ {\rm{B}} ^{\rm{AB}} &= 0 \\
- A_{\rm{v}} \cdot 4 + 63 \cdot 4 \cdot 2 - 234 &= 0 \\
A_{\rm{v}} &= 67.5 \ \rm{kN} \, (\uparrow)
\end{align*}
$$

Nu $A_{\rm{v}}$ bekend is kan $B_{\rm{v}}$ worden opgelost met een momentensom om $\rm{C}$:

$$
\begin{align*}
\sum \left. T \right| _ {\rm{C}} ^{\rm{AC}} &= 0 \\
-10 \cdot A_{\rm{v}} + 63 \cdot 4 \cdot 8 + 150 \cdot 6 + 84 \cdot 6 \cdot 3 - B_{\rm{v}} \cdot 6 &= 0 \\
B_{\rm{v}} &= 625.5 \ \rm{kN} \, (\uparrow)
\end{align*}
$$

::::

% solution_end

::::{admonition} Opgave
:class: exercise

Bepaal het moment halverwege $\rm{AB}$.

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Het punt halverwege $\rm{AB}$ wordt $\rm{D}$ genoemd, waar de volgende snede wordt gemaakt:

```{figure} ./COZ1_data/FBD3.svg
---
align: center
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/COZ_balk_q
---

```

$$
\begin{align*}
\sum \left. M \right| _ {\rm{D}} &= 0 \\
-67.5 \cdot 2 + 63 \cdot 2 \cdot 1 + M_{\rm{B}} &= 0 \\
M_{\rm{B}} &= 9 \ \rm{kNm} \, (⌣)
\end{align*}
$$

::::

% solution_end

::::{admonition} Opgave
:class: exercise

Bepaal het moment halverwege $\rm{BC}$.

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Het punt halverwege $\rm{BC}$ wordt $\rm{E}$ genoemd, waar de volgende snede wordt gemaakt:

```{figure} ./COZ1_data/FBD4.svg
---
align: center
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/COZ_balk_q
---

```

$$
\begin{align*}
\sum \left. M \right| _ {\rm{E}} &=  0 \\
-67.5 \cdot 7 + 63 \cdot 4 \cdot 5 - 625.5 \cdot 3 + 150 \cdot 3 + 84 \cdot 3 \cdot 1.5 + M_{\rm{E}} &= 0 \\
M_{\rm{E}} &= 261 \ \rm{kNm} \, (⌣)
\end{align}*
$$

::::

% solution_end
