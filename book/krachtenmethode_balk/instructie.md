````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze pagina is aangepast van [deze instructie](https://oit.tudelft.nl/CEG-mechanics-BSc/NL/statically_inderminate/force_method/bending.html) van {cite:ts}`CEG_mechanics_BSc`.

```
```` 

(krachtenmethode_balk)=
# Instructie

De krachtenmethode hebben we eerder al behandeld voor onder andere [constructies belast op rek](krachtenmethode_simpel). De methode is niet anders voor constructies op buiging en volgt dus dezelfde vier stappen. Bij balken kunnen we het vervormingsgedrag door rek en buiging ook nog eens afzonderlijk bekijken.

Bij de krachtenmethode 'hoekveranderingsvergelijkingen' wordt er altijd gekozen voor het toevoegen van scharnieren om de constructie statisch bepaald te maken. Dat heeft als voordeel dat het zeer eenvoudig is om de benodigde rotaties te berekenen met behulp van vergeet-mij-nietjes. Echter, voor niet alle constructies zijn vergeet-mij-nietjes beschikbaar en deze aanpak is niet altijd de makkelijkste aanpak.

We tonen de stappen van de krachtenmethode voor een balk.

::::::{prf:example}
:nonumber: true
:label: sd_ben_0

```{figure-start} ./bending_data/Example.svg
---
align: center
figclass: sticky-margin
number:
source: bending_data/constructie.py
---

```

- $EI = \cfrac{16}{3} \ \rm{MNm^2}$
- $EA \gg EI $

```{figure-end}
```

::::::

1. Bepaal de graad van statische bepaaldheid.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ben_1

    Voor ons voorbeeld zijn we geïnteresseerd in de verdeling van inwendige krachten, dus moeten we de graad van inwendige statische onbepaaldheid evalueren. Omdat dit geen gesloten constructie is is de uitwendige graad van statische onbepaaldheid gelijk aan de inwendige graad van statische onbepaaldheid:

    ```{figure} ./bending_data/graad.svg
    ---
    align: center
    source: bending_data/graad.py
    number:
    ---
    
    ```

    Er zijn 4 onbekenden krachten en 3 evenwichtsvergelijkingen. Deze constructie is dus 1e orde inwendig statisch onbepaald.

    ::::::

2. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij een pendelstaaf, of scharnieren toe te voegen: voeg onbekende statisch onbepaalde krachten en vervormingsvoorwaardes toe voor elke opleggging die je hebt weggenomen en scharnieren die je hebt toegevoegd. Let op dat je de constructie niet transformeert tot een (gedeeltelijk) mechanisme!

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ben_2

    Er zijn veel opties, waarvan de meest voor de hand liggende hieronder worden getoond:

    `````{tab-set}
    ````{tab-item} Verticale oplegging bij $\rm{A}$ loslaten
    ```{figure} ./bending_data/optie2.svg
    :align: center
    :number:
    :source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_balk
    ```
    ````
    ````{tab-item} Verticale oplegging bij $\rm{B}$ loslaten
    ```{figure} ./bending_data/optie3.svg
    :align: center
    :number:
    :source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_balk
    ```
    Deze optie is niet erg handig omdat er geen vergeet-mij-nietjes zijn om de verplaatsing bij $\rm{B}$ te verkrijgen voor deze belastingen
    ````
    ````{tab-item} Verticale oplegging bij $\rm{C}$ loslaten
    ```{figure} ./bending_data/optie4.svg
    :align: center
    :number:
    :source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_balk
    ```
    ````
    ````{tab-item} Scharnier toevoegen bij $\rm{B}$
    ```{figure} ./bending_data/optie1.svg
    :align: center
    :number:
    :source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_balk
    ```
    Als alleen scharnieren worden toegevoegd, noemen we deze benadering 'hoekveranderingsvergelijkingen' of 'gaapvergelijkingen'
    ````
    `````

    De laatste optie wordt gekozen.

    ::::::

3. Los de verplaatsing op in termen van de onbekende onbepaalde krachten zoals je normaal zou doen voor een statisch bepaalde constructie.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ben_4

    We hebben de volgende statisch bepaalde constructie gekozen met vormveranderingsvoorwaarde $\varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{B}} \right) = \varphi_{\rm{B}}^{\rm{BC}} \left( M_{\rm{B}} \right) $:

    ```{figure-start} ./bending_data/SB-systeem.svg
    ---
    align: center
    figclass: sticky-margin
    number:
    source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_balk
    ---
    
    ```
    
    - $EI = \cfrac{16}{3} \ \rm{MNm^2}$
    - $EA \gg EI $
    - $\varphi_{\rm{B}}^{\rm{AB}} = \varphi_{\rm{B}}^{\rm{BC}}$

    ```{figure-end}
    ```

    Met behulp van de vergeet-mij-nietjes kunnen de rotaties direct worden geëvalueerd zonder het evalueren van inwendige krachten:

    - $\varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{B}} \right) = \cfrac{4M_{\rm{B}}}{3EI} + \cfrac{200}{3EI}$
    - $\varphi_{\rm{B}}^{\rm{BC}} \left( M_{\rm{B}} \right) = -\cfrac{2M_{\rm{B}}}{EI}$

    ::::::

4. Gebruik je vormveranderingsvoorwaarden om de statisch onbepaalde krachten op te lossen

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ben_5

    $$
    \begin{align*}
    \varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{B}} \right) &= \varphi_{\rm{B}}^{\rm{BC}} \left( M_{\rm{B}} \right) \\
    \cfrac{4M_{\rm{B}}}{3EI} + \cfrac{200}{3EI} &= -\cfrac{2M_{\rm{B}}}{EI} \\
    M_{\rm{B}} &= -20 \ \rm{kNm}
    \end{align*}
    $$
    ::::::

## Meer voorbeelden
Het algemene concept van de krachtenmethode wordt behandeld in hoofdstuk 2.1 terwijl de krachtenmethode voor balken wordt behandeld in hoofdstuk 2.2.1 - 2.2.4 en de meer specifieke 'hoekveranderingsvergelijkingen' in hoofdstuk 3.1 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. De voorbeelden van hoofdstuk 3.1 worden behandeld in [de volgende les](krachtenmethode_raamwerk).

## Instructies in collegevorm

Dit onderwerp is [in 2025 in les 6](https://collegerama.tudelft.nl/Mediasite/Channel/public-ceg-ctb2210/watch/c40ac091651a4143a10fe729246403c31d?sortBy=most-recent) gepresenteerd in collegevorm van 0:04:20 tot 0:30:00. De opname in collegejaar 2026/2027 volgt na het college.

## Opdrachten

- Opgaves 2.1 - 2.14, 2.23, 2.25 en 2.30 in hoofdstuk 2.3 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.
- Opgaves 3.1 - 3.10, 3.16 - 3.21 in hoofdstuk 3.4 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.

Antwoorden zijn beschikbaar op [deze website voor hoofdstuk 2](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/) en [hier voor hoofdstuk 3](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-3/).
