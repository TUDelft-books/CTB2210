# Instructie

...
::::::{prf:algorithm} Matrixmethode
:nonumber: true
:label: matrixmethode_algoritme

1. Bepaal de vrijheidsgraden.
2. Initialiseer het stelsel van vergelijkingen $\mathbf{K} \mathbf{u} = \mathbf{F}$ met nulmatrices.
3. Bepaal voor elk element de elementstijfheidsmatrix $\mathbf{H}$ en voeg deze toe aan de globale stijfheidsmatrix $\mathbf{K}$ op basis van de knopen.
4. Construeer de globale krachtvector $\mathbf{F}$ door de externe krachten toe te voegen op basis van de knopen.
5. Voeg de zowel de voorgeschreven verplaatsingen als de onbekende oplegreacties toe aan het stelsel van vergelijkingen.
6. Los het stelsel van vergelijkingen $\mathbf{K} \mathbf{u} = \mathbf{F}$ op voor de verplaatsingen $\mathbf{u}$.

::::::

De toepassing van deze matrixmethode op een statisch onbepaalde constructie wordt in een voorbeeld getoond.

::::::{prf:example}
:nonumber: true
:label: verplaats_2_0

```{figure} ./theorie_data/structure.svg
---
align: center
---
Voorbeeldconstructie, ...
```

::::::

1. Kies één of meerdere vrijheidsgraden die de vervorming van de constructie bepalen en splits de constructie in of rondom die plek(ken).

    ::::::{prf:example}
    :nonumber: true
    :label: verplaats_2_1

    ```{figure} ./theorie_data/DOF.svg
    ---
    align: center
    ---
    De verplaatsing en rotatie van B wordt gekozen als vrijheidsgraad.
    ```

    Met de verplaatsing en rotatie van B kan de verplaatsing van de hele constructie worden bepaald. 

    ::::::

## Meer voorbeelden
In hoofdstuk 5 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016` wordt de matixmethode behandeld. Hoofdstuk 5.7 wordt niet behandeld.

## Oefeningen
Opgaves 5.1 - 5.5 in hoofdstuk 5.8 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Dit zijn dezelfde opgaves als voor [](../verplaatsingenmethode/lesson.md). Er zijn helaas geen antwoorden beschikbaar. Je kan de constructies doorrekenen met MatrixFrame om je antwoorden te controleren.