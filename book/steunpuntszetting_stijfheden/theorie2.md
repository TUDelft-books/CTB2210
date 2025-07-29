# Theorie stijfheidsinvloeden

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze theorie is aangepast van https://github.com/TUDelft-books/CEG-mechanics-BSc versie EN.
```
```` 

Verschillen in stijfheden zorgen bij statisch bepaalde constructies niet voor een krachtsherverdeling, enkel op de verplaatsingen. Bij statisch onbepaalde constructies zorgen stijfheidsverschillen ook voor verschillen in de krachtsverdeling. Het analyseren van de invloed hiervan kan erg interessant zijn.

Er zijn twee manieren om de stijfheidsinvloeden te analyseren:

1. Onderzoek extremen: bekijk beide gevallen van $EI = 0$ of $EA = 0$ en $EI = \infty$ of $EA = \infty$. Hiermee kun je de uiterste gevallen van krachten en de omhullende van inwendige krachten/verplaatsingen bepalen. Alle werkelijke stijfheidswaarden moeten binnen deze envelop liggen. Bij deze analyse vereenvoudigt een statisch bepaalde constructie soms tot een statisch bepaalde constructie.
2. Los op met een onbekende vermenigvuldigingsfactor $n \cdot EI$ of $n \cdot EA$. Dit geeft een uitdrukking voor krachten/verplaatsingen en maakt het mogelijk een asymptotische grafiek te maken ten opzichte van $n$. Bij deze aanpak dient altijd een statisch bepaalde constructies opgelost te worden met een methode naar keuze.

We behandelen beide aanpakken op de volgende constructie:

````{margin}
```{attributiongrey} Attribution
:class: attribution

Dit voorbeeld is aangepast van https://github.com/TUDelft-books/CT1000 versie CTB2210-2025.
```
```` 

