% source files on https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/stijfheid_steunpunt

````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze instructie is aangepast van de [les van 23 oktober van het vak CT1000S Structural Mechanics 2024/2025](https://oit.tudelft.nl/CT1000/2024/week_8/session_2/intro.html) van {cite:ts}`CT1000_2024`

```
````

# Begeleide oefening 2

Gegeven is de volgende constructie:

```{figure-start} ./lesoefeningen_data/structure.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/stijfheid_steunpunt
:figclass: sticky-margin
```
$EI = \cfrac{250}{3} \ \rm{MNm}^2$

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
M[2]
^^^
?
De constructie is {gap}ste/de graads inwendig statisch onbepaald.

---
::::

## Extremen

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[0]
M[0]
M[0]
M[0]
M[0]
M[0]
M[25]
M[0]
^^^
? Voor het geval dat $nEI \to 0$, bepaal de krachtsverdeling en verplaatsingen:

- $A_{\rm{v}} \left( nEI \to 0 \right)= $ {gap} $\rm{kN}$ (↑)
- $B_{\rm{v}} \left( nEI \to 0 \right)= $ {gap} $\rm{kN}$ (↑)
- $C_{\rm{v}} \left( nEI \to 0 \right)= $ {gap} $\rm{kN}$ (↑)
- $D_{\rm{v}} \left( nEI \to 0 \right)= $ {gap} $\rm{kN}$ (↑)
- $M_{\rm{B}} \left( nEI \to 0 \right)= $ {gap} $\rm{kNm}$ (◡)
- $M_{\rm{D}} \left( nEI \to 0 \right)= $ {gap} $\rm{kNm}$ (◡)
- $w_{\rm{halverwege \ AB}} \left( nEI \to 0 \right)= $ {gap} $\rm{mm}$ (↓)
- $w_{\rm{halverwege \ CD}} \left( nEI \to 0 \right)= $ {gap} $\rm{mm}$ (↓)

---

::::

::::{admonition} Oplossing
:class: solution, dropdown

Als deel $\rm{BC}$ geen buigstijfheid meer heeft ontstaan er feitelijk twee losse liggertjes waarvan de linker 25 $\rm{mm}$ zakt. Dit levert de onderstaande krachten en verplaatsingen:

- $A_{\rm{v}} \left( nEI \to 0 \right) = 0 \rm{kN}$
- $B_{\rm{v}} \left( nEI \to 0 \right) = 0 \rm{kN}$
- $C_{\rm{v}} \left( nEI \to 0 \right) = 0 \rm{kN}$
- $D_{\rm{v}} \left( nEI \to 0 \right) = 0 \rm{kN}$
- $M_{\rm{B}} \left( nEI \to 0 \right) = 0 \rm{kNm}$
- $M_{\rm{D}} \left( nEI \to 0 \right) = 0 \rm{kNm}$
- $w_{\rm{halverwege} \ \rm{AB}} \left( nEI \to 0 \right) = 25 \rm{mm}$
- $w_{\rm{halverwege} \ \rm{CD}} \left( nEI \to 0 \right) = 0 \rm{mm}$

::::

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[6.25]
M[-18.75]
M[18.75]
M[-6.25]
M[62.5]
M[-62.5]
M[29.6875]
M[-4.6875]
^^^
? Voor het geval dat $nEI \to \infty$, bepaal de krachtsverdeling en verplaatsingen:

- $A_{\rm{v}} \left( nEI \to \infty \right)= $ {gap} $\rm{kN}$ (↑)
- $B_{\rm{v}} \left( nEI \to \infty \right)= $ {gap} $\rm{kN}$ (↑)
- $C_{\rm{v}} \left( nEI \to \infty \right)= $ {gap} $\rm{kN}$ (↑)
- $D_{\rm{v}} \left( nEI \to \infty \right)= $ {gap} $\rm{kN}$ (↑)
- $M_{\rm{B}} \left( nEI \to \infty \right)= $ {gap} $\rm{kNm}$ (◡)
- $M_{\rm{D}} \left( nEI \to \infty \right)= $ {gap} $\rm{kNm}$ (◡)
- $w_{\rm{halverwege \ AB}} \left( nEI \to \infty \right)= $ {gap} $\rm{mm}$ (↓)
- $w_{\rm{halverwege \ CD}} \left( nEI \to \infty \right)= $ {gap} $\rm{mm}$ (↓)

---

::::

::::{admonition} Oplossing
:class: solution, dropdown

Er wordt gekozen voor het onderstaande statisch bepaalde systeem, waarbij scharnieren en onbekende momentenparen zijn toegevoegd in $\rm{B}$ en $\rm{C}$. 

```{figure-start} ./lesoefeningen_data/SB_systeem1.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/stijfheid_steunpunt
```

- $EI_{\rm{AB}} = EI_{\rm{CD}} = \cfrac{250}{3} \ \rm{MNm^2}$
- $EI_{\rm{BC}} = \infty$

```{figure-end}
```

De bijbehorende vormveranderingsvoorwaarden zijn:

- $\varphi_{\rm{B}}^{\rm{AB}}=\varphi_{\rm{B}}^{\rm{BC}}$
- $\varphi_{\rm{C}}^{\rm{BC}}=\varphi_{\rm{C}}^{\rm{CD}}$

Omdat deel $\rm{BC}$ oneindig stijf is geldt: $\varphi_{\rm{B}}^{\rm{BC}}=\varphi_{\rm{C}}^{\rm{BC}}=\cfrac{25}{10000}=0.0025\rm{rad}$

Met behulp van het vergeet-mij-nietje voor een ligger op twee steunpunten belast door een koppel wordt het volgende gevonden: $\varphi_{\rm{B}}^{\rm{AB}}=\cfrac{M_{\rm{B}}\cdot10}{3\cdot\cfrac{250}{3}\cdot1000} \rightarrow M_{\rm{B}}=62.5 \rm{kNm}$

Uit momentenevenwicht van deel $\rm{AB}$ volgt: $\sum \left. T \right| _ {\rm{B}} ^{\rm{AB}} = - A_{\rm{v}} \cdot 10 + 62.5=0 \rightarrow A_{\rm{v}} =6.25 \rm{kN}$

Uit symmetrie volgt: $M_{\rm{C}}=-M_{\rm{B}}=-62.5 \rm{kNm}$ en $D_{\rm{v}}=-A_{\rm{v}}=-6.25 \rm{kN}$

Met momentenevenwicht van de hele constructie kan nu worden bepaald dat $B_{\rm{v}}=-18.75 \rm{kN}$ en $C_{\rm{v}}=18.75 \rm{kN}$.  

De zakkingen in het midden van de delen $\rm{AB}$ en $\rm{CD}$ kunnen worden bepaald uit de superpositie van de vervorming door buiging en de zakking van de opleggingen. 

- $w_{\rm{halverwege} \ \rm{AB}} = 25 + \cfrac{62.5\cdot 10^2}{16\cdot\cfrac{250}{3}}=29.6875 \ \rm{mm}$
- $w_{\rm{halverwege} \ \rm{CD}} = - \cfrac{62.5\cdot 10^2}{16\cdot\cfrac{250}{3}}=-4.6875 \ \rm{mm}$

::::

## Vermenigvuldigingsfactor

Voor het geval van variabele $n$ is het volgende statisch bepaalde systeem:

```{figure-start} ./lesoefeningen_data/SB.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/stijfheid_steunpunt
:figclass: sticky-margin
```

$EI = \cfrac{250}{3} \ \rm{MNm}^2$

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
M[25]
M[0]
^^^
? Wat zijn de vormveranderingsvoorwaarden?

- Bij $\rm{A}: w_A = $ {gap} $\rm{mm}$ (↓)
- Bij $\rm{D}: w_D = $ {gap} $\rm{mm}$ (↓)

---

::::

::::::{admonition} Opgave
:class: exercise

Voor alleen de zakking:

```{figure} ./lesoefeningen_data/belasting_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/stijfheid_steunpunt
:number:
```

:::::{question}
:type: no-input
:nocaption:
:showanswer:

Schets de mogelijke vervormingen:

---
=

```{figure} ./lesoefeningen_data/vervorming_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/stijfheid_steunpunt
:number:
```

---

:::::

::::{question} Opgave
:type: short-answer
:variant: gaps
:nocaption:
:showanswer:

---
M[0]
M[0]
M[0.0025]
M[0.0025]
M[37.5]
M[-12.5]
^^^
? Bepaal de krachtsverdeling en verplaatsingen.

- $M_{\rm{B}} = $ {gap} $\rm{kNm}$ (◡)
- $M_{\rm{D}} = $ {gap} $\rm{kNm}$ (◡)
- $\varphi_{\rm{B}} = $ {gap} $\rm{rad}$ (↺)
- $\varphi_{\rm{C}} = $ {gap} $\rm{rad}$ (↺)
- $w_{\rm{halverwege \ AB}} = $ {gap} $\rm{mm}$ (↓)
- $w_{\rm{halverwege \ CD}} = $ {gap} $\rm{mm}$ (↓)

---

::::

::::::

::::{admonition} Oplossing
:class: solution, dropdown

Als $A_{\rm{v}}$ en $D_{\rm{v}}$ gelijk zijn aan 0 dan kan de constructie vrij vervormen en onstaat er geen buiging.

::::

::::::{admonition} Opgave
:class: exercise

Voor alleen de statisch onbepaalde krachten (dus geen zakking):

```{figure} ./lesoefeningen_data/belasting_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/stijfheid_steunpunt
:number:
```

:::::{question}
:type: no-input
:nocaption:
:showanswer:

Schets de mogelijke vervormingen:

---
=

```{figure} ./lesoefeningen_data/vervorming_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/stijfheid_steunpunt
:number:
```

---

:::::

::::{question} Opgave
:type: short-answer
:variant: gaps
:nocaption:
:showanswer:

---
M[10]
M[0]
M[0]
M[10]
M[0]
M[0]
M[-0.0004]
M[-0.0002]
M[0]
M[0.0002]
M[0.0004]
M[0]
M[0.004]
M[0.002]
M[0]
M[-0.002]
M[-0.004]
M[0]
^^^
? Bepaal de krachtsverdeling en verplaatsingen als functie van $A_{\rm{v}}$ en $D_{\rm{v}}$ in $\rm{kN}$.

- $M_{\rm{B}} \left(A_{\rm{v}}, D_{\rm{v}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kNm}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kNm}}{\rm{kN}}\right) \cdot D_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kNm}\right)$ (◡)
- $M_{\rm{D}} \left(A_{\rm{v}}, D_{\rm{v}}\right)= $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kNm}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kNm}}{\rm{kN}}\right) \cdot D_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kNm}\right)$ (◡)
- $\varphi_{\rm{B}} \left(A_{\rm{v}}, D_{\rm{v}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot D_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$ (↺)
- $\varphi_{\rm{C}} \left(A_{\rm{v}}, D_{\rm{v}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot D_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$ (↺)
- $w_{\rm{halverwege \ AB}} \left(A_{\rm{v}}, D_{\rm{v}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $ \left(\rm{m} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot D_{\rm{v}} + $ {gap} $\left(\rm{m} \, \rm{rad}\right)$ (↓)
- $w_{\rm{halverwege \ CD}} \left(A_{\rm{v}}, D_{\rm{v}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $ \left(\rm{m} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot D_{\rm{v}} + $ {gap} $\left(\rm{m} \, \rm{rad}\right)$ (↓)

---

::::

::::::

::::{admonition} Oplossing
:class: solution, dropdown

De momenten $M_{\rm{B}}$ en $M_{\rm{C}}$ kunnen worden bepaald door respectievelijk $A_{\rm{v}}$ en $D_{\rm{v}}$ te verplaatsen naar $\rm{B}$ en $\rm{C}$. 

$$M_{\rm{B}} = 10 \cdot A_{\rm{v}}$$
$$M_{\rm{C}} = 10 \cdot D_{\rm{v}}$$

De hoekverdraaiingen in $\rm{B}$ en $\rm{C}$ kunnen worden bepaald uit een superpositie van de vervorming door buiging en de vrije vervorming zoals in de vorige opgave berekend. Voor de vervorming door buiging wordt het vergeet-mij-nietje voor een ligger op twee steunpunten belast door een koppel gebruikt. 

$$ \varphi_{\rm{B}} \left( A_{\rm{v}}, D_{\rm{v}} \right) = -\cfrac{10 \cdot A_{\rm{v}} \cdot 10}{3 \cdot \cfrac{250}{3} \cdot n\cdot 1000} - \cfrac{10 \cdot D_{\rm{v}} \cdot 10}{6 \cdot \cfrac{250}{3} \cdot n\cdot 1000} + 0.0025 = -0.0004 \cdot \cfrac{A_{\rm{v}}}{n} -0.0002 \cdot \cfrac{D_{\rm{v}}}{n} + 0.0025 $$
$$ \varphi_{\rm{C}} \left( A_{\rm{v}}, D_{\rm{v}} \right) = \cfrac{10 \cdot A_{\rm{v}} \cdot 10}{6 \cdot \cfrac{250}{3} \cdot n\cdot 1000} + \cfrac{10 \cdot D_{\rm{v}} \cdot 10}{3 \cdot \cfrac{250}{3} \cdot n\cdot 1000} + 0.0025 = 0.0002 \cdot \cfrac{A_{\rm{v}}}{n} + 0.0004 \cdot \cfrac{D_{\rm{v}}}{n} + 0.0025 $$

De zakkingen in $\rm{A}$ en $\rm{D}$ kunnen worden bepaald uit de superpositie van vrije vervorming van de constructie, vervorming door buiging van deel $\rm{BC}$ en vervorming door buiging van de delen $\rm{AB}$ en $\rm{CD}$. 

$$ w_{\rm{A}} \left( A_{\rm{v}}, D_{\rm{v}} \right) = 0.05 + 10 \cdot \left( -0.0004 \cdot \cfrac{A_{\rm{v}}}{n} -0.0002 \cdot \cfrac{D_{\rm{v}}}{n} \right) - \cfrac{ A_{\rm{v}} \cdot 10^3}{3 \cdot \cfrac{250}{3} \cdot 1000} =-0.004  \cdot A_{\rm{v}} -0.004 \cdot \cfrac{A_{\rm{v}}}{n} -0.002 \cdot \cfrac{D_{\rm{v}}}{n} + 0.05 $$
$$ w_{\rm{D}} \left( A_{\rm{v}}, D_{\rm{v}} \right) = -0.025 - 10 \cdot \left( 0.0002 \cdot \cfrac{A_{\rm{v}}}{n} + 0.0004 \cdot \cfrac{D_{\rm{v}}}{n} \right) - \cfrac{ D_{\rm{v}} \cdot 10^3}{3 \cdot \cfrac{250}{3} \cdot 1000} =-0.002 \cdot \cfrac{A_{\rm{v}}}{n} + -0.004 \cdot D_{\rm{v}} + -0.004\cdot \cfrac{D_{\rm{v}}}{n} -0.025 $$

::::

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[25]
M[0]
M[4]
M[2]
M[25]
M[0]
M[4]
M[2]
^^^
? Los met de vormveranderingsvoorwaardes de onbekende $A_{\rm{v}}$ en $D_{\rm{v}}$ in $\rm{kN}$ op. Let op, dit is een lastige wiskundige exercitie. Je wordt aangeraden gebruik te maken van een tool zoals SymPy.

- $\rm{Av} = ( $ {gap} $ \cdot n + $ {gap} $ ) / ( $ {gap} $ \cdot n + $ {gap} $ )$
- $\rm{Dv} = ( - $ {gap} $ \cdot n + $ {gap} $ ) / ( $ {gap} $ \cdot n + $ {gap} $ )$

---

::::

::::{admonition} Oplossing
:class: solution, dropdown

Oplossen van de vergelijkingen levert:

- $ A_{\rm{v}}= \cfrac{25 \cdot n}{4 \cdot n + 2} $
- $ D_{\rm{v}}= -\cfrac{25 \cdot n}{4 \cdot n + 2} $

Deze functies kunnen ook geplot worden:

```{figure} lesoefeningen_data/steunpuntszetting.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/stijfheid_steunpunt
:number:
```

::::
