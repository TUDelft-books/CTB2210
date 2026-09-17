````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze instructie is aangepast van de [de tentamenopdracht van 8 november van het vak CT1000S Structural Mechanics 2024/2025](https://oit.tudelft.nl/CT1000/2024/week_10/session/intro.html) van {cite:ts}`CT1000_2024`

```
````

# Begeleide oefening 1

Gegeven is de volgende constructie:

```{figure-start} ./lesoefeningen_data/structure2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpuntzetting
:figclass: sticky-margin
```
$EA = 15 \ \rm{MN}$

```{figure-end}
```

::::::{exercise}
:label: steun_1_1
:nonumber: true

Gegeven is de volgende uitwerking:

$N_{\rm{BD}} = \cfrac{90}{6000} \cdot 15000 = 225 \ \rm{kN}$

Evenwicht van knoop D levert:
- $ N_{\rm{AD}} = -281.25 \ \rm{kN}$
- $ N_{\rm{CD}} = -168.75 \ \rm{kN}$

Hieruit volgt:
- $\Delta L_{\rm{AD}} = \cfrac{-281.25 \cdot 7.5}{15000} = -0.109125 \ \rm{m}$
- $\Delta L_{\rm{CD}} = \cfrac{-168.75 \cdot 6}{15000} = - 0.0675 \ \rm{m}$

Met als resultaat:
- Horizontale verplaatsing van $\rm{D}$ van $67.5 \ \rm{mm}$ naar rechts
- Verticale verplaatsing van $\rm{D}$ van $109.125 \cdot \cfrac{4}{5} = 87.3 \ \rm{mm} $ naar beneden

:::::{question}
:nocaption:
:showanswer:
:variant: multiple-select
:columns: 1

Wat is er verkeerd aan de bovenstaande uitwerking?
---
[x] De normaalkracht in $\rm{BD}$ is niet juist berekend.
[ ] De normaalkrachten in $\rm{AD}$ en $\rm{CD}$ zijn niet juist berekend
> De methode van evenwicht is hier juist toegepast, alhoewel de antwoorden fout zijn omdat $N_{\rm{BD}}$ niet goed is
[ ] De verlengingen van de staven $\rm{AD}$ en $\rm{CD}$ zijn niet juist berekend
> De constitutieve en kinematische vergelijkingen zijn hier juist toegepast, alhoewel de antwoorden fout zijn omdat de normaalkrachten al fout zijn.
[x] De verplaatsing van knoop $\rm{D}$ is niet juist berekend
^^^
! De verlenging van $\rm{BD}$ is niet enkel afhankelijk van de verplaatsing van knoop $\rm{B}$. Heb je niet williot nodig in dit geval?
---

:::::

::::::

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
De constructie is {gap}ste/de graads inwendig statisch onbepaald.

---
::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

```{figure} ./lesoefeningen_data/Onbekenden_vergelijkingen.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpuntzetting
```

De constructie is 1ste graads inwendig statisch onbepaald. 

::::

% solution_end

Gekozen is het volgende statisch bepaalde systeem met vormveranderingsvoorwaarde:

```{figure-start} ./lesoefeningen_data/statically_determinate2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpuntzetting
:figclass: sticky-margin
```
$EA = 15 \ \rm{MN}$

```{figure-end}
```

Er is gekozen voor dit systeem zodat we de steunpuntszetting in de vormveranderingsvoorwaarde mee kunnen nemen en niet mee hoeven te nemen in bepalen van krachtsverdeling.

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[1]
M[0]
M[-1.25]
M[0]
M[-0.75]
M[0]
M[0.0004]
M[0]
M[-0.000625]
M[0]
M[-0.0003]
M[0]
M[0.0003]
M[0]
M[0.001]
M[0]
M[0.0014]
M[0]
^^^
? Bepaal de krachtsverdeling en vervormingen als functie van $B_{\rm{v}}$ met $B_{\rm{v}} in $\rm{kN}$.

- $N_{\rm{BD}} \left( \rm{B}_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$ 
- $N_{\rm{AD}} \left( \rm{B}_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $N_{\rm{CD}} \left( \rm{B}_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $\Delta L_{\rm{BD}} \left( \rm{B}_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$
- $\Delta L_{\rm{AD}} \left( \rm{B}_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$
- $\Delta L_{\rm{CD}} \left( \rm{B}_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$
- $w_{D,\rm{h}} \left( \rm{B}_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (→)
- $w_{D,\rm{v}} \left( \rm{B}_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (↓)
- $w_{B,\rm{v}} \left( \rm{B}_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (↓)

---

::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

De normaalkrachten in de staven AD en CD kunnen met behulp van het knoopevenwicht van $\rm{D}$ worden uitgedrukt in $B_{\rm{v}}$. 

$$ N_{\rm{BD}} = B_{\rm{v}} $$
$$ \sum F_{\rm{v}} = 0 \rightarrow N_{\rm{AD}} = - \cfrac{5}{4} \cdot B_{\rm{v}} $$
$$ \sum F_{\rm{h}} = 0 \rightarrow N_{\rm{CD}} = - \cfrac{3}{4} \cdot B_{\rm{v}} $$

Nu de normaalkrachten in de staven bekend zijn kan de verlenging/verkorting per staaf worden bepaald. De resultaten zijn weergegeven in de onderstaande tabel. 

| Staaf | $N\left(B_{\rm{v}}\right)$ (kN)| $\Delta L \left(B_{\rm{v}}\right)\rm{(mm)}$ |
| :-:|:-:|:-:|
|$\rm{AD}$|$-\cfrac{5}{4} \cdot B_{\rm{v}}$|$-\cfrac{5}{8} \cdot B_{\rm{v}}$|
|$\rm{BD}$|$B_{\rm{v}}$|$\cfrac{2}{5} \cdot B_{\rm{v}}$|
|$\rm{CD}$|$- \cfrac{3}{4} \cdot B_{\rm{v}}$|$-\cfrac{3}{10} \cdot B_{\rm{v}}$|

Met behulp van de berekende verlenging/verkorting kan het williot diagram worden getekend, zie de figuur hieronder. 

```{figure} lesoefeningen_data/williot.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpuntzetting
```

Uit het williot diagram kan worden afgelezen:

- $ w_{D,\rm{h}} = 0.0003 \cdot B_{\rm{v}} \ \rm{m} \ \left(\rightarrow\right)$
- $ w_{D,\rm{v}} \approx 0.001 \cdot B_{\rm{v}} \ \rm{m} \  \left(\downarrow\right)$
- $ w_{B,\rm{h}} = 0 $$
- $ w_{B,\rm{v}} \approx 0.0014 \cdot B_{\rm{v}} \ \rm{m} \ \left(\downarrow\right)$

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
M[64]
^^^
? Los de vormveranderingsvoorwaarden op om de statisch onbepaalde krachten te vinden.

$B_{\rm{v}}= $ {gap} $\rm{kN}$
---

::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

De vormveranderingsvoorwaarde is: $w_{B,\rm{v}} = 1.4 \cdot B_{\rm{v}} = 90 \rm{mm}$.

Hieruit volgt: $B_{\rm{v}} = 64 \rm{kN}$

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
M[64]
M[-80]
M[48]
M[19]
M[64]
^^^
? Los nu ook de overige krachtenverdeling op.

- $N_{\rm{BD}}= $ {gap} $\rm{kN}$
- $N_{\rm{AD}}= $ {gap} $\rm{kN}$
- $N_{\rm{CD}}= $ {gap} $\rm{kN}$
- $w_{D,\rm{h}} = $ {gap} $\rm{mm}$ (→)
- $w_{D,\rm{v}} = $ {gap} $\rm{mm}$ (↓)

---

::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

De krachten en verplaatsingen kunnen worden opgelost uit de eerder opgestelde vergelijkingen door daar de berekende waarde voor $B_{\rm{v}}$ in in te vullen.

- $ N_{\rm{BD}}= 64 \rm{kN} $
- $ N_{\rm{AD}}= -80 \rm{kN} $
- $ N_{\rm{CD}}= -48 \rm{kN} $
- $ w_{D,\rm{h}} = 19 \rm{mm} \ \left(\rightarrow\right)$
- $ w_{D,\rm{v}} = 64 \rm{mm} \ \left(\downarrow\right)$

::::

% solution_end

:::::{question} Opgave
:type: no-input
:nocaption:
:class: exercise
:admonition:
:showanswer:

Teken de vervormde constructie

---
=

```{figure} ./lesoefeningen_data/vervormd.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpuntzetting
```

---

:::::
