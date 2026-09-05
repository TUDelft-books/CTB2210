# Begeleide oefening

Gegeven is de volgende constructie:

```{figure-start} lesoefeningen_data/structure.svg
---
align: center
figclass: sticky-margin
number:
name: rekoefening
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
---

```

- $EA = 2.5 \ \rm{MN}$
- $EI \gg EA$

```{figure-end}
```

Bepaal de oplegreacties en het snedekrachtenlijnen. Je gaat dit doen voor drie verschillende statisch onbepaalde krachten.

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

- Weghalen verticale oplegging bij $\rm{A}$
- Weghalen oplegging bij $\rm{B}$
- Weghalen verticale oplegging bij $\rm{C}$
- Toevoegen scharnier bij $\rm{B}$ (in doorgaande liggen $\rm{DBEG}$)
- Toevoegen scharnier bij $\rm{E}$ (in doorgaande liggen $\rm{DBEG}$)
- Splitsen constructie in pendelstaaf $\rm{AD}$
- Splitsen constructie in pendelstaaf $\rm{CE}$

:::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Schets de mogelijke vervormingen voor de optie van het weghalen van de verticale oplegging bij $\rm{A}$
---
=

```{figure} ./lesoefeningen_data/optie_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
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

Schets de mogelijke vervormingen voor de optie van het weghalen van deoplegging bij $\rm{B}$
---
=

```{figure} ./lesoefeningen_data/optie_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
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

Schets de mogelijke vervormingen voor de optie van het weghalen van de verticale oplegging bij $\rm{C}$
---
=

```{figure} ./lesoefeningen_data/optie_3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
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

Schets de mogelijke vervormingen voor de optie van het toevoegen van een scharnier bij $\rm{B}$ (in doorgaande liggen $\rm{DBEG}$)
---
=

```{figure} ./lesoefeningen_data/optie_4.svg
:align: center
:name: optie_4
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
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

Schets de mogelijke vervormingen voor de optie van het toevoegen van een scharnier bij $\rm{E}$ (in doorgaande liggen $\rm{DBEG}$)
---
=

```{figure} ./lesoefeningen_data/optie_5.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
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

Schets de mogelijke vervormingen voor de optie van het splitsen van de constructie in pendelstaaf $\rm{AD}$
---
=

```{figure} ./lesoefeningen_data/optie_6.svg
:align: center
:name: optie_6
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
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

Schets de mogelijke vervormingen voor de optie van het splitsen van de constructie in pendelstaaf $\rm{CE}$
---
=

```{figure} ./lesoefeningen_data/optie_7.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
:number:
```

---

:::::

::::{question} Opgave
:variant: multiple-select
:columns: 1
:admonition:
:class: exercise
:nocaption:
:showanswer:

Welke van de volgende is geen optie om de constructie statisch bepaald te maken?
---
[ ] Weghalen verticale oplegging bij $\rm{A}$
[x] Weghalen oplegging bij $\rm{B}$
> Inderdaad! Als je de hele oplegging weghaalt heb je een mechanisme wat naar links en rechts kan bewegen!
[ ] Weghalen verticale oplegging bij $\rm{C}$
[ ] Toevoegen scharnier bij $\rm{B}$ (in doorgaande liggen $\rm{DBEG}$)
[x] Toevoegen scharnier bij $\rm{E}$ (in doorgaande liggen $\rm{DBEG}$)
> Inderdaad, als je hier een scharnier toevoegt krijg je een mechanisme waarbij $\rm{EG}$ om $\rm{E}$ kan draaien
[ ] Splitsen constructie in pendelstaaf $\rm{AD}$
[ ] Splitsen constructie in pendelstaaf $\rm{CE}$
---

::::

## Statisch onbepaalde kracht $B_{\rm{v}}$

Gekozen wordt voor het volgende statisch onbepaalde systeem:

```{figure-start} lesoefeningen_data/stat_bepaald_Bv.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
---

```

- $EA = 2.5 \ \rm{MN}$
- $EI \gg EA$

