````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze oefening is aangepast de [les van 20 september](https://oit.tudelft.nl/CT1000/2024/week_3/session_3/intro.html) van {cite:ts}`CT1000_2024`

```
````



# Begeleide oefening

Gegeven is de volgende constructie:

```{figure-start} lesoefeningen_2_data/structure.svg
:align: center
:number:
:figclass: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
```

$EA = 3750 \ \rm{kN}$

```{figure-end}
```

Bepaal de verplaatsingen van de knopen.

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

- Weghalen horizontale oplegging bij $\rm{B}$
- Weghalen verticale oplegging bij $\rm{B}$
- Splitsen constructie in pendelstaaf $\rm{AC}$
- Splitsen constructie in pendelstaaf $\rm{AD}$
- Splitsen constructie in pendelstaaf $\rm{CE}$
- Splitsen constructie in pendelstaaf $\rm{DE}$
- Toevoegen scharnier halverwege $\rm{CD}$

:::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Schets de mogelijke vervormingen voor de optie van het weghalen van de horizontale oplegging bij $\rm{B}$.
---
=

```{figure} ./lesoefeningen_2_data/optie_1.svg
:align: center
:name: optie_1
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
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

```{figure} ./lesoefeningen_2_data/optie_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
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

Schets de mogelijke vervormingen voor de optie van het splitsen van de pendelstaaf $\rm{AC}$.
---
=

```{figure} ./lesoefeningen_2_data/optie_3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
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

Schets de mogelijke vervormingen voor de optie van het splitsen van de pendelstaaf $\rm{AD}$.
---
=

```{figure} ./lesoefeningen_2_data/optie_4.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
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

Schets de mogelijke vervormingen voor de optie van het splitsen van de pendelstaaf $\rm{CE}$.
---
=

```{figure} ./lesoefeningen_2_data/optie_5.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
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

Schets de mogelijke vervormingen voor de optie van het splitsen van de pendelstaaf $\rm{DE}$.
---
=

```{figure} ./lesoefeningen_2_data/optie_7.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
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

Schets de mogelijke vervormingen voor de optie van het toevoegen van een scharnier halverwege $\rm{CD}$.
---
=

```{figure} ./lesoefeningen_2_data/optie_6.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
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
[ ] Weghalen horizontale oplegging bij $\rm{B}$
[x] Weghalen verticale oplegging bij $\rm{B}$
> Inderdaad! Als je de hele oplegging weghaalt heb je een mechanisme dat kan roteren rondom $\rm{A}$.
[x] Splitsen constructie in pendelstaaf $\rm{AC}$
> Inderdaad, als je deze pendelstaaf weghaalt krijg je een mechanisme dat kan roteren om $\rm{A}$ en $\rm{B}$.
[ ] Splitsen constructie in pendelstaaf $\rm{AD}$
[x] Splitsen constructie in pendelstaaf $\rm{CE}$
> Inderdaad, als je deze pendelstaaf weghaalt krijg je een mechanisme dat can roteren om $\rm{A}$ en $\rm{B}$.
[x] Splitsen constructie in pendelstaaf $\rm{DE}$
> Inderdaad, als je deze pendelstaaf weghaalt krijg je een mechanisme dat kan roteren om $\rm{A}$ en $\rm{B}$.
[x] Toevoegen scharnier halverwege $\rm{CD}$
> Inderdaad, als je deze pendelstaaf weghaalt krijg je een lokaal mechanisme dat kan roteren om $\rm{C}$ en $\rm{D}$.
---

::::

We kiezen voor een statisch onbepaalde kracht $B_{\rm{h}}$ (naar links positief) met de vormveranderingsvoorwaarde $w_{\rm{B,h}} = 0 $.

```{figure-start} lesoefeningen_2_data/SD.svg
:align: center
:figclass: sticky-margin
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2

```

$EA = 3750 \ \rm{kN}$

```{figure-end}
```

Hierboven schetste je al de vervormingen ten gevolge van de kracht $B_{\rm{h}}$:

:::{fetch} {numref}`optie_1`
:::

:::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Schets de mogelijke vervormingen ten gevolge van de kracht van $\rm{20} \, \rm{kN}$.
---
=

```{figure} ./lesoefeningen_2_data/displaced_20_cor_without.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
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
M[0]
M[-18.75]
M[-1]
M[11.25]
M[0]
M[-6.25]
M[0]
M[-7.5]
M[0]
M[6.25]
M[-1]
M[3.75]
M[0]
M[-6.25]
^^^
? Bepaal de normaalkrachten in alle staven als functie van $B_{\rm{h}}$, met  $B_{\rm{h}}$ en $N$ in $\rm{kN}$.

- $N_{\rm{AC}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{h}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $N_{\rm{AD}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{h}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $N_{\rm{CD}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{h}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $N_{\rm{CE}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{h}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $N_{\rm{DE}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{h}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $N_{\rm{DB}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{h}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $N_{\rm{BE}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{h}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$


---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Allereerst worden de oplegreacties berekend:

```{figure} lesoefeningen_2_data/FBD_sol.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2

```

De staafkrachten kunnen nu worden opgelost, beginnende bij de krachten in de staven $\rm{BE}$ en $\rm{BD}$:

```{figure} lesoefeningen_2_data/FBD_B.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
```

$$
\sum {{F_{\rm{v}}} = 0}  \to {N_{{\rm{BE}}}} = -6.25{\, \rm{ kN}}\\
\sum {{F_{\rm{h}}} = 0}  \to {N_{{\rm{BD}}}} =  3.75 - {B_{\rm{h}}}
$$

Dit geeft:

```{figure} lesoefeningen_2_data/FBD_B_sol.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
```

Vervolgens wordt een snede gemaakt door de staven $\rm{AD}$, $\rm{CD}$ en $\rm{CE}$:

```{figure} lesoefeningen_2_data/FBD_AC.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
```

$$
\sum {{F_{\rm{v}}} = 0}  \to {N_{{\rm{CD}}}} =  - 6.25{\rm{ kN}}\\
{\sum {\left. T \right|} _{\rm{D}}} = 0 \to {N_{CE}} =  - 7.5{\rm{ kN}}\\
\sum {{F_{\rm{h}}} = 0}  \to {N_{{\rm{AD}}}} = 11.25 - {B_{\rm{h}}}
$$

Dit geeft:

```{figure} lesoefeningen_2_data/FBD_AC_sol.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
```

Daarna wordt knoopevenwicht van $\rm{D}$ beschouwd:

```{figure} lesoefeningen_2_data/FBD_D.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
```

$$\sum {{F_{\rm{v}}} = 0}  \to {N_{{\rm{DE}}}} =  6.25{\rm{ kN}}$$

Dit geeft:

```{figure} lesoefeningen_2_data/FBD_D_sol.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
```

En ten slotte knoop $\rm{C}$:

```{figure} lesoefeningen_2_data/FBD_C.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
```

$$\sum {{F_{\rm{v}}} = 0}  \to {N_{{\rm{AC}}}} =  - 18.75{\rm{ kN}}$$

Dit geeft:

```{figure} lesoefeningen_2_data/FBD_C_sol.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
```

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
M[0]
M[-25]
M[-1.6]
M[18]
M[0]
MAPE[-25/3;0.1;3]
M[0]
M[-12]
M[0]
MAPE[25/3;0.1;3]
M[-1.6]
M[6]
M[0]
MAPE[-25/3;0.1;3]
^^^
? Bepaal de verlenging/verkorting in alle staven als functie van $B_{\rm{h}}$, met $\Delta L$ in $\rm{mm}$ en $B_{\rm{h}}$ in $\rm{kN}$.

- $\Delta L_{\rm{AC}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{h}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$
- $\Delta L_{\rm{AD}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{h}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$
- $\Delta L_{\rm{CD}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{h}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$
- $\Delta L_{\rm{CE}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{h}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$
- $\Delta L_{\rm{DE}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{h}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$
- $\Delta L_{\rm{DB}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{h}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$
- $\Delta L_{\rm{BE}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{h}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$


---

::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

De verlenging / verkorting kan worden berekend met $\Delta L = \cfrac{{NL}}{{EA}}$
::::

% solution_end

Om de verplaatsingen te vinden van de knopen kijken we afzonderlijk naar de invloed van de horizontale kracht $B_{\rm{h}}$ en van de belasting van $20 \ \rm{kN}$. Hiermee worden de Williot-diagrammetjes iets simpeler

We beginnen met de de belasting van $20 \ \rm{kN}$. Daarvoor reken we dus enkel met de volgende verkortingen/verlengingen:

$$\begin{array}{c}
{\Delta {L_{{\rm{AC}}}} =  - 0.025 \ {\rm{ m}}}\\
{\Delta {L_{{\rm{CE}}}} =  - 0.012\ {\rm{ m}}}\\
{\Delta {L_{{\rm{BE}}}} = \cfrac{1}{{120}} \approx  - 0.00833\ {\rm{ m}}}\\
{\Delta {L_{{\rm{CD}}}} = \cfrac{1}{{120}} \approx  - 0.00833\ {\rm{ m}}}\\
{\Delta {L_{{\rm{DE}}}} = \cfrac{1}{{120}} \approx 0.00833 \ {\rm{ m}}}\\
{\Delta {L_{{\rm{AD}}}} = 0.018 \ {\rm{ m}}}\\
{\Delta {L_{{\rm{DB}}}} = 0.006 \ {\rm{ m}}}
\end{array}$$

De verlengingen/verkortingen ten gevolge van de $20 \ \rm{kN}$ geven:

| Scharnier | Verplaatsing in horizontale richting → (mm)| Verplaatsing in verticale richting ↓ (mm)|
| :-:|:-:|:-:|
|$\rm{A}$|$0$|$0$|
|$\rm{B}$|$24$|$-108$|
|$\rm{C}$|$-15$|$20$|
|$\rm{D}$|$18$|$-\cfrac{91}{6} \approx -15.167$|
|$\rm{E}$|$-27$|$-\cfrac{178}{3} \approx -59.33$|

Dit geeft de volgende vervormde constructie.

```{figure} lesoefeningen_2_data/displaced_20.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
```

$\rm{B}$ zou niet verticaal moeten verplaatsen, dus de constructie moet teruggedraaid worden met $\theta  \approx \cfrac{{108}}{{12000}} = 9 \cdot {10^{ - 3}}{\rm{ rad}}$ ⟳, leading to:

| Scharnier | Verplaatsing in horizontale richting → (mm)| Verplaatsing in verticale richting ↓ (mm)|
| :-:|:-:|:-:|
|$\rm{A}$|$0$|$0$|
|$\rm{B}$|$0$|$108$|
|$\rm{C}$|$36$|$27$|
|$\rm{D}$|$0$|$54$|
|$\rm{E}$|$36$|$81$|

Dit geeft in totaal:

| Scharnier | Verplaatsing in horizontale richting → (mm)| Verplaatsing in verticale richting ↓ (mm)|
| :-:|:-:|:-:|
|$\rm{A}$|$0$|$0$|
|$\rm{B}$|$24$|$0$|
|$\rm{C}$|$21$|$47$|
|$\rm{D}$|$18$|$\cfrac{233}{6} \approx 38.833$|
|$\rm{E}$|$9$|$\cfrac{65}{3} \approx 21.67$|

Dit geeft de volgende vervormde constructie.

```{figure} lesoefeningen_2_data/displaced_20_cor.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
```

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

Bepaal nu de verplaatsingen ten gevolge van $B_{\rm{h}}$. Daarvoor reken we dus enkel met de volgende verkortingen/verlengingen:

$$\begin{array}{c}
{\Delta {L_{{\rm{AC}}}} =  \Delta {L_{{\rm{CE}}}} = \Delta {L_{\rm{BE}}} = \Delta {L_{{\rm{CD}}}} = \Delta {L_{{\rm{DE}}}} = 0}\\
{\Delta {L_{{\rm{AD}}}} = - 1.6 \cdot {B_{\rm{h}}} \ {\rm{mm}}}\\
{\Delta {L_{{\rm{DB}}}} = - 1.6 \cdot {B_{\rm{h}}} \ {\rm{mm}}}
\end{array}$$

---
M[0]
M[0]
M[2.4]
M[-3.2]
M[-0.6]
M[-0.8]
M[0]
M[-1.6]
M[0.6]
M[0.8]
^^^
? Bepaal op basis van deze verlengingen en verkortingen alle verplaatsingen met een apart williot-diagram. Neem daarvoor een zelf gekozen lengte aan voor $B_{\rm{h}}$ (bijvoorbeeld $4$ hokjes komt overeen met $1.6{B_{\rm{h}}}$). Houd daarnaast eerst $\rm{AD}$ in de horizontale oriëntatie zodat je die daarna kan terugdraaien.

- $w_{\rm{A,v}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{h}} $
- $w_{\rm{A,h}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{h}} $
- $w_{\rm{B,v}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{h}} $
- $w_{\rm{B,h}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{h}} $
- $w_{\rm{C,v}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{h}} $
- $w_{\rm{C,h}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{h}} $
- $w_{\rm{D,v}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{h}} $
- $w_{\rm{D,h}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{h}} $
- $w_{\rm{E,v}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{h}} $
- $w_{\rm{E,h}} \left( B_{\rm{h}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{h}} $

---

::::

::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Teken de vervormde statisch bepaalde constructie (met $\rm{AD}$ nog niet teruggeroteerd) ten gevolge van enkel $B_{\rm{h}}$ op schaal.
---
=
```{figure} lesoefeningen_2_data/displaced_Bh.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
```

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
M[0.0002]
^^^
? Draai de vastgehouden $\rm{AD}$ nu zo terug dat $\rm{B}$ niet meer verticaal verplaatst.
De constructie moet $\varphi = $ {gap} $ \left( \rm{in} \, \cfrac{\rm{rad}}{\rm{kN}} \right) \cdot B_{\rm{h}} $ teruggedraaid worden

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
M[24]
M[-3.2]
M[7.5]
^^^
? Wat is nu de ingevulde vormveranderingsvoorwaarde en wat is de oplossing voor $B_{\rm{h}} $? Ga uit van $B_{\rm{h}}$ in $\rm{kN}$ en $w_{\rm{B,h}}$ in $\rm{mm}$ positief naar rechts

$w_{\rm{B,h}} = 0$

{gap} $ \left( \rm{in} \, \rm{mm} \right) + $ {gap} $ \left( \rm{in} \, \cfrac{\rm{mm}}{\rm{kN}} \right) \cdot B_{\rm{h}} = 0 $

$ B_{\rm{h}} = $ {gap} $\rm{kN}$
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
M[-18.75]
M[3.75]
M[-6.25]
M[-7.5]
M[6.25]
M[-3.75]
M[-6.25]
^^^
? Gebruik je resultaat om de normaalkrachten in alle staven te vinden voor de statisch **onbepaalde** constructie.
- $N_{\rm{AC}} = $ {gap} $\rm{kN}$
- $N_{\rm{AD}} = $ {gap} $\rm{kN}$
- $N_{\rm{CD}} = $ {gap} $\rm{kN}$
- $N_{\rm{CE}} = $ {gap} $\rm{kN}$
- $N_{\rm{DE}} = $ {gap} $\rm{kN}$
- $N_{\rm{DB}} = $ {gap} $\rm{kN}$
- $N_{\rm{BE}} = $ {gap} $\rm{kN}$

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

```{figure} lesoefeningen_2_data/displaced_3.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
```

---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

De verplaatsingen ten gevolge van enkel $B_{\rm{h}}$ na rotatie zijn:

| Scharnier | Verplaatsing in horizontale richting → (mm)| Verplaatsing in verticale richting ↓ (mm)|
| :-:|:-:|:-:|
|$\rm{A}$|$0$|$0$|
|$\rm{B}$|$-3.2B_\rm{h}$|$0$|
|$\rm{C}$|$-1.6B_\rm{h}$|$-1.2B_\rm{h}$|
|$\rm{D}$|$-1.6{B_{\rm{h}}}$|$-1.2B_\rm{h}$|
|$\rm{E}$|$-1.6B_\rm{h}$|$-1.2B_\rm{h}$|

Invullen van $B_{\rm{h}} = 7.5 \ \rm{kN}$ en optellen bij de verplaatsingen ten gevolge van de $20 \ \rm{kN}$ belasting geeft:

```{figure} lesoefeningen_2_data/displaced_3.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2
```

% solution_end
