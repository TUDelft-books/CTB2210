# Begeleide oefening

Gegeven is de volgende constructie:

```{figure-start} lesoefeningen_data/structure.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
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
M[0]
^^^
?
De constructie is {gap}ste/de graads uitwendig statisch onbepaald
---

::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

```{figure} lesoefeningen_data/graad.svg
---
align: center
number:
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
---

```

Er zijn 10 onbekende krachten en 9 evenwichtsvergelijkingen. Dus de constructie is 1ste graads statisch onbepaald

::::

% solution_end

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

::::{question} Opgave
:type: short-answer
:variant: blocks
:admonition:
:class: exercise
:nocaption:
:showanswer:

Neem als statisch onbepaalde kracht de verticale oplegreactie bij $\rm{B}$ (positief omhoog). Wat is de vormveranderingsvoorwaarde? Gebruik de variabele $w_{\rm{...}}$ voor een verticale verplaatsing.
---
M[w_B = 0]
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

- $ N_{\rm{AD}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $ N_{\rm{CE}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $ w_{\rm{E}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right)\cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$ (positief omhoog)
- $ w_{\rm{D}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right)\cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$ (positief omhoog)
- $ w_{\rm{B}} \left( B_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right)\cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$ (positief omhoog)
---

::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

```{figure} lesoefeningen_data/Vrijlichaamsschema1.svg
---
align: center
number:
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_vakwerk
---

```

$$
\begin{align}
\sum  \left. T \right|  _ {\rm{E}} &= 0 \\
5 \cdot N_{\rm{AD}} - 2 \cdot B_{\rm{v}} - 3 \cdot26& =0 \\
N_{\rm{AD}} &= 0.4 \cdot B_{\rm{v}} + 15.6
\end{align}
$$ 

$$
\begin{align}
\sum F_ {\rm{v}} &=0 \\
- N_{\rm{AD}} + B_{\rm{v}} + N_{\rm{CE}} -26&= 0 \\
N_{\rm{CE}} &= - 0.6 \cdot B_{\rm{v}} + 41.6
\end{align}
$$


$$ w_{\rm{E}} = - \Delta L_{\rm{CE}} = \cfrac{-N_{\rm{CE}} \cdot L_{\rm{CE}}}{EA} = 0.0006 \cdot B_{\rm{v}} - 0.0416  $$

$$ w_{\rm{D}} = \Delta L_{\rm{AD}} = \cfrac{-N_{\rm{AD}} \cdot L_{\rm{AD}}}{EA} = 0.0004 \cdot B_{\rm{v}} - 0.0156 $$ 

$$ w_{\rm{B}} = w_{\rm{D}} + \cfrac{3}{5} \cdot \left( w_{\rm{E}} - w_{\rm{D}} \right) = \cfrac{3}{5} \cdot w_{\rm{E}} + \cfrac{2}{5} \cdot w_{\rm{D}} = 0.00052 \cdot B_{\rm{v}} - 0.01872 $$

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

:::::{exercise}
:label: km_vak_1_6
:nonumber: true

Neem als statisch onbepaalde kracht het moment $M_{\rm{B}}$ (positief zorgt voor trek aan de onderkant).

```{h5p} https://tudelft.h5p.com/content/1292634286050413117/embed
```

:::::

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
? Neem als statisch onbepaalde kracht het moment $M_{\rm{B}}$ (positief zorgt voor trek aan de onderkant). Wat is de vormveranderingsvoorwaarde?

{gap}$(${gap}$) = ${gap}$(${gap}$)$
---

::::


:::::{exercise}
:label: km_vak_1_7
:nonumber: true

Bepaal achtereenvolgens de normaalkrachten en verplaatsingen als functie van $M_{\rm{B}}$.

```{h5p} https://tudelft.h5p.com/content/1292634293341890027/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

```{figure} lesoefeningen_data/Vrijlichaamsschema2.svg
---
align: center
---
Constructie vrijgemaakt van pendelstaven met $M_{\rm{B}}$ als statisch onbepaalde. 
```

De gebruikte vergelijkingen zijn:

$$ \sum  \left. M \right| _ {\rm{B}} ^{\rm{BD}} = 3 \cdot N_{\rm{AD}} + M_{\rm{B}} =0 $$ 
$$ \sum  \left. M \right| _ {\rm{B}} ^{\rm{BG}} = - M_{\rm{B}} + 2 \cdot N_{\rm{CE}} - 5 \cdot26=0 $$ 
$$ \varphi _ {\rm{B}} ^{\rm{DB}} = \cfrac{w_{\rm{D}}}{3} $$
$$ \varphi _ {\rm{B}} ^{\rm{BE}} = \cfrac{w_{\rm{E}}}{2} $$

