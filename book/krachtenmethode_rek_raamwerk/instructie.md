# Instructie

Tot nu toe hebben we statisch onbepaalde constructies behandeld die ofwel op rek ofwel op buiging worden belast. In deze les behandelen we constructies die zowel op rek als op buiging worden belast. We gebruiken de krachtenmethode om de verplaatsingen en inwendige krachten te berekenen. De aanpak voor deze constructies is niet anders, maar de verplaatsingen kunnen wat complexer zijn. We behandelen de toepassing met het volgende voorbeeld.

::::::{prf:example}
:nonumber: true
:label: rek_raam_0

% https://oit.tudelft.nl/CTB2210/2025/TOZ/opgave.html

```{figure-start} ./instructie_data/constructie.svg
---
align: center
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode
number:
---

```

- $EI = 64 \ \rm{MNm^2}$
- $EA = 4 \ \rm{MN}$

```{figure-end}
```

::::::

1. Bepaal de graad van statische bepaaldheid.

    ::::::{prf:example}
    :nonumber: true
    :label: rek_raam_1

    ```{figure} instructie_data/SB1.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode
    :number:
    ```

    Er zijn 7 onbekende oplegreacties en 6 onbekende verbindingskrachten. Dat geeft een uitwendige graad van statisch onbepaaldheid van 1. Omdat deze constructie niet gesloten is, is de inwendige graad van statisch onbepaaldheid ook gelijk aan 1.

    ::::::

2. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij een pendelstaaf, of scharnieren toe te voegen: voeg onbekende statisch onbepaalde krachten en vervormingsvoorwaardes toe voor elke opleggging die je hebt weggenomen en scharnieren die je hebt toegevoegd. Let op dat je de constructie niet transformeert tot een (gedeeltelijk) mechanisme! Kies een statisch bepaald systeem dat makkelijk is uit te rekenen: Kies een statisch bepaald systeem dat makkelijk is uit te rekenen: elementen verplaatsen bij voorkeur niet als ze ook al roteren en je kan vergeet-me-nietjes herkennen in het statisch bepaalde systeem.

    ::::::{prf:example}
    :nonumber: true
    :label: ...

    Er zijn veel opties, waarvan een aantal mogelijke opties:

    `````{tab-set}
    :sync-group: raamwerk

    ````{tab-item} De inklemming bij $\rm{A}$ vervangen door een scharnier
    :sync: keyraamrek_1
    ```{figure-start} ./instructie_data/optie1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    $ \varphi_{\rm{A}} = 0 $

    ```{figure-end}
    ```
    ````
    ````{tab-item} Staaf $\rm{BD}$ splitsen
    :sync: keyraamrek_2
    ```{figure-start} ./instructie_data/optie2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    $ w_{\rm{D}}^{\rm{BD}} = w_{\rm{D}}^{\rm{BD}}$

    ```{figure-end}
    ```

    ````
    ````{tab-item} Staaf $\rm{CG}$ splitsen
    ```{figure} ./instructie_data/optie3.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```
    Deze constructie is een mechanisme dus geen geschikte statisch bepaalde constructie.
    ````
    ````{tab-item} Scharnier toevoegen tussen $\rm{A}$ en $\rm{D}$
    :sync: keyraamrek_4
    ```{figure-start} ./instructie_data/optie4.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    $\varphi_{\rm{S}}^{\rm{AS}} = \varphi_{\rm{S}}^{\rm{SD}}$

    ```{figure-end}
    ```
    ````
    ````{tab-item} Scharnier toevoegen tussen $\rm{D}$ en $\rm{E}$
    ```{figure} ./instructie_data/optie5.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```
    Deze constructie is een mechanisme dus geen geschikte statisch bepaalde constructie.
    ````
    ````{tab-item} Scharnier toevoegen tussen $\rm{E}$ en $\rm{G}$
    ```{figure} ./instructie_data/optie6.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```
    Deze constructie is een mechanisme dus geen geschikte statisch bepaalde constructie.
    ````
    ````{tab-item} Scharnieroplegging bij $\rm{C}$ vervangen door een verticaal rolscharnier 
    ```{figure} ./instructie_data/optie7.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```
    Deze constructie is een mechanisme dus geen geschikte statisch bepaalde constructie.
    ````
    `````

    Voor elk van de opties die geen mechanisme zijn kunnen we de verplaatsingen schetsen door zowel de statisch onbepaalde kracht en de al aanwezige belasting om een variant te kiezen die een simpel verplaatsingspatroon heeft:

    ```````{tab-set}
    :sync-group: raamwerk

    ``````{tab-item} De inklemming bij $\rm{A}$ vervangen door een scharnier
    :sync: keyraamrek_1

    ```{figure} ./instructie_data/optie1_verplaatsingen_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    Dit is een redelijk goed te doen verplaatsingspatroon, waarbij het rechter gedeelte alleen star roteert en geen invloed heeft op de rotatie van $\rm{A}$. De linker ligger kan worden behandeld met het vergeet-me-nietje van een ligger op twee steunpunten met een puntlast in het midden en een koppel op het uiteinde, die ook nog om een vast punt een starre rotatie ondergaat.

    ```{figure} ./instructie_data/optie1_verplaatsingen_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    In dit geval zijn de verplaatsingen van het rechter gedeelte wederom niet van invloed op de verplaatsingen van het linker gedeelte. $\rm{AE}$ kan gemodelleerd worden als een ligger op twee steunpunten met een puntlast in het midden die ook nog om een vast punt een starre rotatie ondergaat. Niet het makkelijkste verplaatsingspatroon, maar wel goed te doen.   

    ``````

    ``````{tab-item} Staaf $\rm{BD}$ splitsen
    :sync: keyraamrek_2

    :::::{grid}
    :class-container: center-grid

    ::::{grid-item}
    :columns: auto

    ```{figure} ./instructie_data/optie2_verplaatsingen_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    Dit is een goed te doen verplaatsingspatroon. $\rm{BD}$ verlengt alleen maar en $\rm{AD}$ kan worden behandeld als een uitkragende ligger met een kracht op het uiteinde. Het rechter gedeelte roteert alleen star en heeft geen invloed heeft op de zakking van $\rm{D}$.
    ::::

    ::::{grid-item}
    :columns: auto

    ```{figure} ./instructie_data/optie2_verplaatsingen_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```
    ::::

    :::::

    Ligger $\rm{AB}$ wordt niet korter of langer, maar kan nog wel buigen. De vervormingen zijn daarmee te bepalen met het vergeet-me-nietje van een ligger op twee steunpunten met een koppel op het uiteinde, een uitkragende ligger met een puntlast op het uiteinde en een uitkragende ligger met een koppel op het uiteinde. Daarbij moeten de inwendige momenten in $\rm{B}$ en $\rm{C}$ bepaald worden om de vervormingen te kunnen berekenen.


    ``````

    ``````{tab-item} Scharnier toevoegen tussen $\rm{A}$ en $\rm{D}$
    :sync: keyraamrek_4

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

    ```````

    ::::::

3. Los de verplaatsing op in termen van de onbekende onbepaalde krachten zoals je normaal zou doen voor een statisch bepaalde constructie.

    ::::::{prf:example}
    :nonumber: true
    :label: ...

    ::::::

4. Gebruik je vormveranderingsvoorwaarden om de statisch onbepaalde krachten op te lossen

    ::::::{prf:example}
    :nonumber: true
    :label: ...

    ::::::

## Meer voorbeelden

...

## Zelfde instructies in collegevorm

De opname volgt na het college.

## Extra opgaves in boek

- ...

