# COZ opgave 2.2

::::::{note}
Deze opgave kan in ANS gemaakt worden.
::::::
% https://ans.app/repo_questions/....

Gegeven is de volgende constructie:

```{figure} coz_data/constructie2.svg
---
align: center
figclass: sticky-margin
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/matrixframe
---
Constructie
```

::::{admonition} Opgave
:class: exercise

Wat is de graad van uitwendig statisch bepaaldheid van deze constructie?

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

```{figure} coz_data/uitwerking2deel1.svg
:align: center
:source https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/blob/main/graad_statisch_coz
```

$ 3 - 3 = 0 $

::::

% solution_end

::::{admonition} Opgave
:class: exercise

Wat is de graad van inwendig statisch bepaaldheid van deze constructie?

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown


```{figure} coz_data/uitwerking2deel2.svg
:align: center
:source https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/blob/main/graad_statisch_coz
```
De graad van inwendig statisch onbepaaldheid is gelijk aan het aantal onbekenden minus het aantal vergelijkingen. De onbekenden zijn oplegreacties (3) en verbindingskrachten (30). De staven leveren 18 vergelijkingen en de knopen 15. Dat geeft:

$ 33 - 33 = 0 $

::::

% solution_end
