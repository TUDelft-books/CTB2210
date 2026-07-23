# COZ opgave 2.2

::::::{note}
Deze opgave kan in [ANS](https://ans.app/universities/1/courses/712480/assignments/1860496/go_to) gemaakt worden.

Als je nog geen toegang hebt tot deze toets, registreer je dan via [deze link](https://ans.app/accept/invitations/07b7bc5a-d334-43d7-9532-a1434730f6d7).

::::::
% https://ans.app/repo_questions/63870231/generator

Gegeven is de volgende constructie:

```{figure} coz_data/constructie2.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/matrixframe
---

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
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/matrixframe
:number:
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

```{figure} coz_data/uitwerking2deel2onbekenden.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/matrixframe
:number:

```

Er zijn 33 onbekende krachten

```{figure} coz_data/uitwerking2deel2vergelijkingen.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/matrixframe
:number:

```

Er zijn 33 evenwichtsvergelijkingen

$ 33 - 33 = 0 $

Indien er geen rekening is gehouden met pendelstaven komen er 6 onbekende krachten en 6 evenwichtsvergelijkingen bij.

::::

% solution_end
