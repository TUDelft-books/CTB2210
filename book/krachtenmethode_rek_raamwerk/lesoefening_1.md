# Begeleide oefening 1

...
```{figure-start} ./lesoefeningen_data/constructie.svg
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

```{figure} ./lesoefeningen2_data/aanpassing1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
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
> Er zijn drie aanpassingen gedaan, waarvan elke aanpassing de graad van statische onbepaaldheid met 1 verlaagd.
[ ] Deze constructie is een mechanisme.
> Er zijn geen globale of lokale mechanismes! Het scharnier halverwege $\rm{B}$ en $\rm{C}$ kan niet vrij bewegen aangezien staaf $\rm{AB}$ weerstand biedt voor de rotatie van knoop $\rm{B}$.
---

:::::

:::::{question}
:type: no-input
:nocaption:
:showanswer:

Schets de mogelijke vervormingen ten gevolge van de verdeelde belasting:

---
=

```{figure} ./lesoefeningen2_data/aanpassing1_verplaatsing.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
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
> De zakking van het scharnier halverwege $\rm{B}$ en $\rm{C}$ maakt het lastiger om de verplaatsingen te berekenen.
[x] Het kan, maar er zijn betere opties
[ ] Nee
> Deze constructie is statisch bepaald en daarmee geschikt!
---

:::::

::::::