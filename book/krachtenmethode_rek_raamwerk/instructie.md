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

-$EI = 64 \ \rm{MNm^2}$
-$EA = 4 \ \rm{MN}$

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
    ```{figure} ./instructie_data/optie1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```
    ````
    ````{tab-item} Staaf $\rm{BD}$ splitsen
    :sync: keyraamrek_2
    ```{figure} ./instructie_data/optie2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
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
    ```{figure} ./instructie_data/optie4.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    ````
    ````{tab-item} Scharnier toevoegen tussen $\rm{D}$ en $\rm{E}$
    ```{figure} ./instructie_data/optie5.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    Deze constructie is een mechanisme dus geen geschikte statisch bepaalde constructie.
    ````
    ````{tab-item} Scharnier toevoegen tussen $\rm{E}$ en $\rm{G}$
    ```{figure} ./instructie_data/optie6.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    Deze constructie is een mechanisme dus geen geschikte statisch bepaalde constructie.
    ````
    ````{tab-item} Scharnieroplegging bij $\rm{C}$ vervangen door een verticaal rolscharnier 
    ```{figure} ./instructie_data/optie7.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode_raamwerk_2
    ```
    Deze constructie is een mechanisme dus geen geschikte statisch bepaalde constructie.
    ````
    `````

    Voor elk van de opties die geen mechanisme zijn kunnen we de verplaatsingen schetsen om een variant te kiezen die een simpel verplaatsingspatroon heeft:

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

