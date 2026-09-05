# Begeleide oefening 2

Gegeven is de volgende constructie

```{figure} ./lesoefeningen_data/structure.svg
:align: center
:figclass: sticky-margin
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2
```

Bepaal de krachtsverdeling en verplaatsingen.

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[1]
^^^
?
De constructie is {gap}ste/de graads inwendig statisch onbepaald
---

::::

We overwegen de volgende alternatieven als statisch onbepaalde constructie:

- Inklemming aanpassen naar scharnierende oplegging bij $\rm{A}$ en toevoegen scharnier bij $\rm{C}$
- Weghalen verticale oplegging bij $\rm{A}$
- Inklemming aanpassen naar scharnierende oplegging bij $\rm{A}$
- Toevoegen scharnier bij $\rm{C}$
- Weghalen verticale oplegging bij $\rm{B}$

:::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Schets de mogelijke vervormingen voor de optie van het aanpassen van de inklemming naar een scharnierende oplegging bij $\rm{A}$ en het toevoegen van een scharnier bij $\rm{C}$.
---
=

```{figure} ./lesoefeningen_data/optie_5.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2
:number:
```

---

:::::

:::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Schets de mogelijke vervormingen voor de optie van het weghalen van de verticale oplegging bij $\rm{A}$.
---
=

```{figure} ./lesoefeningen_data/optie_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2
:number:
```

---

:::::

:::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Schets de mogelijke vervormingen voor de optie van het aanpassen van de inklemming naar een scharnierende oplegging bij $\rm{A}$.
---
=

```{figure} ./lesoefeningen_data/optie_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2
:number:
```

---

:::::

:::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Schets de mogelijke vervormingen voor de optie van het toevoegen van een scharnier bij $\rm{C}$.
---
=

```{figure} ./lesoefeningen_data/optie_3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2
:name: optie3_balk
:number:
```

---

:::::

:::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Schets de mogelijke vervormingen voor de optie van het weghalen van de verticale oplegging bij $\rm{B}$.
---
=

```{figure} ./lesoefeningen_data/optie_4.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2
:number:
```

---

:::::

::::{question} Opgave
:variant: multiple-select
:admonition:
:class: exercise
:nocaption:
:showanswer:

Welke van de volgende is geen optie om de constructie statisch bepaald te maken als je de constructie op wilt lossen? Sluit ook de gevallen uit waarvoor geen vergeet-me-nietjes zijn of de verplaatsingen relatief complex zijn.
---
[x] Inklemming aanpassen naar scharnierende oplegging bij $\rm{A}$ en toevoegen scharnier bij $\rm{C}$
> Inderdaad, hier ontstaat een mechanisme dus dit is geen geldig statisch bepaald systeem
[x] Weghalen verticale oplegging bij $\rm{A}$
> Inderdaad, er is geen vergeet-me-nietje die voor dat statisch bepaalde systeem de verplaatsingen geeft
[x] Inklemming aanpassen naar scharnierende oplegging bij $\rm{A}$
> Inderdaad, er is geen vergeet-me-nietje die voor dat statisch bepaalde systeem de verplaatsingen geeft
[ ] Toevoegen scharnier bij $\rm{C}$
> Er zijn wel degelijk vergeet-me-nietjes voor deze situatie, maar het rechter deel zal echter ook nog roteren rondom $\rm{B}$ dus dat is wel wat complexer dan één van de ander opties.
[ ] Weghalen verticale oplegging bij $\rm{B}$
---

::::


## Statisch bepaald systeem 1

Ga uit van het volgende statisch bepaalde systeem:

```{figure} ./lesoefeningen_data/SB-1.svg
:align: center
:figclass: sticky-margin
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2

```

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-1]
M[54]
M[-3]
M[0]
M[-1]
M[0]
M[-0.0125]
M[0.27]
M[0.0075]
M[-0.135]
M[-0.045]
M[0.675]
^^^
? Los de krachtsverdeling en verplaatsingen van deze constructie uit als functie van $B_{\rm{v}}$, met  $B_{\rm{v}}$ en $V$ in $\rm{kN}$, $M_{\rm{C}}$ in $\rm{kNm}$, $\varphi_{\rm{B}}$ in $\rm{rad}$, $w_{\rm{A}}$ in $\rm{m}$ en het gegeven assenstelsel.

