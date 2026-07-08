````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze oefening is aangepast de [pagina over de krachtenmethode voor vakwerkconstructies](https://oit.tudelft.nl/CEG-mechanics-BSc/NL/statically_inderminate/force_method/extension.html) van {cite:ts}`CEG_mechanics_BSc`

```
````

# COZ opgave 2.3

::::::{note}
Deze opgave kan in ANS gemaakt worden.
:::{todo}
[Toevoegen link naar ANS toets.](https://github.com/TUDelft-books/CTB2210/issues/72)
:::
::::::

% https://ans.app/repo_questions/63917295/generator

Gegeven is de volgende constructie:

```{figure-start} coz_data/constructie3.svg
:align: center
:number:
:figclass: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_williot
```

$$0 < EA_{\rm{CD}}, EA_{\rm{BE}} \ll EI, EA_{\rm{ADE}}$$

```{figure-end}
```

Los de krachtsverdeling en vervormingen op met MatrixFrame.

::::{admonition} Opgave
:class: exercise

Wat is de verticale oplegreactie bij $\rm{B}$?

::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

$75 \, \rm{kN}$ omhoog

::::

% solution_end

::::{admonition} Opgave
:class: exercise

Wat is de normaalkracht in $\rm{CD}$?
::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

$22.5 \, \rm{kN}$

::::

% solution_end

::::{admonition} Opgave
:class: exercise

Wat is de normaalkracht in $\rm{BE}$?

::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

$-75 \, \rm{kN}$

::::

% solution_end

% solution_start

::::{admonition} Uitwerking MatrixFramebestand
:class: solution, dropdown

Het bestand van dit voorbeeld is [hier](./coz_data/coz3.mxf) te downloaden.

::::

% solution_end
