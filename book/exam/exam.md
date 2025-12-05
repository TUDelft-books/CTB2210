# Reguliere tentamenopdracht

% source files on https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam

Je eigen indiening en de beoordeling daarvan is hier te vinden: [<img height="12px" src="../figures/ANS.svg" alt="ANS"> tentamenopdracht Statisch onbepaalde constructies 1](https://ans.app/universities/1/courses/577550/assignments/1516051/go_to).

Gegeven is de volgende constructie:

```{figure} ./exam_data/constructie.svg
:align: center
```

:::::{exercise}
:label: exam_1_1
:nonumber: true

Laat zien dat deze constructie enkelvoudig statisch onbepaald is.

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Voor deze constructie is de inwendige statisch onbepaaldheid gelijk aan de uitwendig statisch onbepaaldheid.

```{figure} ./exam_data/statisch_onbepaaldheid.svg
:align: center
```

Er zijn 9 onbekenden en 8 evenwichtsvergelijkingen, waarmee is de constructie enkelvoudig statisch onbepaald.

::::

::::::{admonition} Veelgemaakte fouten
:class: remark, dropdown

**Statisch onbepaaldheid berekend met # oplegreacties - 3 evenwichtsvergelijkingen - # scharnieren**

Dit is een aanpak die in constuctiemechanica 1 is toegepast op scharnierliggers en driescharnierspanten, maar niet een methode die in het algemeen werkt. In dit geval komt de berekening echter wel op het goede antwoord uit: 7 oplegreacties - 3 evenwichtsvergelijkingen - 3 scharnieren = 1.

Als de constructie net anders zou zijn met het scharnier bij G in de ligger in plaats van daarboven, zou deze methode niet meer het juiste antwoord geven:

```{figure} ./exam_data/scharnier.svg
:align: center

Statisch bepaalde constructie met scharnier in de ligger in plaats van daarboven
```

De foutieve methode zou dan nog steeds op eerstegraads statisch onbepaald uitkomen, terwijl de juiste methode laat zien dat de constructie nu statisch bepaald is:

```{figure} ./exam_data/SOB2.svg
:align: center

Graad van statisch onbepaaldheid voor de constructie met scharnier in de ligger
```

Er zijn 13 onbekenden en 13 evenwichtsvergelijkingen, daarmee is de constructie met de juiste methode dus statisch bepaald

**Constructie niet uit elkaar in scharniende delen**

Voor het berekenen van de statisch onbepaaldheid moet de constructie in alle scharnierende delen uit elkaar gehaald worden. Als dat niet gebeurt kan de statisch onbepaaldheid verkeerd worden berekend.

```{figure} exam_data/niet-uit-elkaar.svg
:align: center

Constructie onterecht niet volledig uit elkaar gehaald.
```

**2 evenwichtsvergelijkingen voor star lichaam met krachten op uiteindes**

Het aantal evenwichtsvergelijkingen voor een star lichaam is altijd gelijk aan 3, tenzij we het kunnen versimpelen tot een pendelstaaf: dan zijn alleen de krachten in de richting van de staaf onbekend en is er maar 1 evenwichtsvergelijking nodig (in de richting van de staaf). 2 evenwichtsvergelijkingen voor een staaf is dus niet mogelijk; het niet aanwezig zijn van een koppel betekent niet dat er geen momentenevenwichtsvergelijking kan worden toegepast

```{figure} exam_data/pendelstaaf.svg
:align: center

Star lichaam met krachten op uiteindes
```

::::::


:::::{exercise}
:label: exam_1_2
:nonumber: true

Geef vier geldige varianten om deze constructie statisch bepaald te maken ten behoeve van de krachtenmethode of verplaatsingenmethode met statisch onbepaalde verplaatsingen. Zorg voor vier verschillende varianten: je aanpassingen moeten elk een ander onderdeel van de constructie aanpassen.
Geef bij elk van de varianten de benodigde vergelijking(en) om de statisch onbepaalde kracht(en) of statisch onbepaalde verplaatsing(en) mee te kunnen bepalen.

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Een scharnier toevoegen in hetzelfde segment of een pendelstaaf loshalen in hetzelfde segment telt niet als een geldige variant.

Een aantal mogelijk opties zijn

```{figure} ./exam_data/SB_1.svg
:align: center
```

```{figure} ./exam_data/SB_2.svg
:align: center
```

```{figure} ./exam_data/SB_3.svg
:align: center
```

```{figure} ./exam_data/SB_4.svg
:align: center
```

::::

::::::{admonition} Veelgemaakte fouten
:class: remark, dropdown

**Mechanisme gecreëerd**

Er kunnen op verschillende manieren mechanismes worden gecreëerd:

`````{tab-set}
````{tab-item} Losmaken horizontale oplegging bij $\rm{A}$

```{figure} ./exam_data/mechanisme1.svg
:align: center
```

De ligger $\rm{AGJK}$ kan nu vrij naar links en rechts bewegen.
````

````{tab-item} Losmaken horizontale oplegging bij $\rm{D}$

```{figure} ./exam_data/mechanisme2.svg
:align: center
```

Pendelstaaf $\rm{DK}$ kan nu vrij roteren rondom $\rm{K}$
````

````{tab-item} Losmaken horizontale oplegging bij $\rm{C}$

```{figure} ./exam_data/mechanisme3.svg
:align: center
```

Pendelstaaf $\rm{BOC}$ kan nu vrij naar links en rechts bewegen.
````

````{tab-item} Scharnier toevoegen in staaf $\rm{OG}$

```{figure} ./exam_data/mechanisme4.svg
:align: center
```

Het toegevoegde scharnier kan nu vrij naar links en rechts bewegen.
````

````{tab-item} Scharnier toevoegen in staaf $\rm{DK}$

```{figure} ./exam_data/mechanisme5.svg
:align: center
```

Het toegevoegde scharnier kan nu vrij naar links en rechts bewegen.
````


`````

**Verplaatsingenmethode met vrijheidsgraden**

Hoewel de verplaatsingemethode met vrijheidsgraden een prima methode is om de statisch onbepaalde constructie door te rekenen, is het niet een geldige statisch bepaalde constructie.

```{figure} ./exam_data/verplaatsingenmethode.svg
:align: center

Mogelijk constructie voor verplaatsingenmethode met vrijheidsgraden
```

**Onterecht verplaatsing gelijk stellen aan $0$**

In sommige gevallen wordt een verplaatsing onterecht gelijk gesteld aan $0$, terwijl deze verplaatsing juist onbekend is en alleen maar gelijk gesteld kan worden aan een andere onbekende verplaatsing.

```{figure} ./exam_data/gelijkaan0.svg
:align: center

Ten onrechte zeggen dat de verplaatsingen niet alleen aan elkaar gelijk zijn, maar ook gelijk aan $0$.
```

::::::

:::::{exercise}
:label: exam_1_3
:nonumber: true

Bepaal de zakking in $\rm{G}$ met behulp van de krachtenmethode of verplaatsingenmethode.

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Als voorbeeld is de krachtenmethode toegepast met het volgende statisch bepaalde system bekeken, maar andere methodes zijn ook goed:

```{figure} ./exam_data/SB_5.svg
:align: center
```

```{figure} ./exam_data/FBD_D.svg
:align: center
```

$$\sum {F_{\rm{v}}} = 0 \to N_{\rm{DK}} = D_{\rm{v}}$$

```{figure} ./exam_data/FBD_AK.svg
:align: center
```

$$\sum {T_{\rm{A}}} = 0 \to N_{\rm{OG}} = 66 - 3 \cdot D_{\rm{v}}$$

```{figure} ./exam_data/BC.svg
:align: center
```

Vergeet-me-nietje geeft:

$$w_{\rm{O}} = 0.022 - 0.001 \cdot D_{\rm{v}}$$

```{figure} ./exam_data/OG.svg
:align: center
```

Verlenging van staaf geeft:

$$w_{\rm{G}} = 0.22 - 0.01 \cdot D_{\rm{v}}$$

```{figure} ./exam_data/AK.svg
:align: center
```

Rotatie van starre staaf geeft:

$$w_{\rm{K}} = 0.66 - 0.03 \cdot D_{\rm{v}}$$

```{figure} ./exam_data/DK.svg
:align: center
```

Verlenging van staaf geeft:

$$w_{\rm{D}} = 0.66 - 0.033 \cdot D_{\rm{v}}$$

Oplossen van de vormveranderingsvoorwaarde geeft: $w_{\rm{D}} =0 \to D_{\rm{v}} = 20 \ \rm{ kN}$

Invullen in $w_{\rm{G}} = 0.22 - 0.01 \cdot D_{\rm{v}}$ geeft: $w_{\rm{G}} = 20 \ \rm{ mm}$

::::

:::::{exercise}
:label: exam_1_4
:nonumber: true

Bepaal de normaalkracht in $\rm{DK}$ in de extreme gevallen dat de $EA_{\rm{OG}} \to 0$ en $EA_{\rm{OG}} \to \infty$.

:::::

::::::{admonition} Veelgemaakte fouten
:class: remark, dropdown

**Constructie foutief versimpelen / starre rotaties niet meegenomen**

De constructie wordt op verschillende manieren verkeerde versimpeld door verplaatsingen / krachten te negeren en/of opleggingen toe te voegen. Daarnaast worden starre rotaties van delen van de constructie soms niet meegenomen.

```{figure} ./exam_data/versimpelen.svg
:align: center

Boven voorbeeld van foutieve versimpeling door vervormingen van pendelstaven en $\rm{BC}$ te negeren en de verplaatsingen van $\rm{G}$ en $\rm{K}$ gelijk te stellen aan $0$. Daarnaast worden niet aanwezige vervormingen geïntroduceerd in the starre staaf. De hoekverandering zou een resultaat moeten zijn van de vervormingen van de niet starre delen (zoals onder getoond)
```

**Rekstijfheid negeren**
De rekstijfheid van de pendelstaven wordt ten onrechte genegeerd, waardoor de verplaatsingen enkel een functie wordt van de buigende delen

```{figure} ./exam_data/starre_staven.svg
:align: center

Foutieve aanpassing waarbij de rekstijfheid van de pendelstaven oneindig groot wordt gemaakt.
```

**Constructie oplossen met enkel (foutieve) evenwichtsvergelijkingen**

De constructie wordt opgelost met enkel evenwichtsvergelijkingen door delen van de constructie te negeren. Zodra er krachten worden berekend zonder dat er vervormingen worden meegenomen kan de berekening niet kloppen.

```{figure} ./exam_data/evenwicht.svg
:align: center

Foutief vrijlichaamsschema van $\rm{AK}$ waarbij de pendelstaaf $\rm{OG}$ wordt genegeerd. Nu kunnen direct oplegreacties/inwendige krachten worden berekend
```

::::::

:::::{admonition} Oplossing
:class: solution, dropdown

Voor $EA_{\rm{OG}} \to 0$ verandert de constructie in twee statisch bepaalde systemen:

```{figure} ./exam_data/EA0.svg
:align: center
```

Dit geeft met evenwicht:

```{figure} ./exam_data/FBD_AK2.svg
:align: center
```

$$\sum {T_{\rm{A}}} = 0 \to N_{\rm{DK}}= 22 \ \rm{ kN}$$

Voor $EA_{\rm{OG}} \to \infty$ is $w_{\rm{O}}$ gelijk aan $w_{\rm{G}}$. Gebruikmakend van de berekeningen van de vorige vraag geeft $N_{\rm{DK}} = 11 \ \rm{ kN}$.

::::

::::::{admonition} Veelgemaakte fouten
:class: remark, dropdown

**$EA \to \infty $ geeft $N \to \infty$**

De relatie $N = EA \cdot \epsilon$ wordt onterecht geïnterpreteerd als dat als $EA \to \infty$, dan ook $N \to \infty$. Echter het enige wat geldt is dat als $EA \to \infty$, dan zal $\epsilon \to 0$ (geen rek); de kracht $N$ kan nog steeds een eindige waarde hebben.

**$EA \to \infty $ geeft verplaatsingen van 0**

Hoewel de pendelstaaf oneindig staaf wordt, kan deze nog steeds verplaatsingen overdragen tussen beide liggers. De verplaatsing van de pendelstaaf wordt soms ten onrechte volledig genegeerd, terwijl de oneindige stijve pendelstaaf nog steeds de verplaatsingen van de buigende ligger kan overdragen naar de andere ligger.

```{figure} ./exam_data/teveel_oneindig.svg
:align: center

Niet overdragen van verplaatsingen door oneindig stijve pendelstaaf komt neer op het modelleren als de andere ligger ook als oneindig stijf
```

::::::