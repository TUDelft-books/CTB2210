# Begeleide oefening 2

Gegeven is de volgende constructie:

```{figure} lesoefeningen_data/structure_3.svg
---
align: center
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/matrixframe
---
Constructie
```

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
MAP[7.78;0.1]
MAP[0.16;0.01]
MAP[0.66;0.01]
^^^
? Voer de linear-elastische berekening uit en bekijk de resultaten.

- Het moment in D is {gap} $\rm{kNm}$
- De maximale zakking is {gap} $\rm{m}$
- De absolute waarde van de rotatie van knoop A is {gap} $^\rm{o}$
---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Elke combinatie van stijfheden die leidt tot $EA = 800 \, \rm{kN}$ en $EI = 3 \rm{MNm^2}$ zal hetzelfde resultaat opleveren. De stijfheden van de staven kunnen dus vrij gekozen worden, zolang het product van $E$ en $A$ en het product van $E$ en $I$ maar gelijk is aan de genoemde waarden. Bijvoorbeeld:

- $A = 0.8 \, \rm{m^2}$
- $I = 3 \rm{m^4}$
- $E = 1000 \, \rm{kN/m^2}$

Het maximale moment in $\rm{D}$ kan worden gevonden met de spion functie als er geen knoop in $\rm{D}$ is. Als er wel een knoop in $\rm{D}$ is kan het moment direct in de algehele momentenlijn worden afgelezen. 

```{figure} lesoefeningen_data/image4.png
---
align: center
---
Moment in $\rm{D}$
```

De zakking kan afgelezen wroden uit de algehele verplaatsingen.

```{figure} lesoefeningen_data/image5.png
---
align: center
---
Maximale zakking
```

De rotatie kan in de tabel onderaan het scherm met knoopverplaatsingen worden afgelezen.

```{figure} lesoefeningen_data/image_3.png
---
align: center
---
Rotatie van knoop $\rm{A}$ in radialen
```

::::

::::::{admonition} Uitwerking MatrixFramebestand
:class: solution, dropdown

Het bestand van dit voorbeeld is [hier](./lesoefeningen_data/lesoefening_2.mxe) te downloaden.

::::::

% solution_end