- $V_{\rm{C}}^{\rm{AC}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $M_{\rm{C}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kNm}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kNm}\right)$
- $V_{\rm{B}}^{\rm{BC}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $w_{\rm{C}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$
- $\varphi_{\rm{C}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$
- $w_{\rm{B}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$

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
M[15]
^^^
? Los de vormveranderingsvoorwaarde op om $B_{\rm{v}}$ te vinden.

$B_{\rm{v}}= $ {gap} $\rm{kN}$ (↑)

---

::::


## Statisch bepaald systeem 2

Ga nu uit van het volgende statisch bepaalde systeem:

```{figure} ./lesoefeningen_data/SB-2.svg
:align: center
:figclass: sticky-margin
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2

```

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
MAPE[-1/3;0.1;2]
M[0]
MAPE[-1/3;0.1;2]
M[54]
M[0.0025]
M[-0.135]
M[-1/240;0.0001;4]
M[0.27]
M[-0.0025]
> Houd rekening met de rotatie van BC door de zakking van C
M[0.09]
> Houd rekening met de rotatie van BC door de zakking van C
^^^
? Los de krachtsverdeling en verplaatsingen van deze constructie uit als functie van $M_{\rm{C}}$, met $M_{\rm{C}}$ in $\rm{kNm}$, $B_{\rm{v}}$ en $V_{\rm{C}}^{\rm{AC}}$ in $\rm{kN}$, $\varphi$ in $\rm{rad}$, $w_{\rm{C}}$ in $\rm{m}$ en het gegeven assenstelsel.

- $B_{\rm{v}} \left( M_{\rm{C}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kNm}}{\rm{kNm}}\right) \cdot M_{\rm{C}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $V_{\rm{C}}^{\rm{AC}} \left( M_{\rm{C}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kNm}}\right) \cdot M_{\rm{C}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $\varphi_{\rm{C}}^{\rm{AC}} \left( M_{\rm{C}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{C}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$
- $w_{\rm{C}} \left( M_{\rm{C}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kNm}}\right) \cdot M_{\rm{C}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$
- $\varphi_{\rm{C}}^{\rm{BC}} \left( M_{\rm{C}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{C}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$

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
? Los de vormveranderingsvoorwaarde op om $M_{\rm{C}}$ te vinden.

$M_{\rm{C}}= $ {gap} $\rm{kNm}$

---

::::


## Krachtsverdeling en verplaatsingen statisch onbepaald systeem

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-39]
M[72]
M[-15]
M[-72]
M[45]
M[39]
M[-15]
M[82.5]
M[-0.0225]

^^^
? Los nu de volledige krachtsverdeling en verplaatsingen op met de resultaten van een of beide van je statisch onbepaalde systemen.

- $A_{\rm{v}}= $ {gap} $\rm{kN}$
- $A_{\rm{m}}= $ {gap} $\rm{kNm}$
- $B_{\rm{v}}= $ {gap} $\rm{kN}$
- $M_{\rm{A}}= $ {gap} $\rm{kNm}$
- $M_{\rm{C}}= $ {gap} $\rm{kNm}$
- $V_{\rm{AC}}= $ {gap} $\rm{kN}$
- $V_{\rm{CB}}= $ {gap} $\rm{kN}$
- $w_{\rm{C}}= $ {gap} $\rm{mm}$
- $\varphi_{\rm{C}}= $ {gap} $\rm{rad}$

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
MAPE[24/13;0.01;3]

^^^
? Waar bevindt zich het buigpunt van de constructie? (waar de kromming wisselt van teken)

$x_{\rm{buigpunt}}= $ {gap} $\rm{m}$

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

```{figure} ./lesoefeningen_data/disp.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk
```

---

::::
