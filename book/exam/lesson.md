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

::::{admonition} Uitwerking
:class: solution, dropdown

De constructie is open, dus de inwendige graad is gelijk aan de uitwendige graad. De vormvaste scharnierende delen zijn de volgende:

```{figure} ./lesson_data/stat_bepaald.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Er zijn dus $3 + 1 + 2 + 2 = 8$ onbekenden en $3 + 3 = 6$ evenwichtsvergelijkingen, dus de constructie is uit- en inwendig tweedegraads statisch onbepaald.

::::

:::::{exercise}
:nonumber: true

Geef vijf verschillende statisch bepaalde varianten van deze constructie voor het toepassen van de krachtmethode. Het maken van een identieke aanpassing op twee punten in hetzelfde element telt niet als een andere variant.

Voor elk van de varianten:

- Geef de noodzakelijke vormveranderingsvoorwaardes om de statisch onbepaalde krachten te bepalen
- Leg uit waarom jouw varianten geen mechanismen zijn op basis van tekeningen van de vervormde constructies.

:::::

::::::{admonition} Uitwerking
:class: solution, dropdown

:::::{grid}
:class-container: center-grid
:gutter: 1

::::{grid-item-card}
:columns: 6

```{figure} ./lesson_data/variant1.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Deze variant vervormt als volgt t.g.v. de  
verdeelde belasting:

```{figure} ./lesson_data/variant1_def.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

En is dus geen mechanisme.

::::

::::{grid-item-card}
:columns: 6

```{figure} ./lesson_data/variant2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Deze variant vervormt als volgt t.g.v. de  
verdeelde belasting:

```{figure} ./lesson_data/variant2_def.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

En is dus geen mechanisme.

::::

::::{grid-item-card}
:columns: 6

```{figure} ./lesson_data/variant3.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Deze variant vervormt als volgt t.g.v. de  
verdeelde belasting:

```{figure} ./lesson_data/variant3_def.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

En is dus geen mechanisme.

::::

::::{grid-item-card}
:columns: 6

```{figure} ./lesson_data/variant4.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Deze variant vervormt als volgt t.g.v. de  
verdeelde belasting:

```{figure} ./lesson_data/variant4_def.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

En is dus geen mechanisme.

::::

:::::
::::::

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

::::::{admonition} Uitwerking
:class: solution, dropdown

De constructie is eerstegraads statisch onbepaald. Deze zou als volgt kunnen worden aangepast:

```{figure} ./lesson_data/statisch_bepaald.svg
:align: center
:number:
:figclass: sticky-margin
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Dit geeft de volgende vervormingen:

:::::{grid}
:class-container: center-grid

::::{grid-item}
:columns: auto

```{figure} ./lesson_data/vervorming_1.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

::::

::::{grid-item}
:columns: auto

```{figure} ./lesson_data/vervorming_2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

::::

::::{grid-item}
:columns: auto

```{figure} ./lesson_data/vervorming_3.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

::::

:::::

De hoek $\varphi_{\rm{D}}^{\rm{AD}}$ kan worden berekend met behulp van het vergeet-me-nietje van een uitkragende ligger met een koppel op het uiteinde:

$$ \varphi_{\rm{D}}^{\rm{AD}} = - \cfrac{M_{\rm{D}} \cdot 3}{3 \cdot 62720} = - \cfrac{3 \cdot M_{\rm{D}}}{62720} $$

De zakking van $\rm{C}$ kan worden berekend met de verlenging van een starre staaf, daarvoor moet eerst de normaalkracht in $\rm{BC}$ worden berekend:

```{figure} ./lesson_data/VLS_CD.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

$$
\begin{align*}
\left. T \right|_{\rm{D}} &= 0 \\
N_{\rm{BC}} \cdot 7 - 32 \cdot 7 \cdot 3.5 - M_{\rm{D}} &= 0 \\
N_{\rm{BC}} &= 112 + \cfrac{M_{\rm{D}}}{7}
\end{align*}
$$

Nu kan de zakking van $\rm{C}$ worden berekend met behulp van de verlenging van een starre staaf:

$$ w_{\rm{C}} = \cfrac{N_{\rm{BC}} \cdot 3}{14.4 \cdot 10^3} = \cfrac{7}{300} + \cfrac{M_{\rm{D}}}{33600} \left( \downarrow \right) $$

De hoek $\varphi_{\rm{D}}^{\rm{CD}}$ kan worden berekend met behulp van het vergeet-me-nietje van een ligger op twee steunpunten met een koppel op het uiteinde, een ligger op twee steunpunten met een verdeelde belasting, en de starre rotatie door de zakking van $\rm{C}$:

$$ \varphi_{\rm{D}}^{\rm{CD}} = \cfrac{M_{\rm{D}} \cdot 7}{3 \cdot 62720} + \cfrac{32 \cdot 7^3}{24 \cdot 62720} + \cfrac{w_{\rm{C}}}{7} = \cfrac{17}{1600} + \cfrac{13 \cdot M_{\rm{D}}}{313600} $$

Nu kan de vormveranderingsvoorwaarde worden opgelost:

$$
\begin{align*}
\varphi_{\rm{D}}^{\rm{AD}} &= \varphi_{\rm{D}}^{\rm{CD}} \\
- \cfrac{3 \cdot M_{\rm{D}}}{62720} &= \cfrac{17}{1600} + \cfrac{13 \cdot M_{\rm{D}}}{313600} \\
M_{\rm{D}} &= -119 \, \rm{kNm}
\end{align*}
$$

::::::

:::::{exercise}
:nonumber: true

Vanwege welke beperking(en) is het, voor de matrixmethode zoals die in deze cursus is behandeld, niet mogelijk om de matrixmethode toe te passen op deze constructie. Ter informatie, de matrixmethode in deze cursus was gebaseerd op deze enkele stijfheidsmatrix:

$$
\mathbf{K^{\rm{(e)}}} = \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2 EI}{L} \\ \cfrac{2 EI}{L} & \cfrac{4 EI}{L} \end{bmatrix}
$$

:::::

::::{admonition} Uitwerking
:class: solution, dropdown

De constructie heeft:

- Verplaatsbare knopen
- Scharnieren
- Belastingen op elementen

Welke allemaal niet meegenomen worden in de elementsstijfheidsmatrix zoals die in deze cursus is behandeld.

::::
