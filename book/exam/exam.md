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
```

De foutieve methode zou dan nog steeds op eerstegraads statisch onbepaald uitkomen, terwijl de juiste methode laat zien dat de constructie nu statisch bepaald is:

```{figure} ./exam_data/SOB2.svg
:align: center
```

Er zijn 13 onbekenden en 13 evenwichtsvergelijkingen, daarmee is de constructie met de juiste methode dus statisch bepaald

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