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

Welke van de volgende is geen optie om de constructie statisch bepaald te maken als je de constructie op wilt lossen? Sluit ook de gevallen uit waarvoor geen vergeet-me-nietjes zijn.
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

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Met behulp van het gegeven vrijlichaamsschema kunnen de dwarskracht net links van C, het moment in C en de dwarskracht net links van B worden bepaald als functie van $B_{\rm{v}}$:

$$ V_{\rm{C}}^{\rm{AC}} \left( B_{\rm{v}} \right) = -1 \cdot B_{\rm{v}} + 54 $$
$$ M_{\rm{C}} \left( B_{\rm{v}} \right) = -3 \cdot B_{\rm{v}} $$ 
$$ V_{\rm{B}}^{\rm{BC}} \left( B_{\rm{v}} \right) = -1 \cdot B_{\rm{v}} $$

De zakking, $w_{\rm{C}}$, en rotatie, $\varphi_{\rm{C}}$, in C kunnen worden gevonden door de kracht $B_{\rm{v}}$ te verplaatsen van B naar C met toevoeging van een moment, zie het onderstaande vrijlichaamsschema:

```{figure} ./lesoefeningen_data/VrijlichaamsschemaAC_1.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2
```

Met behulp van de vergeet-mij-nietjes voor een uitkragende ligger belast door een kracht en een koppel wordt gevonden:

$$ w_{\rm{C}} \left( B_{\rm{v}} \right) = \cfrac{\left(54 - B_{\rm{v}} \right) \cdot 3^3}{3 \cdot 1800} - \cfrac{3 \cdot B_{\rm{v}} \cdot 3^2}{2 \cdot 1800} = -0.0125 \cdot B_{\rm{v}} + 0.27 $$
$$ \varphi_{\rm{C}} \left( B_{\rm{v}} \right) = -\cfrac{\left(54 - B_{\rm{v}} \right) \cdot 3^2}{2 \cdot 1800} + \cfrac{3 \cdot B_{\rm{v}} \cdot 3}{1800} = 0.0075 \cdot B_{\rm{v}} - 0.135 $$

De zakking in B, $w_{\rm{B}}$, is dan gelijk aan:

$$ w_{\rm{B}} \left( B_{\rm{v}} \right) = w_{\rm{C}} - \varphi_{\rm{C}} \cdot 3 - \cfrac{B_{\rm{v}} \cdot 3^3}{3 \cdot 900} = -0.045 \cdot B_{\rm{v}} + 0.675 $$

::::

% solution_end

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

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

De vormveranderingsvoorwaarde is: $w_{\rm{B}} = -0.045 \cdot B_{\rm{v}} + 0.675 = 0$. 

Hieruit volgt dat $B_{\rm{v}} = 15 \rm{kN}$

::::

% solution_end

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


% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

De uitdrukkingen voor $B_{\rm{v}}$ en $V_{\rm{C}}^{\rm{AC}}$ kunnen worden afgeleid uit evenwicht van het deel BC.

$$ \sum \left. T \right| _ {\rm{C}} ^{\rm{CB}} = - 3 \cdot B_{\rm{v}} - M_{\rm{C}} = 0 \rightarrow B_{\rm{v}} = - \cfrac{1}{3} \cdot M_{\rm{C}} $$
$$ V_{\rm{C}}^{\rm{AC}} = B_{\rm{v}} + 54 = - \cfrac{1}{3} \cdot M_{\rm{C}} + 54 $$

De rotatie net links van C, $\varphi_{\rm{C}}^{\rm{AC}}$, en de zakking in C $w_{\rm{C}}$ kunnen worden bepaald met de vergeet-mij-nietjes voor een uitkragende ligger belast door een koppel en door een puntlast, zie het onderstaande vrijlichaamsschema:

```{figure} ./lesoefeningen_data/VrijlichaamsschemaAC_2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_balk_2
```

$$ \varphi_{\rm{C}}^{\rm{AC}} \left( M_{\rm{C}} \right) = \cfrac{M_{\rm{C}} \cdot 3}{1800} - \cfrac{\left( - \cfrac{1}{3} \cdot M_{\rm{C}} + 54 \right) \cdot 3^2}{2 \cdot 1800} = 0.0025 \cdot M_{\rm{C}} - 0.135 $$

$$ w_{\rm{C}} \left( M_{\rm{C}} \right) = - \cfrac{M_{\rm{C}} \cdot 3^2}{2 \cdot 1800} + \cfrac{\left( - \cfrac{1}{3} \cdot M_{\rm{C}} + 54 \right) \cdot 3^3}{3 \cdot 1800} = -0.00417 \cdot M_{\rm{C}} + 0.27 $$

De rotatie net rechts van C, $\varphi_{\rm{C}}^{\rm{BC}}$, wordt veroorzaakt door buiging van deel BC ten gevolge van $M_{\rm{C}}$ en door de zakking in C, $w_{\rm{C}}$:

:::{fetch} {numref}`optie3_balk`
:::

De rotatie ten gevolge van de buiging kan worden bepaald met behulp van het vergeet-mij-nietje voor een ligger op twee steunpunten belast door een koppel. 

$$ \varphi_{\rm{C}}^{\rm{BC}} \left( M_{\rm{C}} \right) = \cfrac{w_{\rm{C}}}{3} - \cfrac{M_{\rm{C}} \cdot 3}{3 \cdot 900} = 0.0025 \cdot M_{\rm{C}} -0.09 $$

::::

% solution_end

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

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

De vormveranderingsvoorwaarde is: $\varphi_{\rm{C}}^{\rm{AC}} = \varphi_{\rm{C}}^{\rm{BC}} \rightarrow 0.0025 \cdot M_{\rm{C}} - 0.135 = -0.0025 \cdot M_{\rm{C}} + 0.09$. 

Hieruit volgt $M_{\rm{C}} = 45 \rm{kNm}$. 

::::

% solution_end

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

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

De helling van de momentenlijn tussen $\rm{A}$ en $\rm{C}$ is gelijk aan de dwarskracht $V_{\rm{AC}} = 39 \, \rm{kN}$. De momentenlijn is dus $0$ bij $x_{\rm{buigpunt}} = \cfrac{M_{\rm{A}}}{V_{\rm{AC}}} = \cfrac{72}{39} = \cfrac{24}{13} \approx 1.85 \, \rm{m}$

::::

% solution_end

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
