# Instructie stijfheidsinvloeden

````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze theorie is aangepast van https://github.com/TUDelft-books/CEG-mechanics-BSc versie EN.
```
````

Verschillen in stijfheden zorgen bij statisch bepaalde constructies niet voor een krachtsherverdeling, enkel op de verplaatsingen. Bij statisch onbepaalde constructies zorgen stijfheidsverschillen ook voor verschillen in de krachtsverdeling. Het analyseren van de invloed hiervan kan erg interessant zijn.

Er zijn twee manieren om de stijfheidsinvloeden te analyseren:

1. Los op met een onbekende vermenigvuldigingsfactor $n \cdot EI$ of $n \cdot EA$. Dit geeft een uitdrukking voor krachten/verplaatsingen en maakt het mogelijk een asymptotische grafiek te maken ten opzichte van $n$. Bij deze aanpak dient altijd een statisch bepaalde constructies opgelost te worden met een methode naar keuze.
2. Onderzoek extremen: bekijk beide gevallen van $EI \to 0$ of $EA \to 0$ en $EI \to \infty$ of $EA \to \infty$. Hiermee kun je de uiterste gevallen van krachten en de omhullende van inwendige krachten/verplaatsingen bepalen. Alle werkelijke stijfheidswaarden moeten binnen deze envelop liggen. Bij deze analyse vereenvoudigt een statisch bepaalde constructie soms tot een statisch bepaalde constructie.


We behandelen beide aanpakken op de volgende constructie:

````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Dit voorbeeld is aangepast van https://github.com/TUDelft-books/CT1000 versie CTB2210-2025.
```
```` 

::::::{prf:example}
:nonumber: true
:label: stijfheid_0

```{figure} ./theorie_data/systeem.svg
---
align: center
---
Voorbeeldconstructie
```

::::::

## Vermenigvuldigingsfactor

1. Bepaal de graad van statische bepaaldheid.

    ::::::{prf:example}
    :nonumber: true
    :label: stijfheid_1

    Deze constructie is 1e orde intern statisch onbepaald.

    ::::::

2. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij een pendelstaaf, of scharnieren toe te voegen: voeg onbekende statisch onbepaalde krachten en vervormingsvoorwaardes toe voor elke opleggging die je hebt weggenomen en scharnieren die je hebt toegevoegd. Let op dat je de constructie niet transformeert tot een (gedeeltelijk) mechanisme!

    ::::::{prf:example}
    :nonumber: true
    :label: stijfheid_2

    Er wordt hier gekozen voor hoekveranderingsvergelijkingen. Dat geeft dit statisch bepaalde systeem.

    ```{figure} ./theorie_data/SB_systeem_2.svg
    ---
    align: center
    ---
    Statisch bepaald systeem
    ```

    ::::::

3. Los de verplaatsing op in termen van de onbekende onbepaalde krachten zoals je normaal zou doen voor een statisch bepaalde constructie.

    ::::::{prf:example}
    :nonumber: true
    :label: stijfheid_3

    Met behulp van vergeet-me-nietjes kunnen de rotaties worden gevonden ten gevolge van de momenten en verdeelde belasting.

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
---
align: center
---
$\rm{AB}$ als $nEI \to 0 $
```

Dit geeft direct het moment in $\rm{D}$ met $\cfrac{1}{4}FL = 8 \ \rm{kNm}$ en de volgende momentenlijn:

```{figure} ./theorie_data/M_1.svg
---
align: center
---
Momentenlijn voor $nEI \to 0 $
```

**Geval $nEI \to \infty$**

Voor het tweede geval van $nEI = \infty$ wordt het rechter gedeelte oneindig stijf:

```{figure} ./theorie_data/systeem_inf.svg
---
align: center
---
Statisch onbepaalde ligger voor  $nEI \to \infty$
```

Dit geeft de volgende rotaties voor het statisch bepaalde systeem met vormveranderingsvoorwaarde $\varphi _{\rm{B}}^{{\rm{AB}}} = \varphi _{\rm{B}}^{{\rm{BC}}}$ (zie [de toepassing van hoekveranderingsvergelijkingen met de vermenigvuldigingsfactor](stijfheid_3)):

 - $\varphi _{\rm{B}}^{{\rm{AB}}}  = \cfrac{4 M_{\rm{B}}}{3 EI} + \cfrac{8}{EI}$
 - $\varphi _{\rm{B}}^{{\rm{BC}}}  = 0$

Resulterend in $M_{\rm{B}} = 6 \ \rm{kNm}$ en $M_{\rm{D}} = 5 \ \rm{kNm}$:

```{figure} ./theorie_data/M_2.svg
---
align: center
---
Momentenlijn voor $nEI \to \infty $
```


**Omhullende momentenlijn**

De extreme momenten kunnen gecombineerd worden tot omhullende momentenlijn waarbij alle mogelijk waardes voor het moment voor $n$ in het grijze gedeelte vallen.

```{figure} ./theorie_data/omhullende.svg
---
align: center
---
Omhullende momentenlijn
```

::::::

## Meer voorbeelden

In hoofdstuk 7 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016` worden stijfheidsinvloeden behandeld. De aanpak van hoekveranderingsvergelijkingen met verplaatsbare knopen bij voorbeeld 6.1.3 kan worden vervangen door een van de bekende methodes.