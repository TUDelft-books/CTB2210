````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze instructie is aangepast van de [les van 18 oktober van het vak CT1000S Structural Mechanics 2024/2025](https://oit.tudelft.nl/CT1000/2024/week_7/session_3/intro.html) van {cite:ts}`CT1000_2024`

```
````

# Instructie stijfheidsinvloeden

Verschillen in stijfheden zorgen bij statisch bepaalde constructies niet voor een krachtsherverdeling, enkel op de verplaatsingen. Bij statisch onbepaalde constructies zorgen stijfheidsverschillen ook voor verschillen in de krachtsverdeling. Het analyseren van de invloed hiervan kan erg interessant zijn.

Er zijn twee manieren om de stijfheidsinvloeden te analyseren:

1. Los op met een onbekende vermenigvuldigingsfactor $n \cdot EI$ of $n \cdot EA$. Dit geeft een uitdrukking voor krachten/verplaatsingen en maakt het mogelijk een asymptotische grafiek te maken ten opzichte van $n$. Bij deze aanpak dient altijd een statisch bepaalde constructies opgelost te worden met een methode naar keuze.
2. Onderzoek extremen: bekijk beide gevallen van $EI \to 0$ of $EA \to 0$ en $EI \to \infty$ of $EA \to \infty$. Hiermee kun je de uiterste gevallen van krachten en de omhullende van inwendige krachten/verplaatsingen bepalen. Alle werkelijke stijfheidswaarden moeten binnen deze envelop liggen. Bij deze analyse vereenvoudigt een statisch bepaalde constructie soms tot een statisch bepaalde constructie.

We behandelen beide aanpakken op de volgende constructie: 

::::::{prf:example}
:nonumber: true
:label: stijfheid_0

```{figure} ./theorie_data/systeem.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
:figclass: sticky-margin
```

::::::

## Vermenigvuldigingsfactor

1. Bepaal de graad van statische bepaaldheid.

    ::::::{prf:example}
    :nonumber: true
    :label: stijfheid_1

    ```{figure} ./theorie_data/statisch_onbepaaldheid_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
    ```

    Deze constructie is 1e orde intern statisch onbepaald.

    ::::::

2. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij een pendelstaaf, of scharnieren toe te voegen: voeg onbekende statisch onbepaalde krachten en vervormingsvoorwaardes toe voor elke opleggging die je hebt weggenomen en scharnieren die je hebt toegevoegd. Let op dat je de constructie niet transformeert tot een (gedeeltelijk) mechanisme! Kies een statisch bepaald systeem dat makkelijk is uit te rekenen: elementen verplaatsen bij voorkeur niet als ze ook al roteren en je kan vergeet-me-nietjes herkennen in het statisch bepaalde systeem.

    ::::::{prf:example}
    :nonumber: true
    :label: stijfheid_2

    Er wordt hier gekozen voor hoekveranderingsvergelijkingen. Dat geeft dit statisch bepaalde systeem.

    ```{figure} ./theorie_data/SB_systeem_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
    :figclass: sticky-margin
    ```

    ::::::

3. Los de verplaatsing op in termen van de onbekende onbepaalde krachten zoals je normaal zou doen voor een statisch bepaalde constructie.

    ::::::{prf:example}
    :nonumber: true
    :label: stijfheid_3

    Met behulp van vergeet-me-nietjes kunnen de rotaties worden gevonden ten gevolge van de momenten en verdeelde belasting.

    :::::{grid}
    :class-container: center-grid

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/verplaatsing_5.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
    ```

    ::::

    ::::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/verplaatsing_6.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
    ```
    ::::

    :::::

    - $\varphi _{\rm{B}}^{{\rm{AB}}}  = \cfrac{4 M_{\rm{B}}}{3 EI} + \cfrac{8}{EI}$
    - $\varphi _{\rm{B}}^{{\rm{BC}}}  = \cfrac{-4 M_{\rm{B}}}{3 n EI}$

    ::::::


4. Gebruik je vormveranderingsvoorwaarden om de statisch onbepaalde krachten op te lossen

    ::::::{prf:example}
    :nonumber: true
    :label: stijfheid_4

    $\varphi _{\rm{B}}^{{\rm{AB}}} = \varphi _{\rm{B}}^{{\rm{BC}}}$ geeft $M_{\rm{B}} = -\cfrac{6n}{n+1}$. $M_{\rm{D}}$ is dan $-\cfrac{3n}{n+1}+8$ (◡).

    Voor $n=0$ geeft dit:
    
    - $M_{\rm{B}} = 0 \ \rm{kNm}$
    - $M_{\rm{D}} = 8 \ \rm{kNm}$

    Voor $\mathop {\lim }\limits_{n \to \infty } $ geeft dit:
    
    - $M_{\rm{B}} = -6 \ \rm{kNm}$
    - $M_{\rm{D}} = 5 \ \rm{kNm}$

    Deze resultaten kunnen geplot worden:

    ```{figure} ./theorie_data/steunpuntszetting.svg
    ---
    align: center
    ---
    Verloop momenten voor waardes van n
    ```


    ::::::

## Extremen

::::::{prf:example}
:nonumber: true
:label: stijfheid_5

**Geval $nEI \to 0$**

Voor het eerste geval van $nEI \to 0 $ heeft het rechter gedeelte van de constructie geen stijfheid meer. Je zou het gedeelte $\rm{AB}$ daarom kunnen zijn als een statisch bepaalde ligger op twee steunpunten:

```{figure} ./theorie_data/systeem_0.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
```

Dit geeft direct het moment in $\rm{D}$ met $\cfrac{1}{4}FL = 8 \ \rm{kNm}$ en de volgende momentenlijn:

```{figure} ./theorie_data/M_1.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
```

**Geval $nEI \to \infty$**

Voor het tweede geval van $nEI = \infty$ wordt het rechter gedeelte oneindig stijf:

```{figure} ./theorie_data/systeem_inf.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
```

Dit geeft de volgende rotaties voor het statisch bepaalde systeem met vormveranderingsvoorwaarde $\varphi _{\rm{B}}^{{\rm{AB}}} = \varphi _{\rm{B}}^{{\rm{BC}}}$ (zie [de toepassing van hoekveranderingsvergelijkingen met de vermenigvuldigingsfactor](stijfheid_3)):

 - $\varphi _{\rm{B}}^{{\rm{AB}}}  = \cfrac{4 M_{\rm{B}}}{3 EI} + \cfrac{8}{EI}$
 - $\varphi _{\rm{B}}^{{\rm{BC}}}  = 0$

Resulterend in $M_{\rm{B}} = 6 \ \rm{kNm}$ en $M_{\rm{D}} = 5 \ \rm{kNm}$:

```{figure} ./theorie_data/M_2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
```

::::::

## Omhullende momentenlijn

::::::{prf:example}
:nonumber: true
:label: stijfheid_6

De extreme momenten kunnen gecombineerd worden tot omhullende momentenlijn waarbij alle mogelijk waardes voor het moment voor $n$ in het grijze gedeelte vallen.

```{figure} ./theorie_data/omhullende.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid
```

Dit kan ook gedaan worden voor andere krachts- en verplaatsingsgrootheden.

::::::

## Meer voorbeelden

In hoofdstuk 7 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016` worden stijfheidsinvloeden behandeld. De aanpak van hoekveranderingsvergelijkingen met verplaatsbare knopen bij hoofdstuk 7.1 voorbeeld 2 kan worden vervangen door een van de bekende methodes.

## Zelfde instructies in collegevorm

Dit onderwerp is [in les 8](https://collegerama.tudelft.nl/Mediasite/Channel/public-ceg-ctb2210/watch/035392e16a6948ec88d380408b2de5701d?sortBy=most-recent) gepresenteerd in collegevorm van 0:03:40 tot 0:38:10.
