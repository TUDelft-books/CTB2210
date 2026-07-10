(krachtenmethode_simpel)=
# Instructie

De krachtenmethode is een aanpak om statisch onbepaalde constructies door te rekenen. In deze methode wordt de constructie aangepast naar een statisch bepaalde constructie met vormveranderingsvoorwaarden. Vervolgens kan je de constructie oplossen zoals je gewend bent van statisch bepaalde constructies. De krachtenmethode bestaat altijd uit de volgende stappen:

::::::{prf:algorithm} Krachtenmethode
:nonumber: true
:label: krachtenmethode_algoritme

1. Bepaal de graad van statische bepaaldheid.
2. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij pendelstaven of scharnieren toe te voegen: voeg onbekende statisch onbepaalde krachten en vervormingsvoorwaarden toe voor elke oplegging die je hebt weggenomen, aansluiting van de pendelstaven die je hebt weggenomen en scharnieren die je hebt toegevoegd. Let op dat je de constructie niet transformeert tot een (gedeeltelijk) mechanisme! Kies een statisch bepaald systeem dat makkelijk is uit te rekenen: elementen roteren bij voorkeur om een vast punt.

    `````{tab-set}
    ````{tab-item} Weghalen oplegging
    ```{figure} theorie_data/1.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```
    ````
    ````{tab-item} Splitsen constructie bij pendelstaven
    ```{figure} theorie_data/2.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```
    ````
    ````{tab-item} Toevoegen scharnieren
    ```{figure} theorie_data/3.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```
    ````
    `````
    
    Er zijn meestal meerdere mogelijkheden om dit te doen, kies de optie die het makkelijkst is uit te rekenen. Teken daarvoor  de vervormde constructie ten gevolge van individuele krachten (inclusief de statisch onbepaalde kracht):
    
    - Een makkelijk model is een model waarbij knopen zoveel mogelijk op z'n plek blijven bij vervorming; waarbij er zo min mogelijk starre verplaatsingen en rotaties optreden.
    - Een makkelijk model is een model waarbij de verplaatsingen worden beschreven met starre verplaatsingen en rotaties, vergeet-me-nietjes en/of verlengingen van staven.

3. Los de verplaatsing op in termen van de onbekende onbepaalde krachten zoals je normaal zou doen voor een statisch bepaalde constructie.
4. Gebruik je vervormingsvoorwaarden om de statisch onbepaalde krachten op te lossen.

::::::

We behandelen de toepassing op constructies die enkel op rek worden beoordeeld met het volgende voorbeeld.

::::::{prf:example}
:nonumber: true
:label: sd_extsimpel_0

```{figure-start} ./theorie_data/constructie.svg
---
align: center
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
number:
---

```

- $EA = 2.5 \ \rm{MN}$
- $EI \gg EA$

```{figure-end}
```

::::::

1. Bepaal de graad van statische bepaaldheid.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_extsimpel_1

    Voor ons voorbeeld zijn we geïnteresseerd in de interne krachtenverdeling, dus moeten we de graad van interne statische onbepaaldheid evalueren. Echter is deze constructie open, dus is er geen verschil tussen interne en externe statische onbepaaldheid:

    ```{figure} ./theorie_data/statisch_onbepaaldheid.svg
    ---
    align: center
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    number:
    ---
    
    ```

    Er zijn 4 onbekende krachten en 3 evenwichtsvergelijkingen

    Deze constructie is dus 1e orde intern statisch onbepaald.

    ::::::

2. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij een pendelstaaf, of scharnieren toe te voegen: voeg onbekende statisch onbepaalde krachten en vervormingsvoorwaardes toe voor elke opleggging die je hebt weggenomen en scharnieren die je hebt toegevoegd. Let op dat je de constructie niet transformeert tot een (gedeeltelijk) mechanisme! Kies een statisch bepaald systeem dat makkelijk is uit te rekenen: elementen roteren bij voorkeur om een vast punt.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_extsimpel_2

    Er zijn hier enkele opties, waarvan er enkele hieronder worden getoond:

    ::::{grid} 3
    :class-container: center-grid

    :::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie1.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    :::

    :::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie2.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    :::

    :::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie3.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    :::

    ::::

    De mogelijke vervormingen van elke constructie kunnen geschetst worden.
    
    ::::{grid} 3
    :class-container: center-grid

    :::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/verpl_2.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    :::

    :::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie2_verpl.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    :::

    :::{grid-item}
    :columns: auto

    ```{figure} ./theorie_data/optie3_verpl.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    :::

    ::::

    Geen van de opties vormt een mechanica en alle drie de opties zijn uit te rekenen met de verlenging van staven. De eerste optie wordt gekozen.

    ::::::

3. Los de verplaatsing op in termen van de onbekende onbepaalde krachten zoals je normaal zou doen voor een statisch bepaalde constructie.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_extsimpel_4

    We hebben de volgende statisch bepaalde constructie gekozen met vervormingsvoorwaarde $w_{\rm{B}}\left( B_{\rm{v}} \right) = 0$:

    ```{figure-start} ./theorie_data/SB-systeem.svg
    ---
    align: center
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    number:
    ---

    ```

    - $EA = 2.5 \ \rm{MN}$
    - $EI \gg EA$

    ```{figure-end}
    ```

    Zonder een berekening te maken kunnen we voor de afzonderlijke krachten de verplaatsingen schetsen:

    ::::{grid} 2
    :class-container: center-grid

    :::{grid-item}

    De verdeelde belasting zorgt voor verlenging van de statisch bepaalde constructie:

    ```{figure} ./theorie_data/verpl_1.svg
    :align: center
    :source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    :::

    :::{grid-item}

    De statisch onbepaalde kracht zorgt voor verkorting van de statisch bepaalde constructie, zoals eerder ook al getekend:

    ```{figure} ./theorie_data/verpl_2.svg
    :align: center
    :source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    :::

    ::::

    Om de verplaatsing van $\rm{B}$ te vinden, kunnen eerst de normaalkrachten worden geëvalueerd als functie van $B_{\rm{v}}$ met behulp van verticaal krachtenevenwicht:

    - $N_{\rm{AC}}\left( B_{\rm{v}} \right) = - B_{\rm{v}} + 6 - 3 \cdot x $
    - $N_{\rm{BC}} \left( B_{\rm{v}} \right) = - B_{\rm{v}}$

    Dit leidt tot de volgende uitrekking van de elementen, met behulp van $\Delta L = \cfrac{N \ L}{EA}$ en de algemere $\Delta L = \int\limits_L {\cfrac{N\left(x\right)}{EA} dx}$:
    - $\Delta L_{\rm{AC}}\left( B_{\rm{v}} \right) = - \cfrac{B_{\rm{v}} \cdot 2}{2500} + \cfrac{6 \cdot 2}{2500} - \int\limits_0^2 {\cfrac{ 3 \cdot x}{2500}dx} = - \cfrac{B_{\rm{v}}}{1250} + \cfrac{3}{1250} $
    - $\Delta L_{\rm{BC}}\left( B_{\rm{v}} \right) = -\cfrac{B_{\rm{v}}}{1250}$

    Dit leidt tot een verplaatsing van:

    - $w_{\rm{C}}\left( B_{\rm{v}} \right) = \cfrac{B_{\rm{v}}}{1250} - \cfrac{3}{1250}  $
    - $w_{\rm{B}}\left( B_{\rm{v}} \right) = \cfrac{B_{\rm{v}}}{625} - \cfrac{3}{1250} $

    ::::::

4. Gebruik je vormveranderingsvoorwaarden om de statisch onbepaalde krachten op te lossen

    ::::::{prf:example}
    :nonumber: true
    :label: sd_extsimpel_5

    $$
    \begin{align*}
    w_{\rm{B}}\left( B_{\rm{v}} \right) &= 0 \\
    \cfrac{B_{\rm{v}}}{625} - \cfrac{3}{1250} &= 0 \\
    B_{\rm{v}} &= 1.5 \ \rm{kN}
    \end{align*}
    $$

    Dit leidt tot de volgende andere resultaten:

    ```{figure} ./theorie_data/Nlijn.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```

    $w_{\rm{C}} = 1.2 \ \rm{mm} \left( \downarrow \right) $

    Dit geeft de volgende vervormde constructie (op schaal):
    
    ```{figure} ./theorie_data/vervormde_constructie.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_rek
    :number:
    ```
    
    ::::::

## Meer voorbeelden

In hoofdstuk 2.1 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016` wordt de krachtemethode in het algemeen behandeld. Specifiek voor simpele vakwerkconstructies wordt behandeld in hoofdstuk 2.2.8 - 2.2.9.

## Instructies in collegevorm

Dit onderwerp is [in 2025 in les 4](https://collegerama.tudelft.nl/Mediasite/Channel/public-ceg-ctb2210/watch/b59d1e6849ba4f92957d462f07f7e37f1d?sortBy=most-recent) gepresenteerd in collegevorm van 0:11:30 tot 0:43:10. De opname in collegejaar 2026/2027 volgt na het college.

## Oefeningen
- Opgaves 2.31 - 2.39, in hoofdstuk 2.3 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.

Antwoorden zijn [hier beschikbaar](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/).