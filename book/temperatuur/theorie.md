# Instructie

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze theorie is aangepast van https://github.com/TUDelft-books/CEG-mechanics-BSc versie EN.
```
````

Elementen verlengen onder uniforme belasting met een extra rek van $\epsilon^{\rm{T}} = \alpha \ \Delta T$, waarbij $\alpha$ de lineaire uitzettingscoëfficiënt is. Wanneer een temperatuurverandering over de hoogte van een element optreedt, verlengen de vezels individueel, wat leidt tot buiging van elementen met een extra kromming van $\kappa^{\rm{T}} = \alpha \ \cfrac{\Delta T}{h}$, waarbij $h$ de hoogte van het element is. In statisch bepaalde constructies leidt dit tot extra spanningsloze rekken (en dus vervormingen) zonder invloed op de krachtverdeling, omdat de krachtverdeling onafhankelijk is van de vervormingen.

De vervorming kan worden gevonden door de spanningsloze rekken te integreren met behulp van de differentiaalvergelijkingen. Alternatief kan een equivalente belasting worden gebruikt die tot dezelfde kromming leidt, zodat de vergeet-me-nietjes toegepast kunnen worden. Dit vereist een kinematisch equivalente belasting die geen invloed heeft op reactiekrachten en interne krachten:

```{figure} ./temperature_data/kin_eq_load_SB.svg
:align: center

Kinematisch equivalente belasting die tot dezelfde rek en kromming leidt als rek door lineaire uitzetting
```

In statisch onbepaalde constructies zijn de vervorming en krachtverdeling gekoppeld, wat leidt tot reactiekrachten en interne spanningen door de (tegengehouden) vervormingen als gevolg van de temperatuurverandering. Deze krachten kunnen opnieuw worden gevonden door de rekken (zowel de spanningsveroorzakende rekken als spanningsloze temperatuurrekken) te integreren met behulp van de differentiaalvergelijkingen. Alternatief kan een kinematisch equivalente belasting, zoals bij statisch bepaalde constructies, worden toegepast in combinatie met de krachtmethode: de verplaatsingen door temperatuur worden meegenomen in de vormveranderingsvoorwaarden.

```{figure} ./temperature_data/kin_eq_load_SO.svg
:align: center

Kinematisch equivalente belasting die tot dezelfde rek en kromming leidt als rek door lineaire uitzetting, terwijl statisch onbepaalde reactiekrachten spanningen en reactiekrachten veroorzaken
```

De toepassing van temperatuursinvloeden op een statisch onbepaalde constructie wordt in een voorbeeld getoond met de krachtenmethode.

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze theorie is aangepast van https://github.com/TUDelft-books/CEG-mechanics-BSc versie 2024.
```
````

::::::{prf:example}
:nonumber: true
:label: temp_0

```{figure} ./theorie_data/structure2.svg
---
align: center
---
Voorbeeldconstructie
```

Het temperatuurverschil over de hoogte van de balk geeft de kromming $\kappa^{\rm{T}} = 10^{-5} \ \rm{m}^{-1}$ over de gehele lengte van de balk:

```{figure} ./theorie_data/curv_sun.svg
---
align: center
---
Krommingslijn
```

Om de kinematisch equivalente kracht te vinden moeten we de constructie eerste statisch bepaald maken. Dat kan bijvoorbeeld met het volgende statisch bepaalde systeem:

```{figure} ./theorie_data/structure_deter2.svg
---
align: center
---
Statisch bepaald systeem met vormveranderingsvoorwaarde
```

Voor dit systeem krijgen we met een koppel (↻) op het uiteinde van de balk dezelfde vorm van de krommingslijn. De waarde van dat koppel moet $M = \kappa \cdot EI = 6 \ \rm{kNm}$ zijn voor dezelfde kromming. Dat geeft het volgende statisch bepaalde systeem:

```{figure} ./theorie_data/structure_deter3.svg
---
align: center
---
Statisch bepaald systeem met vormveranderingsvoorwaarde en kinematisch equivalente belasting door de temperatuursinvloed
```

Nu kunnen we verder met de krachtenmethode zoals we die gewend zijn. De verplaatsing van $\rm{B}$ kan gevonden worden met vergeet-me-nietjes: $  w_{\rm{B}} = - \cfrac{6 \cdot 6 ^2}{2 \cdot 6000} + \cfrac{B_{\rm{v}} \cdot 6^3}{3 \cdot 6000}= -0.018 + \cfrac{3}{250}B_{\rm{v}}$.

Dit geeft $B_{v} = 1.5 \ \rm{kN}$

De momentenlijn en verplaatsingen kunnen nu gevonden worden. Voor de momentenlijn dient de kinematisch equivalente belasting van $6 \ \rm{kNm}$ niet te worden meegenomen, maar voor de verplaatsingen wel. Dit geeft:


```{figure} theorie_data/M-line.svg
:align: center

Momentenljin
```

```{figure} theorie_data/disp_total.svg
:align: center

Vervormde constructie
```

::::::

## Afleiding en meer voorbeelden
In hoofdstuk 4.12 van het boek Mechanica: spanningen, vervormingen en verplaatsingen {cite:p}`Hartsuijker2013` wordt de afleiding van temperatuursinvloeden behandeld. In hoofdstuk 6.2.1 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016` is deze versimpeld herhaald voor statisch bepaalde constucties. De aanpak met de momentenvlakstelling wordt niet behandeld in dit vak. Daarnaast worden de standaardgevallen voor een ligger op twee steunpunten en een ingeklemde ligger niet gebruikt. In hoofdstuk 6.2.2 worden statisch onbepaalde constructies behandeld. Ook hier geldt dat de momentenvlakstelling geen onderdeel is van dit vak

## Oefeningen
- Opgaves 6.25 - 6.30, 3.32 - 6.39, 6.41 - 6.43 in hoofdstuk 6.3 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Er zijn helaas geen antwoorden beschikbaar.