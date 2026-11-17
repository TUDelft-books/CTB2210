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

:::{admonition} Alternatieve aanpak met de inwendige statische onbepaaldheid
:class: note, dropdown

De inwendige graad van statische onbepaaldheid kan ook volledig worden berekend (zonder deze gelijk te stellen aan de uitwendige graad):

```{figure} ./lesson_data/inwendig.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Er zijn $3 + 3 + 3 + 2 + 1 +  1 + 1 + 1 = 15$ onbekenden en $3 + 3 + 3 + 2 + 1 + 1 = 13$ evenwichtsvergelijkingen, dus de constructie is inwendig tweedegraads statisch onbepaald.

:::

::::

::::::{admonition} Veelgemaakte fouten
:class: remark, dropdown

**Statische bepaaldheid berekend met # oplegreacties - 3 evenwichtsvergelijkingen - # scharnieren**

Deze aanpak werkt niet in het algemeen, maar geeft in dit geval wel het juiste antwoord: 6 oplegreacties - 3 evenwichtsvergelijkingen - 1 scharnier = 2.

**Onjuist gemodelleerde pendelstaaf**

Het element $\rm{BC}$ is een pendelstaaf, dus de inwendige krachten in dit element zijn uitsluitend normaalkrachten. Daarom kan het aantal onbekenden aan de uiteinden van dit element worden teruggebracht tot één per uiteinde. Voor het element geldt dan één evenwichtsvergelijking. Ook kan het aantal evenwichtsvergelijkingen voor de aangesloten elementen afnemen wanneer de inwendige statische onbepaaldheid wordt berekend. Een juiste aanpak is:

```{figure} ./lesson_data/pendelstaaf.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Er zijn fouten gemaakt in het aantal onbekenden aan de aansluitingen $\rm{B}$ en $\rm{C}$ en in het aantal evenwichtsvergelijkingen.

::::::

:::::{exercise}
:nonumber: true

Geef vijf verschillende statisch bepaalde varianten van deze constructie voor het toepassen van de krachtmethode. Het maken van een identieke aanpassing op twee punten in hetzelfde element telt niet als een andere variant.

Voor elk van de varianten:

- Geef de noodzakelijke vormveranderingsvoorwaardes om de statisch onbepaalde krachten te bepalen
- Leg uit waarom jouw varianten geen mechanismen zijn op basis van tekeningen van de vervormde constructies.

:::::

::::::{admonition} Uitwerking
:class: solution, dropdown

Bijvoorbeeld de volgende varianten:

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
:name: variant2_def
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

::::::{admonition} Veelgemaakte fouten
:class: remark, dropdown

**Een mechanisme gemaakt**

De scharnierende oplegging bij $\rm{B}$ vervangen door een horizontale roloplegging of de oplegging helemaal weggelaten. Dit is geen statisch bepaalde variant, omdat de constructie dan een mechanisme is:

:::::{grid}
:class-container: center-grid
:gutter: 1

::::{grid-item-card}
:columns: 6

```{figure} ./lesson_data/variant5.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Deze variant vervormt onder invloed van de statisch onbepaalde kracht als volgt:

```{figure} ./lesson_data/variant5_def.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

::::

::::{grid-item-card}
:columns: 6


```{figure} ./lesson_data/variant6.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Deze variant vervormt onder invloed van de statisch onbepaalde kracht als volgt:

```{figure} ./lesson_data/variant6_def.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

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

:::{admonition} Alternatief met een verticale roloplegging bij $\rm{B}$
:class: note, dropdown

Een andere mogelijke oplossing is de constructie als volgt aan te passen:

```{figure} ./lesson_data/stat_bepaald_2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Ook andere oplossingen zijn mogelijk.

:::

Dit geeft de volgende vervormingen:

:::::{grid}
:class-container: center-grid

::::{grid-item}
:columns: auto

```{figure} ./lesson_data/vervorming_1.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
:name: vervorming_1
```

::::

::::{grid-item}
:columns: auto

```{figure} ./lesson_data/vervorming_2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
:name: vervorming_2
```

::::

::::{grid-item}
:columns: auto

```{figure} ./lesson_data/vervorming_3.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
:name: vervorming_3
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

::::::{admonition} Veelgemaakte fouten
:class: remark, dropdown

**Verlenging van $\rm{BC}$ niet meegenomen**

De verlenging van $\rm{BC}$ is niet meegenomen in de vervormingen, terwijl deze wel invloed heeft op de vormveranderingsvoorwaarde. Zoals in de onderstaande figuren te zien is, vergroot de verlenging van $\rm{BC}$ de rotatie bij $\rm{D}$.

:::::{grid}
:class-container: center-grid

::::{grid-item}
:columns: auto

:::{fetch} {ref}`vervorming_1`
:::

::::

::::{grid-item}
:columns: auto

:::{fetch} {ref}`vervorming_2`
:::

::::
:::::

**Vervorming van $\rm{AD}$ niet meegenomen**

De vervorming van $\rm{AD}$, of meer specifiek de rotatie van $\rm{D}$ als gevolg van de buiging van $\rm{AD}$, is niet meegenomen in de vervormingen, terwijl deze wel invloed heeft op de vormveranderingsvoorwaarde. Zoals in de onderstaande figuren te zien is, vergroot de buiging van $\rm{AD}$ de rotatie bij $\rm{D}$. Deze fout werd vooral gemaakt bij het oplossen van het statisch bepaalde systeem met een verticale roloplegging bij $\rm{B}$.

:::{fetch} {ref}`variant2_def`
:::

**Vergeet-me-nietjes voor statisch onbepaalde systemen gebruikt**

Met de krachtmethode is een statisch bepaalde constructie gemaakt, dus de vergeet-me-nietjes voor statisch onbepaalde constructies zijn niet nodig. In het hier getoonde antwoord is bijvoorbeeld voor $\rm{AD}$ het vergeet-me-nietje voor een uitkragende ligger met een extra steunpunt gebruikt, terwijl dat voor een uitkragende ligger met een eindmoment had moeten zijn. Dit is te zien aan de vervormde constructie:

:::{fetch} {ref}`vervorming_3`
:::

**Statisch bepaalde constructie die niet eenvoudig met vergeet-me-nietjes op te lossen is**

```{figure} ./lesson_data/variant7.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Deze variant vervormt onder invloed van de statisch onbepaalde kracht als volgt:

```{figure} ./lesson_data/variant7_def.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

Deze is niet eenvoudig met de vergeet-me-nietjes op te lossen.

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

::::::{admonition} Veelgemaakte fouten
:class: remark, dropdown

**Numerieke waarden van de stijfheden ontbreken**

Het ontbreken van de buigstijfheid van $\rm{BC}$ en de zeer hoge axiale stijfheid van $\rm{CDA}$ zijn geen reden waarom de matrixmethode niet kan worden toegepast. Hoewel numerieke waarden nodig kunnen zijn, kunnen willekeurige waarden of waarden die bij benadering kloppen worden gebruikt, wat tot de juiste resultaten leidt.

**Niet-uniforme stijfheden**

In de matrixmethode kan elk element eigen waarden voor $EI$ en $EA$ hebben, dus ook dit is geen reden waarom de matrixmethode niet kan worden toegepast.

::::::
