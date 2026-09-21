````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze oefening is aangepast de [tentamenopdracht van 9 december 2025](https://oit.tudelft.nl/CT1000/2025/week_15/session/intro.html) van {cite:ts}`CT1000`

```
````

# Begeleide oefening

```{figure-start} ./lesoefening_data/constructie.svg
:align: center
:figclass: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/exam_SOB
:number:
```

- $EI = 768 \ \rm{MNm^2}$
- $EA = 125 \ \rm{MN}$

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


% https://oit.tudelft.nl/CT1000/2025/week_15/session/intro.html

::::::{admonition} Opgave
:class: exercise

Gegeven is de volgende mogelijke aangepaste constructie:

```{figure} ./lesoefening_data/optie_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
:number:
```

:::::{question}
:nocaption:
:showanswer:
:columns: 1


Is deze constructie statisch bepaald, statisch onbepaald of een mechanisme?
---
[x] Deze constructie is statisch bepaald.
[ ] Deze constructie is statisch onbepaald.
[ ] Deze constructie is een mechanisme.
---

:::::

:::::{question}
:type: no-input
:nocaption:
:showanswer:

Schets de mogelijke vervormingen ten gevolge van het moment $M_{\rm{A}}$::

---
=

```{figure} ./lesoefening_data/optie_1_verplaatsing.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
:number:
```

---

:::::

:::::{question}
:nocaption:
:showanswer:
:columns: 1

Is deze aangepaste constructie een goede keuze voor de krachtenmethode?
---
[ ] Ja
> $\rm{AB}$ zal zowel buigen als star roteren rondom $\rm{A}$, wat de berekening van de verplaatsingen bemoeilijkt.
[x] Het kan, maar er zijn betere opties
[ ] Nee
> Deze constructie is statisch bepaald en daarmee geschikt!
---

:::::

::::::

::::::{admonition} Opgave
:class: exercise

Gegeven is de volgende mogelijke aangepaste constructie:

```{figure} ./lesoefening_data/optie_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
:number:
```

:::::{question}
:nocaption:
:showanswer:
:columns: 1


Is deze constructie statisch bepaald, statisch onbepaald of een mechanisme?
---
[ ] Deze constructie is statisch bepaald.
[ ] Deze constructie is statisch onbepaald.
[x] Deze constructie is een mechanisme.
---

:::::

:::::{question}
:nocaption:
:showanswer:
:columns: 1

Is deze aangepaste constructie een goede keuze voor de krachtenmethode?
---
[ ] Ja
[ ] Het kan, maar er zijn betere opties
[x] Nee
---

:::::

::::::

::::::{admonition} Opgave
:class: exercise

Gegeven is de volgende mogelijke aangepaste constructie:

```{figure} ./lesoefening_data/optie_3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
:number:
```

:::::{question}
:nocaption:
:showanswer:
:columns: 1


Is deze constructie statisch bepaald, statisch onbepaald of een mechanisme?
---
[x] Deze constructie is statisch bepaald.
[ ] Deze constructie is statisch onbepaald.
[ ] Deze constructie is een mechanisme.
---

:::::

:::::{question}
:type: no-input
:nocaption:
:showanswer:

Schets de mogelijke vervormingen ten gevolge van de statisch onbepaalde kracht $B_{\rm{v}}$::

---
=

```{figure} ./lesoefening_data/optie_3_verplaatsingen.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
:number:
```

---

:::::

:::::{question}
:nocaption:
:showanswer:
:columns: 1

Is deze aangepaste constructie een goede keuze voor de krachtenmethode?
---
[x] Ja
[ ] Het kan, maar er zijn betere opties
[ ] Nee
> Deze constructie is statisch bepaald en daarmee geschikt!
---

:::::

::::::

Er wordt gekozen voor het volgende statisch bepaalde systeem inclusief vormveranderingsvoorwaarden:

```{figure-start} ./lesoefening_data/stat_bepaald.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
:figclass: sticky-margin
:number:
```

- $EI = 768 \ \rm{MNm^2}$
- $EA = 125 \ \rm{MN}$

```{figure-end}
```

:::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Schets de mogelijke vervormingen ten gevolgde van de $90 \ \rm{kN}$.
---
=

```{figure} ./lesoefening_data/verplaatsingen_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
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

Schets de mogelijke vervormingen ten gevolgde van de statisch onbepaalde kracht $N_{\rm{C}}$.
---
=

```{figure} ./lesoefening_data/verplaatsingen_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_SOB
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
ME[\cfrac{3}{5};1]
M[90]
M[-1]
ME[\cfrac{-4}{5};1]
M[0]
ME[\cfrac{4}{125};2]
ME[\cfrac{16}{625};3]
M[0]
M[0]
MAPE[\cfrac{1}{60};0.0001;3]
ME[\cfrac{5}{2};2]
M[0]
ME[\cfrac{1}{25};1]
M[0]
ME[\cfrac{16}{625};3]
ME[\cfrac{881}{12500};4]
ME[\cfrac{3}{2};2]
^^^
? Bepaal de verplaatsingen in $\rm{mm}$ met $B_{\rm{v}}$ en $N_{\rm{C}}$ in $\rm{kN}$.

- $V_{\rm{B}}^{\rm{AB}} \left( \rm{B}_{\rm{v}}, N_{\rm{C}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot N_{\rm{C}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$ (zorgt voor afschuiving van punt $\rm{B}$ naar rechts tov $\rm{A}$)
- $N_{\rm{AB}} \left( \rm{B}_{\rm{v}}, N_{\rm{C}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{kN}}\right) \cdot N_{\rm{C}} + $ {gap} $\left(\rm{in} \, \rm{kN}\right)$
- $w_{\rm{B}} \left( \rm{B}_{\rm{v}}, N_{\rm{C}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot N_{\rm{C}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$ (↑)
- $w_{\rm{B,h}} \left( \rm{B}_{\rm{v}}, N_{\rm{C}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot N_{\rm{C}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$ (→)
- $\Delta L_{\rm{BC}} \left( \rm{B}_{\rm{v}}, N_{\rm{C}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot N_{\rm{C}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$
- $w_{\rm{C}} \left( \rm{B}_{\rm{v}}, N_{\rm{C}}\right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot B_{\rm{v}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot N_{\rm{C}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$ (↗)

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
M[-30]
^^^
? Los de vormveranderingsvoorwaarden op om de statisch onbepaalde krachten te vinden.

- $B_{\rm{v}}= $ {gap} $\rm{kN}$
- $N_{\rm{C}}= $ {gap} $\rm{kN}$

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
M[288]
M[0]
M[72]
^^^
? Los nu ook de overige krachtenverdeling op.

- $M_{\rm{A}}= $ {gap} $\rm{kNm}$ (ᑐ)
- $N_{\rm{AB}}= $ {gap} $\rm{kN}$
- $\left| V_{AB} \right|= $ {gap} $\rm{kNm}$

---

::::
