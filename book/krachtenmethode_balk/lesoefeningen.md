````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze pagina is aangepast van [deze instructie](https://oit.tudelft.nl/CEG-mechanics-BSc/NL/statically_inderminate/force_method/bending.html) van {cite:ts}`CEG_mechanics_BSc`.

```
```` 

# Begeleide oefening 1

Gegeven is de volgende constructie:

```{figure-start} ./bending_data/Example.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
---

```

- $EI = \cfrac{16}{3} \ \rm{MNm^2}$
- $EA \gg EI $

```{figure-end}
```

Bepaal de krachtsverdeling en verplaatsingen.

Ga uit van het volgende statisch bepaalde systeem:

```{figure-start} ./bending_data/SB-systeem2.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
---

```

- $EI = \cfrac{16}{3} \ \rm{MNm^2}$
- $EA \gg EI $

```{figure-end}
```

In de instructie werden al de vervormingen ten gevolge van de kracht $A_{\rm{v}}$ geschetst.

:::{fetch} {numref}`optie2_balk`
:::

:::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Schets de mogelijke vervormingen ten gevolge van verdeelde belasting op de statisch bepaalde constructie.
---
=

```{figure} ./bending_data/disp_25.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
:number:
```

---

:::::

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[4]
M[-200]
M[0.0015]
M[-0.075]
M[0.01]
M[-0.45]
^^^
? Bepaal de normaalkrachten in alle staven als functie van $A_{\rm{v}}$, met  $A_{\rm{v}}$ in $\rm{kN}$, $M_{\rm{B}}$ in $\rm{kNm}$, $\varphi_{\rm{B}}$ in $\rm{rad}$ en $w_{\rm{A}}$ in $\rm{m}$.

- $M_{\rm{B}} \left( A_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kNm}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kNm}\right)$ (◡)
- $\varphi_{\rm{B}} \left( A_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$ (↻)
- $w_{\rm{A}} \left( A_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (↑)

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
M[45]
^^^
? Los de vormveranderingsvoorwaarde op om $A_{\rm{v}}$ te vinden.

$A_{\rm{v}}= $ {gap} $\rm{kN}$ (↑)

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
MAPE[175/3;0.1;4]
MAPE[10/3;0.1;2]
M[-20]
M[40]
M[-0.0075]
M[11.875]
M[-8.4375]

^^^
? Los nu de andere oplegreacties op en bepaal de momenten en verplaatsingen.

- $B_{\rm{v}}= $ {gap} $\rm{kN}$ (↑)
- $C_{\rm{v}}= $ {gap} $\rm{kN}$ (↑)
- $M_{\rm{B}}= $ {gap} $\rm{kNm}$ (◠)
- $M_{\rm{halverwege \ AB}}= $ {gap} $\rm{kNm}$ (◠)
- $\varphi_{\rm{B}}= $ {gap} $\rm{rad}$ (↻)
- $w_{\rm{halverwege \ AB}}= $ {gap} $\rm{mm}$ (↓)
- $w_{\rm{halverwege \ BC}}= $ {gap} $\rm{mm}$ (↓)

---

::::


::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Teken de vervormde statisch **onbepaalde** constructie op schaal.
---
=

```{figure} ./bending_data/disp.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
```

Dit is precies dezelfde tekening als wanneer deze werd opgelost met behulp van hoekveranderingsvergelijkingen.
---

::::
