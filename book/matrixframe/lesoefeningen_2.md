# Begeleide oefening 2

Gegeven is de volgende constructie:

```{figure} lesoefeningen_data/structure_3.svg
---
align: center
---
Constructie, $EA = 800 \ \rm{kN}, EI = 3 \ \rm{MNm^2}$
```

Bepaal de oplegreacties, verplaatsingen en het krachtsverloop in de constructie met MatrixFrame.

:::::{exercise}
:label: mf_3_1
:nonumber: true

Voer de geometrie, profielgegevens, opleggingen en scharnierende aansluitingen in, voer de linear-elastische berekening uit en bekijk de resultaten.

```{h5p} https://tudelft.h5p.com/content/1292628975060884047/embed
```

:::::

% solution_start

::::{admonition} Solution
:class: solution, dropdown

- Het moment in D is *7.78* kNm
- De maximale zakking is *0.16* m
- De absolute waarde van de rotatie van knoop A is *0.66* graden

```{figure} lesoefeningen_data/image4.png
---
align: center
---
Moment in D
```

```{figure} lesoefeningen_data/image5.png
---
align: center
---
Maximale zakking
```

```{figure} lesoefeningen_data/image_3.png
---
align: center
---
Rotatie van knoop A in radialen
```

::::

% solution_end

:::::{margin}
::::{versionadded} v2025.1.1
2025-09-03: Matrixframe bestand toegevoegd
::::
:::::

::::::{hint}

Het bestand van dit voorbeeld is [hier](./lesoefeningen_data/lesoefening_2.mxe) te downloaden.

::::::