```{figure-end}
```

::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

Wat is de vormveranderingsvoorwaarde? Gebruik de variabele $w_{\rm{...}}$ voor een verticale verplaatsing.
---
M[w_B = 0]
---

::::

:::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Schets de vervormde statisch onbepaalde constructie onder invloed van de $26 \, \rm{kN}$ en, afzonderlijk, van de statisch onbepaalde kracht.
---
=

::::{grid} 2
:class-container: center-grid

:::{grid-item}
:columns: auto

```{figure} ./lesoefeningen_data/optie_8.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
:number:
```

:::
:::{grid-item}

```{figure} ./lesoefeningen_data/optie_8_26.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
:number:
```

:::
::::

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
M[0.4]
M[15.6]
M[-0.6]
M[41.6]
M[0.0006]
M[-0.0416]
M[0.0004]
M[0.0156]
M[0.00052]
M[-0.01872]
^^^
? Bepaal achtereenvolgens de normaalkrachten en verplaatsingen als functie van $B_{\rm{v}}$.

- $ N_{\rm{AD}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $ N_{\rm{CE}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $ w_{\rm{E}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right)\cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (positief omhoog)
- $ w_{\rm{D}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right)\cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (positief omhoog)
- $ w_{\rm{B}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right)\cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (positief omhoog)
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
M[36]
^^^
? Los met de vormveranderingsvoorwaarde de statisch onbepaalde kracht op.

$ B_{v} = $ {gap} $\rm{kN}$ (positief omhoog)
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
M[30]
M[20]
M[-2]
M[3]
M[0]
^^^
? Los nu ook de normaalkrachten en verplaatsingen op.

- $ N_{\rm{AD}} = $ {gap} $ \rm{kN}$
- $ N_{\rm{CE}}  = $ {gap} $ \rm{kN}$
- $ w_{\rm{E}} = $ {gap} $ \rm{cm}$ (positief omhoog)
- $ w_{\rm{D}} = $ {gap} $ \rm{cm}$ (positief omhoog)
- $ w_{\rm{B}} = $ {gap} $ \rm{cm}$ (positief omhoog)
---

::::

## Statisch onbepaald moment $M_{\rm{B}}$

Nu wordt gekozen voor het volgende statisch onbepaalde systeem:

```{hide-sticky-margin}
```
```{figure-start} lesoefeningen_data/stat_bepaald_Mb.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
---

```

- $EA = 2.5 \ \rm{MN}$
- $EI \gg EA$

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
DS[{φ};w]
DS[{B aan de kant van BD};D]
DS[{φ};w]
DS[G;E aan de kant van EG;E aan de kant van BE;{B aan de kant van BE}]
^^^
? Wat is de vormveranderingsvoorwaarde?

{gap}$(${gap}$) = ${gap}$(${gap}$)$
---

::::

De vervormde constructie onder invloed van de statisch onbepaalde kracht $M_{\rm{B}}$ heb je al getekend in een van de eerste oefeningen:

:::{fetch} {numref}`optie_4`
:::

:::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Schets de vervormde statisch onbepaalde constructie onder invloed van de $26 \, \rm{kN}$. 
---
=

```{figure} ./lesoefeningen_data/optie4_26.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
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
MAPE[-1/3;0.01;2]
M[0]
M[0.5]
M[65]
MAPE[1/9000;0.00001;2]
M[0]
M[-0.00025]
M[-0.0325]
^^^
? Bepaal achtereenvolgens de normaalkrachten en verplaatsingen als functie van $M_{\rm{B}}$.

- $ N_{\rm{AD}} \left( M_{\rm{B}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kNm}}\right) \cdot M_{\rm{B}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $ N_{\rm{CE}} \left( M_{\rm{B}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kNm}}\right) \cdot M_{\rm{B}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $ \varphi _ {\rm{B}} ^{\rm{DB}} \left( M_{\rm{B}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right)\cdot M_{\rm{B}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$ (↺)
- $ \varphi _ {\rm{B}} ^{\rm{BE}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right)\cdot M_{\rm{B}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$ (↺)
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
M[-90]
^^^
? Los met de vormveranderingsvoorwaarde de statisch onbepaalde kracht $M_{\rm{B}}$ op.

$ M_{v} = $ {gap} $\rm{kNm}$ (positief geeft trek aan de onderkant, rond af op gehele getallen)
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
M[30]
M[20]
M[-0.01]
^^^
? Los nu ook de normaalkrachten en rotatie op.

- $ N_{\rm{AD}} = $ {gap} $ \rm{kN}$
- $ N_{\rm{CE}}  = $ {gap} $ \rm{kN}$
- $ \varphi_{\rm{B}} = $ {gap} $ \rm{rad}$ (↺)
---

::::

## Statisch onbepaalde normaalkracht $N_{\rm{AD}}$

Nu wordt gekozen voor het volgende statisch onbepaalde systeem:

```{hide-sticky-margin}
```
```{figure-start} lesoefeningen_data/stat_bepaald_N_AD.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
---

```

- $EA = 2.5 \ \rm{MN}$
- $EI \gg EA$

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
DS[φ;{w}]
DS[{D aan de kant van AD};D aan de kant van BD;B aan de kant van DB]
DS[φ;{w}]
DS[{D aan de kant van BD};B aan de kant van DB]
^^^

? Wat is de vormveranderingsvoorwaarde?

{gap}$(${gap}$) = ${gap}$(${gap}$)$
---

::::

De vervormde constructie onder invloed van de statisch onbepaalde kracht $N_{\rm{AD}}$ heb je al getekend in een van de eerste oefeningen:

:::{fetch} {numref}`optie_6`
:::

:::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Schets de vervormde statisch onbepaalde constructie onder invloed van de $26 \, \rm{kN}$.
---
=

```{figure} ./lesoefeningen_data/optie6_26.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
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
M[-1.5]
M[65]
M[0.015]
M[-0.0650]
M[0.001]
M[0]
M[-0.00225]
M[0.09750]
^^^
? Bepaal achtereenvolgens de normaalkrachten en verplaatsingen als functie van $N_{\rm{AD}}$.

- $ N_{\rm{CE}} \left( N_{\rm{AD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot N_{\rm{AD}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $ w_{\rm{E}} \left( N_{\rm{AD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right)\cdot N_{\rm{AD}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (positief omhoog)
- $ w_{\rm{D}} ^{\rm{AD}} \left( N_{\rm{AD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right)\cdot N_{\rm{AD}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (positief omhoog)
- $ w_{\rm{D}} ^{\rm{BD}} \left( N_{\rm{AD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right)\cdot N_{\rm{AD}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (positief omhoog)
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
M[30]
^^^
? Los met de vormveranderingsvoorwaarde de statisch onbepaalde kracht $N_{\rm{AD}}$ op.

$ N_{\rm{AD}} = $ {gap} $\rm{kN}$
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
M[20]
M[-2]
M[3]
M[3]
^^^
? Los nu ook de normaalkracht $N_{\rm{CE}}$ en de verplaatsingen op.

- $ N_{\rm{CE}}  = $ {gap} $ \rm{kN}$
- $ w_{\rm{E}} = $ {gap} $ \rm{cm}$ (positief omhoog)
- $ w_{\rm{D}} ^{\rm{AD}} = $ {gap} $ \rm{cm}$ (positief omhoog)
- $ w_{\rm{D}} ^{\rm{BD}} = $ {gap} $ \rm{cm}$ (positief omhoog)
---

::::

## Vervormde constructie

Nu we de constructie op meerdere manieren statisch bepaald hebben gemaakt, kunnen we een of meerdere van de uitwerkingen gebruiken om de vervormde statisch onbepaalde constructie te tekenen.

:::{fetch} {numref}`rekoefening`
:::

::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Teken de vervormde **statisch onbepaalde** constructie op schaal.
---
=
```{figure} lesoefeningen_data/verplaatsingen.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
```

---

::::