Hieruit volgt:

$$ N_{\rm{AD}} = -0.33 \cdot M_{\rm{B}}$$
$$ N_{\rm{CE}} = 0.5 \cdot M_{\rm{B}} + 65 $$
$$ \varphi _ {\rm{B}} ^{\rm{DB}} = -0.00011 \cdot M_{\rm{B}} $$
$$ \varphi _ {\rm{B}} ^{\rm{BE}} = 0.00025 \cdot M_{\rm{B}} + 0.0325 $$

::::

% solution_end

:::::{exercise}
:label: km_vak_1_8
:nonumber: true

Los met de vormveranderingsvoorwaarde de statisch onbepaalde kracht $M_{\rm{B}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292634306404351337/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

Oplossen van de vergelijkingen geeft:

$$ N_{\rm{AD}} = 30 \rm{kN} $$
$$ N_{\rm{CE}} = 20 \rm{kN} $$
$$ \varphi_{\rm{B}} = 0.01 \rm{rad} $$
$$ M_{\rm{B}} = -90 \rm{kNm} $$

::::

% solution_end

## Statisch onbepaalde normaalkracht $N_{\rm{AD}}$

:::::{exercise}
:label: km_vak_1_9
:nonumber: true

Neem als statisch onbepaalde kracht de normaalkracht $N_{\rm{AD}}$ door de pendelstaaf in het scharnier los te maken van de balk.

```{h5p} https://tudelft.h5p.com/content/1292634312901581657/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

De vormveranderingsvoorwaarde is: 

$$ w _ {\rm{{D}}}^{\rm{AD}} = w _ {\rm{{D}}}^{\rm{BD}} $$

::::

% solution_end

:::::{exercise}
:label: km_vak_1_10
:nonumber: true

Bepaal achtereenvolgens de normaalkrachten en verplaatsingen als functie van $N_{\rm{AD}}$.

```{h5p} https://tudelft.h5p.com/content/1292634315769955647/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

```{figure} lesoefeningen_data/Vrijlichaamsschema3.svg
---
align: center
---
Constructie met $N_{\rm{AD}}$ als statisch onbepaalde en vrijgemaakt van pendelstaaf CE. 
```

De gebruikte vergelijkingen zijn:

$$ \sum \left.  M \right| _ {\rm{B}} = 3 \cdot N_{\rm{AD}} + 2 \cdot N_{\rm{CE}} - 5 \cdot 26 = 0 $$ 
$$ w_{\rm{E}} = - \Delta l_{\rm{CE}} = \cfrac{-N_{\rm{CE}} \cdot l_{\rm{CE}}}{EA} $$
$$ w_{\rm{D}} ^ {\rm{AD}} = \Delta l_{\rm{AD}} = \cfrac{N_{\rm{AD}} \cdot l_{\rm{AD}}}{EA} $$ 
$$ w_{\rm{D}} ^ {\rm{BD}} = \varphi_{\rm{B}} \cdot 3 = - \cfrac{3}{2} w_{\rm{E}} $$

Hieruit volgt:

$$ N_{\rm{CE}} = - 1.5 \cdot N_{\rm{AD}} + 65 $$
$$ w_{\rm{E}} = 0.0015 \cdot N_{\rm{AD}} -0.065 $$
$$ w_{\rm{D}} ^{\rm{AD}} = 0.001 \cdot N_{\rm{AD}} $$
$$ w_{\rm{D}} ^{\rm{BD}} = -0.00225 \cdot N_{\rm{AD}} + 0.0975 $$

::::

% solution_end

:::::{exercise}
:label: km_vak_1_11
:nonumber: true

Los met de vormveranderingsvoorwaarde de statisch onbepaalde kracht $N_{\rm{AD}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292634317462305007/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

Oplossen van de vergelijkingen geeft:

$$ N_{\rm{AD}} = 30 \rm{kN} $$
$$ N_{\rm{CE}} = 20 \rm{kN} $$
$$ w_{\rm{E}} = -2 \rm{cm} $$
$$ w_{\rm{D}} = 3 \rm{cm} $$

::::

% solution_end
