````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze pagina is aangepast van [deze pagina over de krachtenmethode](https://oit.tudelft.nl/CEG-mechanics-BSc/NL/statically_inderminate/force_method/bending2.html) van {cite:ts}`CEG_mechanics_BSc`

```
```` 

(krachtenmethode_raamwerk)=
# Instructie

De krachtenmethode hebben we eerder al behandeld voor onder andere [constructies belast op rek](krachtenmethode_simpel) en [balken](krachtenmethode_balk). Voor raamwerken is de procedure niet anders, behalve dat we het gedrag van rek en buiging niet altijd kunnen splitsen en dat bij samenkomst van meerdere staven / uitwendige koppels we even goed moeten nadenken over de locatie van de schieren. In deze les zal het enkel gaan over raamwerken die enkel vervormen door buiging, dus $EA >> EI$. In de [volgend les](../krachtenmethode_rek_raamwerk/lesson.md) zullen we de krachtenmethode behandelen voor raamwerken die vervormen door zowel buiging als rek.

## Samenkomst van meerdere staven en/of uitwendige koppels

Stel ergens in de constructie komen meerdere staven en/of uitwendige koppels samen:

```{figure} ./theorie_data/knooppunt.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
number:
---

```

Als je daar een scharnier wilt toevoegen met een momentenpaar geldt de gebruikelijke procedure, maar over de plek moeten we even goed nadenken. Als je het scharnier in het kruispunt aanbrengt loop je nameljk tegen een paar vragen op:

```{figure} ./theorie_data/knooppunt_vraagteken.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
number:
---

```

- Hoeveel neemt de graad van statisch onbepaaldheid af met dit ene scharnier?
- Eén scharnier met drie momenten? Is dat nog een momentenpaar?
- Welke momenten zijn nu aan elkaar gelijk?
- Wat moet je met het moment van het uitwendige koppel? Hoe kan een koppel aangrijpen op een scharnier?
- Oke, alle hoeken zullen aan elkaar gelijk moeten zijn, maar dat zijn niet genoeg vergelijkingen voor drie onbekende momenten.

:::{note}
In het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016` worden wel scharnieren in het knooppunt geplaatst met een extra trucje. Deze aanpak is toegestaan maar wordt niet aangeraden.
:::

Het is verstandiger om deze scharnieren nét naast de knoop te plaatsen. Dat zorgt ervoor dat de momentenparen van de staven en het uitwendige koppel niet op dezelfde plek aangrijpen, de graad van statisch onbepaaldheid afneemt met 1 per scharnier, en dat bij elk scharnier er, zoals gebruikelijk, twee hoeken zijn die aan elkaar gelijk moeten zijn:

```{figure} ./theorie_data/knooppunt_nieuw.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
number:
---

```

In bovenstaande voorbeeld zijn twee scharnieren genoeg om de uiteindes van elk van de staven kunnen roteren ten opzichte van de andere staven. Het enige afwijkende ten opzicht van onze analyses tot nu toe is dat er op een van de staven nu niet één moment, maar meerdere momenten aangrijpen. In bovenstaande afbeelding werken op de linkerstaaf drie momenten: één uitwendig koppel en twee momenten van de scharnieren.

::::{warning}
Pas bij het aanbrengen van scharnieren op dat je niet aan alle zijdes van het knooppunt een scharnier aanbrengt. Dat zou namelijk een lokaal mechanisme opleveren, waarbij de knoop kan roteren:

```{figure} ./theorie_data/knooppunt_mechanisme.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
number:
---

```

::::

## Voorbeeld

We behandelen de toepassing op raamwerkconstructies met het volgende voorbeeld.

::::::{prf:example}
:nonumber: true
:label: sd_raam_0

```{figure-start} ./theorie_data/example.svg
---
align: center
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
number:
---

```

$$EI = 5 \ \rm{MNm^2}, EA >> EI$$

```{figure-end}
```

::::::

1. Bepaal de graad van statische bepaaldheid.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_raam_1

    Voor ons voorbeeld zijn we geïnteresseerd in de verdeling van inwendige krachten, dus moeten we de graad van inwendige statische onbepaaldheid evalueren. Aangezien dit een open constructie is, is de inwendige graad van statische onbepaaldheid gelijk aan de uitwerking graad van statische onbepaaldheid:

    ```{figure} ./theorie_data/graad.svg
    ---
    align: center
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    number:
    ---
    
    ```

    Deze constructie is dus ($5-3$) 2e orde inwendig statisch onbepaald.

    ::::::

2. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij een pendelstaaf, of scharnieren toe te voegen: voeg onbekende statisch onbepaalde krachten en vervormingsvoorwaardes toe voor elke opleggging die je hebt weggenomen en scharnieren die je hebt toegevoegd. Let op dat je de constructie niet transformeert tot een (gedeeltelijk) mechanisme! Kies een statisch bepaald systeem dat makkelijk is uit te rekenen: Kies een statisch bepaald systeem dat makkelijk is uit te rekenen: elementen verplaatsen bij voorkeur niet als ze ook al roteren en je kan vergeet-me-nietjes herkennen in het statisch bepaalde systeem.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_raam_2

    Er zijn veel opties, waarvan een aantal mogelijke opties:

    `````{tab-set}
    :sync-group: raamwerk

    ````{tab-item} Horizontale oplegging bij $\rm{B}$ loslaten en scharnier toevoegen in $\rm{B}$
    :sync: keyraam_1
    ```{figure} ./theorie_data/optie1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ````
    ````{tab-item} Horizontale oplegging bij $\rm{B}$ en $\rm{C}$ loslaten
    :sync: keyraam_2
    ```{figure} ./theorie_data/optie2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```

    ````
    ````{tab-item} Horizontale en verticale oplegging bij $\rm{A}$ loslaten
    :sync: keyraam_3
    ```{figure} ./theorie_data/optie3.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ````
    ````{tab-item} Horizontale oplegging bij $\rm{A}$ loslaten en scharnier toevoegen in $\rm{B}$
    :sync: keyraam_4
    ```{figure} ./theorie_data/optie4.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ````
    `````

    Voor elk van deze opties kunnen we de verplaatsingen schetsen om een variant te kiezen die een simpel verplaatsingspatroon heeft:

    ```````{tab-set}
    :sync-group: raamwerk

    ``````{tab-item} Horizontale oplegging bij $\rm{B}$ loslaten en scharnier toevoegen in $\rm{B}$
    :sync: keyraam_1
    
    :::::{grid}
    :class-container: center-grid

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie_1_verplaatsingen_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ::::

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie_1_verplaatsingen_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ::::

    :::::

    Ligger $\rm{AB}$ wordt niet korter of langer, dus dat deel van de constructie zal niet vervormen. Het overige gedeelte is te bepalen met het vergeet-me-nietje van een ligger op twee steunpunten met een koppel op het uiteinde en een uitkragende ligger met een puntlast op het uiteinde. Enkel het moment in $\rm{C}$ zal moeten worden bepaald om de vervormingen te kunnen berekenen.

    ``````

    ``````{tab-item} Horizontale oplegging bij $\rm{B}$ en $\rm{C}$ loslaten
    :sync: keyraam_2

    :::::{grid}
    :class-container: center-grid

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie_2_verplaatsingen_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ::::

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie_2_verplaatsingen_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ::::

    :::::

    Ligger $\rm{AB}$ wordt niet korter of langer, maar kan nog wel buigen. De vervormingen zijn daarmee te bepalen met het vergeet-me-nietje van een ligger op twee steunpunten met een koppel op het uiteinde, een uitkragende ligger met een puntlast op het uiteinde en een uitkragende ligger met een koppel op het uiteinde. Daarbij moeten de inwendige momenten in $\rm{B}$ en $\rm{C}$ bepaald worden om de vervormingen te kunnen berekenen.


    ``````

    ``````{tab-item} Horizontale en verticale oplegging bij $\rm{A}$ loslaten
    :sync: keyraam_3

    :::::{grid}
    :class-container: center-grid

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie_3_verplaatsingen_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ::::

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie_3_verplaatsingen_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ::::

    :::::

    Ligger $\rm{AB}$ wordt niet korter of langer, maar kan nog wel buigen. De vervormingen zijn daarmee te bepalen met het vergeet-me-nietje van een ligger op twee steunpunten met een koppel op het uiteinde en een uitkragende ligger met een puntlast op het uiteinde. Daarbij moeten de inwendige momenten in $\rm{B}$ en $\rm{C}$ bepaald worden om de vervormingen te kunnen berekenen.
    ``````

    ``````{tab-item} Horizontale oplegging bij $\rm{A}$ loslaten en scharnier toevoegen in $\rm{B}$
    :sync: keyraam_4

    :::::{grid}
    :class-container: center-grid

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie_4_verplaatsingen_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ::::

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie_4_verplaatsingen_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ::::

    :::::

    Ligger $\rm{AB}$ wordt niet korter of langer, dus dat deel van de constructie zal niet vervormen. Het overige gedeelte is te bepalen met het vergeet-me-nietje van een ligger op twee steunpunten met een koppel op het uiteinde en een uitkragende ligger met een puntlast op het uiteinde. Enkel het moment in $\rm{C}$ zal moeten worden bepaald om de vervormingen te kunnen berekenen.
    ``````

    ```````

    Hoewel niet de makkelijkste optie, wordt de derde optie gekozen.

    ::::::

3. Los de verplaatsing op in termen van de onbekende onbepaalde krachten zoals je normaal zou doen voor een statisch bepaalde constructie.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_raam_4

    We hebben de volgende statisch bepaalde constructie gekozen met vormveranderingsvoorwaardes $w_{\rm{A,v}}\left( A_{\rm{v}}, A_{\rm{h}} \right) = 0 $ en $w_{\rm{A,h}}\left( A_{\rm{v}}, A_{\rm{h}} \right) = 0 $:

    ```{figure-start} ./theorie_data/SB-systeem.svg
    ---
    align: center
    number:
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    figclass: sticky-margin
    ---
    
    ```
    $$EI = 5 \ \rm{MNm^2}, EA >> EI$$
    ```{figure-end}
    ```

    De krachtsverdeling kan worden gevonden met evenwicht:

    - $M_{\rm{C}} = 90 \ \rm{kNm}$ (◠/ᑐ)
    - $M_{\rm{B}} = 6A_{\rm{v}}$ (◡/ᑐ)

    Met behulp van de vergeet-mij-nietjes kunnen de rotaties nu worden geëvalueerd:

    - $\varphi_{\rm{B}} = \cfrac{90 \cdot 3}{6 \cdot 5000} + \cfrac{6A_{\rm{v}} \cdot 3}{3 \cdot 5000} = 0.0012 A_{\rm{v}} + 0.009$ (↻)
    - $w_{\rm{A}} = \varphi_{\rm{B}} \cdot 6 + \cfrac{A_{\rm{v}} \cdot 6^3}{3 \cdot 5000}= 0.0216 A_{\rm{v}} + 0.054$

    Voor de horizontale verplaatsing geldt: $w_{\rm{A,h}}  = \cfrac{6A_{\rm{h}}}{EA} $

    ::::::

4. Gebruik je vormveranderingsvoorwaarden om de statisch onbepaalde krachten op te lossen

    ::::::{prf:example}
    :nonumber: true
    :label: sd_raam_5

    $$
    \begin{align*}
    w_{\rm{A,v}}\left( A_{\rm{v}}, A_{\rm{h}} \right) &= 0 \\
    0.0216 A_{\rm{v}} + 0.054 &= 0 \\
    A_{\rm{v}} &= -2.5 \ \rm{kN} \\
    \\
    w_{\rm{A,h}}\left( A_{\rm{v}}, A_{\rm{h}} \right) &= 0 \\
    \cfrac{6A_{\rm{h}}}{EA} &= 0 \\
    A_{\rm{h}} &= 0 \ \rm{kN}
    \end{align*}
    $$

    De vervormingen van de statisch onbepaalde constructie kunnen ook geschetst worden. In dit geval had dat zelfs al van tevoren gekund (zonder exacte waardes) aangezien de richtingen van de verplaatsingen te bepalen zijn zonder berekening:

    ```{figure} ./theorie_data/vervormd.svg
    ---
    align: center
    number:
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ---
    
    ```


    ::::::

## Meer voorbeelden

Het algemene concept van de krachtenmethode wordt behandeld in hoofdstuk 2.1 terwijl de krachtenmethode voor raamwerken wordt behandeld in hoofdstuk 2.2.5 - 2.2.7 en de meer specifieke 'hoekveranderingsvergelijkingen' in hoofdstuk 3.1 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.

Wanneer het boek de 'momentenvlakstelling' noemt in voorbeeld 2.2.6 en 2.2.7, kun je de verplaatsingen ook vinden met behulp van vergeet-mij-nietjes. De methode met verplaatsbare knopen ('hoekveranderingsvergelijkingen met verplaatsbare knopen') die in het verleden werd onderwezen wordt niet meer behandeld.

## Zelfde instructies in collegevorm

Dit onderwerp is [in 2025 in les 7](https://collegerama.tudelft.nl/Mediasite/Channel/public-ceg-ctb2210/watch/2e0fc9db91574fc9adacecd1eb833ce71d?sortBy=most-recent) gepresenteerd in collegevorm van 0:07:50 - 0:31:50. De opname in collegejaar 2026/2027 volgt na het college.

## Extra opgaves in boek

- Opgaves 2.15 - 2.22, 2.24, 2.26 - 2.29, 2.42 - 2.48 in hoofdstuk 2.3 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.
- Opgaves 3.11 - 3.15, 3.22, 3.23, 3.25 - 3.33/1, 3.35, 3.36, 3.45, 3.47-1, 3.47-2, 3.47-4, 3.50, 3.51 in hoofdstuk 3.4 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.

Antwoorden zijn beschikbaar op [deze website voor hoofdstuk 2](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/) en [hier voor hoofdstuk 3](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-3/).
