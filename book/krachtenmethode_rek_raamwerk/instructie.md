# Instructie

Tot nu toe hebben we statisch onbepaalde constructies behandeld die ofwel op rek ofwel op buiging worden belast. In deze les behandelen we constructies die zowel op rek als op buiging worden belast. We gebruiken de krachtenmethode om de verplaatsingen en inwendige krachten te berekenen. De aanpak voor deze constructies is niet anders, maar de verplaatsingen kunnen wat complexer zijn. We behandelen de toepassing met het volgende voorbeeld.

::::::{prf:example}
:nonumber: true
:label: ...

% https://oit.tudelft.nl/CTB2210/2025/TOZ/opgave.html

```{figure-start} ./theorie_data/...
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
    :label: ...

    Er zijn veel opties, waarvan een aantal mogelijke opties:

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

