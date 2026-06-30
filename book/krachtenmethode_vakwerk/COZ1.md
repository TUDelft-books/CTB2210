# COZ opgave 2.4

::::::{note}
Deze opgave kan in ANS gemaakt worden.
:::{todo}
[Toevoegen link naar ANS toets.](https://github.com/TUDelft-books/CTB2210/issues/74)
:::
::::::

% https://ans.app/repo_questions/...

Gegeven is de volgende constructie:

```{figure-start} ./COZ_data/constructie.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam
---

```

- $EA = 400 \, \rm{kN}$
- $EI \gg EA$

```{figure-end}
```

::::{admonition} Opgave
:class: exercise

Bepaal de zakking in $\rm{G}$ met behulp van de krachtenmethode en teken de vervormde constructie.

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

:::{todo}
[Bijwerken uitwerkingen](https://github.com/TUDelft-books/CTB2210/issues/74)
:::

Voor deze constructie is de inwendige statisch onbepaaldheid gelijk aan de uitwendig statisch onbepaaldheid.

```{figure} ./COZ_data/statisch_onbepaaldheid.svg
:align: center
:number:
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam
```

Er zijn 9 onbekenden en 8 evenwichtsvergelijkingen, waarmee is de constructie enkelvoudig statisch onbepaald.

Als voorbeeld is de krachtenmethode toegepast met het volgende statisch bepaalde system bekeken, maar andere methodes zijn ook goed:

```{figure} ./COZ_data/SB_5.svg
:align: center
:number:
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam
```

```{figure} ./COZ_data/FBD_D.svg
:align: center
:number:
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam
```

$$\sum {F_{\rm{v}}} = 0 \to N_{\rm{DK}} = D_{\rm{v}}$$

```{figure} ./COZ_data/FBD_AK.svg
:align: center
:number:
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam
```

$$\sum {T_{\rm{A}}} = 0 \to N_{\rm{OG}} = 66 - 3 \cdot D_{\rm{v}}$$

```{figure} ./COZ_data/BC.svg
:align: center
:number:
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam
```

Vergeet-me-nietje geeft:

$$w_{\rm{O}} = 0.022 - 0.001 \cdot D_{\rm{v}}$$

```{figure} ./COZ_data/OG.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam
:number:
```

Verlenging van staaf geeft:

$$w_{\rm{G}} = 0.22 - 0.01 \cdot D_{\rm{v}}$$

```{figure} ./COZ_data/AK.svg
:align: center
:number:
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam
```

Rotatie van starre staaf geeft:

$$w_{\rm{K}} = 0.66 - 0.03 \cdot D_{\rm{v}}$$

```{figure} ./COZ_data/DK.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam
:number:
```

Verlenging van staaf geeft:

$$w_{\rm{D}} = 0.66 - 0.033 \cdot D_{\rm{v}}$$

Oplossen van de vormveranderingsvoorwaarde geeft: $w_{\rm{D}} =0 \to D_{\rm{v}} = 20 \ \rm{ kN}$ (dit wordt 19.8 kN zonder het balkje bovenin)

Invullen in $w_{\rm{G}} = 0.22 - 0.01 \cdot D_{\rm{v}}$ geeft: $w_{\rm{G}} = 20 \ \rm{ mm}$ (dit wordt 55 mm zonder het balkje bovenin)

:::{todo}
[Toevoegen vervormde constructie](https://github.com/TUDelft-books/CTB2210/issues/74)
:::

::::

% solution_end
