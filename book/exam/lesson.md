# 3 november: Tentamenopdracht

Gegeven is de volgende constructie:

```{figure} ./lesson_data/constructie1.svg
:align: center
:figclass: sticky-margin
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

:::::{exercise}
:nonumber: true

Laat zien dat deze constructie inwendig tweedegraads statisch onbepaald is.

:::::

:::::{exercise}
:nonumber: true

Geef vijf verschillende statisch bepaalde varianten van deze constructie voor het toepassen van de krachtmethode. Het maken van een identieke aanpassing op twee punten in hetzelfde element telt niet als een andere variant.

Voor elk van de varianten:

- Geef de noodzakelijke vormveranderingsvoorwaardes om de statisch onbepaalde krachten te bepalen
- Leg uit waarom jouw varianten geen mechanismen zijn op basis van tekeningen van de vervormde constructies.

:::::

```{hide-sticky-margin}
```

Gegeven de volgende constructie. Merk op dat de verticale roloplegging bij $\rm{C}$ is verwijderd.

```{figure-start} ./lesson_data/constructie2.svg
:align: center
:figclass: sticky-margin
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

- $EA_{\rm{BC}} = 14.4 \, \rm{MN}$
- $EI_{\rm{CDA}} = 62720 \, \rm{kNm}^2$
- $EA_{\rm{CDA}} \gg EI_{\rm{CDA}} $

```{figure-end}
```

:::::{exercise}
:nonumber: true

Los je statisch onbepaalde kracht op met behulp van de krachtmethode op basis van een statisch bepaalde constructie naar keuze.

:::::

:::::{exercise}
:nonumber: true

Vanwege welke beperking(en) is het, voor de matrixmethode zoals die in deze cursus is behandeld, niet mogelijk om de matrixmethode toe te passen op deze constructie. Ter informatie, de matrixmethode in deze cursus was gebaseerd op deze enkele stijfheidsmatrix:

$$
\mathbf{K^{\rm{(e)}}} &= \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2 EI}{L} \\ \cfrac{2 EI}{L} & \cfrac{4 EI}{L} \end{bmatrix}
$$

:::::

::::{admonition} Solution
:class: solution, dropdown

- Verplaatsbare knopen
- Scharnieren
- Belastingen op elementen

::::
