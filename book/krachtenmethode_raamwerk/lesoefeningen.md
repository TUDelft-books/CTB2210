# Begeleide oefening 1

Gegeven is de volgende 1ste graads statisch onbepaalde constructie:

```{figure-start} ./lesoefeningen_data/oefening_1.svg
:align: center
:figclass: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_3
:number:
```

- $EI_{\rm{AC}} = 20000 \ \rm{kNm^2}$
- $EI_{\rm{BC}} = \cfrac{2000 \sqrt{13}}{3} \ \rm{kNm^2}$
- $EA \gg EI $

```{figure-end}
```

::::{question} Opgave
:variant: multiple-select
:admonition:
:class: exercise
:nocaption:
:showanswer:
:columns: 1

Gegeven zijn de volgende statisch bepaalde systeem.

`````{grid} 2
:class-container: center-grid

````{grid-item}
:columns: auto

```{figure} ./lesoefeningen_data/statisch_bepaald_systeem_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_3
:number:
```

```` 
````{grid-item}

```{figure} ./lesoefeningen_data/statisch_bepaald_systeem_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_3
:number:
```
 
````
`````

Waarom zijn dit lastige constructies om op te lossen?

---
[ ] Met het koppel is het niet mogelijk verplaatsingen te berekenen.
> Onjuist, er zijn ook vergeet-me-nietjes met koppels
[x] Er zijn geen vergeet-me-nietjes voor deze situatie.
> Juist, de vorm van deze constructie als geheel én delen ervan zijn geen vergeet-me-nietjes
[ ] Het is überhaupt niet mogelijk verplaatsingen te berekenen voor een dergelijke constructie.
> Onjuist, hoewel er geen vergeet-me-nietjes zijn voor deze constructie kunnen we de constructie altijd oplossen met differentiaalvergelijkingen of andere methodes.
---

::::

Laten we de constructie oplossing met hoekveranderingsvergelijkingen, door een scharnier toe te voegen bij hoek $\rm{C}$. Daar werkt echter ook een uitwendig koppel. We voegen het scharnier daarom net links van het scharnier aan:

```{figure-start} ./lesoefeningen_data/scharnier_links_C.svg
:align: center
:figclass: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_3
:number:
```

- $EI_{\rm{AC}} = 20000 \ \rm{kNm^2}$
- $EI_{\rm{BC}} = \cfrac{2000 \sqrt{13}}{3} \ \rm{kNm^2}$
- $EA \gg EI $

```{figure-end}
```

:::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Schets de mogelijke vervormingen ten gevolge van het momentenpaar $M_{\rm{C}}^{\rm{AC}}$ op de statisch bepaalde constructie.
---
=

```{figure} ./lesoefeningen_data/verpl_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_3
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

Schets de mogelijke vervormingen ten gevolge van het uitwendige koppel van $30 \, \rm{kNm}$ op de statisch bepaalde constructie.
---
=

```{figure} ./lesoefeningen_data/verpl_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_3
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
M[0.001]
M[0]
M[-0.0005]
M[-0.015]
^^^
? Bepaal de hoeken $\varphi_{\rm{C}}^{\rm{AC}}$ en $\varphi_{\rm{C}}^{\rm{BC}}$ als functie van $M_{\rm{C}}^{\rm{AC}}$, met $M_{\rm{C}}^{\rm{AC}}$ in $\rm{kNm}$ en $\varphi$ in $\rm{rad}$.

- $\varphi_{\rm{C}}^{\rm{AC}} \left( M_{\rm{C}}^{\rm{AC}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot M_{\rm{C}}^{\rm{AC}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$
- $\varphi_{\rm{C}}^{\rm{BC}} \left( M_{\rm{C}}^{\rm{AC}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot M_{\rm{C}}^{\rm{AC}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$

---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

De uitdrukkingen voor de hoekverdraaiingen kunnen worden gevonden met behulp van het vergeet-mij-nietje voor een ligger op twee steunpunten belast door een koppel. 

$$ \varphi_{\rm{C}}^{\rm{AC}} \left( M_{\rm{C}}^{\rm{AC}} \right) = \cfrac{M_{\rm{C}}^{\rm{AC}} \cdot 6}{3 \cdot 2000} = 0.001 \cdot M_{\rm{C}}^{\rm{AC}} $$
$$ \varphi_{\rm{C}}^{\rm{BC}} \left( M_{\rm{C}}^{\rm{AC}} \right) = - \cfrac{\left(M_{\rm{C}}^{\rm{AC}} + 30 \right) \cdot \sqrt{13}}{3 \cdot \cfrac{2000 \cdot \sqrt{13}}{3}} = -0.0005 \cdot M_{\rm{C}}^{\rm{BC}} - 0.015  $$

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
M[-10]
^^^
? Los de vormveranderingsvoorwaarde op om $M_{\rm{C}}^{\rm{AC}}$ te vinden.

$M_{\rm{C}}^{\rm{AC}}= $ {gap} $\rm{kNm}$

---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

De vormveranderingsvoorwaarde is: $\varphi_{\rm{C}}^{\rm{AC}} = \varphi_{\rm{C}}^{\rm{BC}} \rightarrow M_{\rm{C}}^{\rm{AC}} = -10 \rm{kNm}$.

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
M[-20]
^^^
? Wat is het moment net onder knoop $\rm{C}$? Geef een positief antwoord voor een moment dat trek geeft aan de rechteronderzijde.

$M_{\rm{C}}^{\rm{BC}}= $ {gap} $\rm{kNm}$

---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Het moment is $-10 + 30 = 20 \rm{kNm}$ met druk aan de rechteronderzijde.

::::

% solution_end


:::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Bepaal de momentenlijn van de constructie.
---
=

```{figure} ./lesoefeningen_data/Momentenlijn.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_3
:number:
```

---

:::::
