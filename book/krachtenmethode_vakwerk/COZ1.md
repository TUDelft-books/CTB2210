# COZ opgave 2.8

::::::{note}
Deze opgave kan in [ANS](https://ans.app/universities/1/courses/712480/assignments/1860496/go_to) gemaakt worden.

Als je nog geen toegang hebt tot deze toets, registreer je dan via [deze link](https://ans.app/accept/invitations/07b7bc5a-d334-43d7-9532-a1434730f6d7).

::::::

% https://ans.app/repo_questions/65438895/generator

Gegeven is de volgende constructie:

```{figure-start} ./COZ_data/constructie.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam
---

```

- $EA = 400 \, \rm{kN}$
- $EI \gg EA$

```{figure-end}
```

::::{admonition} Opgave
:class: exercise

Bepaal de zakking in $\rm{D}$ met behulp van de krachtenmethode en teken de vervormde constructie.

::::

::::{admonition} Uitwerking
:class: solution, dropdown

:::{todo}
[Bijwerken uitwerkingen](https://github.com/TUDelft-books/CTB2210/issues/74)
:::

Voor deze constructie is de inwendige statisch onbepaaldheid gelijk aan de uitwendig statisch onbepaaldheid.

```{figure} ./COZ_data/statisch_onbepaaldheid.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam
```

Er zijn 6 onbekenden en 5 evenwichtsvergelijkingen, daarmee is de constructie enkelvoudig statisch onbepaald.

Als voorbeeld is de krachtenmethode toegepast met het volgende statisch bepaalde systeem bekeken, maar andere methodes zijn ook goed:

```{figure} ./COZ_data/SB_systeem.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam
```
De vormveranderingsvoorwaarde behorende bij dit systeem is $w_{\rm{C}} = 0$. 

```{figure} ./COZ_data/FBD_C.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam
```

$$\sum {F_{\rm{v}}} = 0 \to N_{\rm{CE}} = C_{\rm{v}}$$

```{figure} ./COZ_data/FBD_AE.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam
```

$$\sum {T_{\rm{A}}} = 0 \to N_{\rm{BD}} = 66 - 3 \cdot C_{\rm{v}}$$

```{figure} ./COZ_data/AE.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam
```
Verlenging van staaf $\rm{BD}$ geeft:

$$w_{\rm{D}} = \cfrac{N_{\rm{BD}} \cdot l_{\rm{BD}}}{EA_{\rm{BD}}} = 0.495 - 0.0225 \cdot C_{\rm{v}}$$

Rotatie van starre staaf geeft:

$$w_{\rm{E}} = 3 \cdot w_{\rm{D}} = 1.485 - 0.0675 \cdot C_{\rm{v}}$$

```{figure} ./COZ_data/CE.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam
:number:
```

Verlenging van staaf geeft:

$$w_{\rm{C}} = w_{\rm{E}} - \Delta l_{\rm{CE}} = 1.485 - 0.075 \cdot C_{\rm{v}}$$

Oplossen van de vormveranderingsvoorwaarde geeft: $w_{\rm{C}} =0 \to C_{\rm{v}} = 19.8 \ \rm{ kN}$

Invullen in $w_{\rm{D}} = 0.495 - 0.0225 \cdot C_{\rm{v}}$ geeft: $w_{\rm{D}} = 49.5 \ \rm{ mm}$

De vervormde constructie is weergegeven in de onderstaande figuur.

```{figure} ./COZ_data/vervormde_constructie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam
:number:
```

::::
