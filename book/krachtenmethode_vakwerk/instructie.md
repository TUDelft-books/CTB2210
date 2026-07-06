````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze instructie is aangepast van de [pagina over de krachtenmethode voor vakwerkconstructies](https://oit.tudelft.nl/CEG-mechanics-BSc/NL/statically_inderminate/force_method/extension.html) van {cite:ts}`CEG_mechanics_BSc`

```
````

# Instructie

De krachtenmethode hebben we eerder al behandeld voor [simpele constructies](krachtenmethode_simpel). We behandelen de toepassing op complexere vakwerkconstructies met het volgende voorbeeld. Dit voorbeeld bevat een Williot diagram om de verplaatsingen te berekenen.

::::::{prf:example}
:nonumber: true
:label: sd_ext_0

```{figure-start} ./extension_data/Example.svg
---
align: center
number:
figclass: sticky-margin
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_williot
---
```

- $EI \gg EA_{\rm{CD}}, EA_{\rm{BE}}$
- $EA_{\rm{ADE}} \gg EA_{\rm{CD}}, EA_{\rm{BE}}$

```{figure-end}
```

::::::

1. Bepaal de graad van statische bepaaldheid.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ext_1

    Voor ons voorbeeld zijn we geïnteresseerd in de interne krachtenverdeling, dus moeten we de graad van interne statische onbepaaldheid evalueren. Omdat dit een open constructie is, is er geen verschil tussen interne en externe statische onbepaaldheid:

    ```{figure} ./extension_data/uitwerking4.svg
    ---
    align: center
    number:
    source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_williot
    ---

    ```

    Er zijn 10 onbekende krachten en 9 evenwichtsvergelijkingen, dus is deze constructie 1e orde statisch onbepaald.
    ::::::

2. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij pendelstaven of scharnieren toe te voegen: voeg onbekende statisch onbepaalde krachten en vervormingsvoorwaarden toe voor elke oplegging die je hebt weggenomen, aansluiting van de pendelstaven die je hebt weggenomen en scharnieren die je hebt toegevoegd. Let op dat je de constructie niet transformeert tot een (gedeeltelijk) mechanisme!

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ext_2

    Er zijn hier veel opties, waarvan er enkele hieronder worden getoond:

    `````{tab-set}
    ````{tab-item} Splits de constructie bij een scharnier
    ```{figure} ./extension_data/option1.svg
    :align: center
    :source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_williot
    :number:
    ```
    ````
    ````{tab-item} Scharnier toevoegen
    ```{figure} ./extension_data/option2.svg
    :align: center
    :source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_williot
    :number:
    ```
    ````
    ````{tab-item} De horizontale bewegingsrichting van een oplegging vrijmaken
    ```{figure} ./extension_data/option3.svg
    :align: center
    :source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_williot
    :number:
    ```
    ````
    ````{tab-item} Verticale oplegging weghalen
    ```{figure} ./extension_data/option4.svg
    :align: center
    :source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_williot
    :number:
    ```
    ````
    `````


    De laatste optie wordt gekozen.

    ::::::

3. Los de verplaatsing op in termen van de onbekende onbepaalde krachten zoals je normaal zou doen voor een statisch bepaalde constructie.

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ext_4

    We hebben de volgende statisch bepaalde constructie gekozen met vervormingsvoorwaarde $w_{\rm{B}}\left( B_{\rm{v}} \right) = 0$:

    ```{hide-sticky-margin}
    ```
    ```{figure-start} ./extension_data/SD-struc.svg
    ---
    align: center
    number:
    figclass: sticky-margin
    source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_williot
    ---
    
    ```

    - $EI \gg EA_{\rm{CD}}, EA_{\rm{BE}}$
    - $EA_{\rm{ADE}} \gg EA_{\rm{CD}}, EA_{\rm{BE}}$

    ```{figure-end}
    ```

    Omdat $\rm{AE}$ oneindig stijf is, zullen alle vervormingen het gevolg zijn van staven die uitrekken/samendrukken. Om dit te berekenen, kunnen eerst de normaalkrachten worden geëvalueerd als functie van $B_{\rm{v}}$ met behulp van bijvoorbeeld een momentenevenwicht rond $\rm{A}$ voor het element $\rm{ADE}$:

    - $N_{\rm{CD}}\left( B_{\rm{v}} \right) = 210 - 2.5 B_{\rm{v}}$
    - $N_{\rm{BE}} \left( B_{\rm{v}} \right) = - B_{\rm{v}}$

    Dit leidt tot de volgende uitrekking van de elementen, met behulp van $\Delta L = \cfrac{N \ L}{EA}$:

    - $\Delta L_{\rm{CD}}\left( B_{\rm{v}} \right) = \cfrac{1400}{EA} - \cfrac{50 B_{\rm{v}}}{3 EA}$
    - $\Delta L_{\rm{BE}}\left( B_{\rm{v}} \right) = -\cfrac{5 B_{\rm{v}}}{EA}$

    Dit leidt tot de volgende verplaatsing, met behulp van een Williot diagram:

    ```{figure} ./extension_data/williot.svg
    ---
    align: center
    source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_williot
    number:
    ---
    
    ```

    Dit geeft een verplaatsing van $\rm{D}$ van $\cfrac{5}{4} \Delta L_{\rm{CD}} $

    - $w_{\rm{D}}\left( B_{\rm{v}} \right) = \cfrac{1750}{EA} - \cfrac{125 B_{\rm{v}}}{6 EA} \left( \downarrow \right) $
    - $w_{\rm{E}}\left( B_{\rm{v}} \right) = \cfrac{3500}{EA} - \cfrac{125 B_{\rm{v}}}{3 EA} \left( \downarrow \right) $
    - $w_{\rm{B}}\left( B_{\rm{v}} \right) = \cfrac{3500}{EA} - \cfrac{140 B_{\rm{v}}}{3 EA} \left( \downarrow \right) $

    ::::::

4. Gebruik je vormveranderingsvoorwaarden om de statisch onbepaalde krachten op te lossen

    ::::::{prf:example}
    :nonumber: true
    :label: sd_ext_5

    $$
    \begin{align*}
    w_{\rm{B}}\left( B_{\rm{v}} \right) &= 0 \\
    \cfrac{3500}{EA} - \cfrac{140 B_{\rm{v}}}{3 EA} &= 0 \\
    B_{\rm{v}} &= 75 \ \rm{kN}
    \end{align*}
    $$

    Dit leidt tot de volgende andere resultaten:

    - $N_{\rm{CD}} = 22.5 \ \rm{kN}$
    - $N_{\rm{BE}} -75 \ \rm{kN} $
    - $w_{\rm{D}} = \cfrac{375000}{2 \cdot EA \, \left( \rm{in} \, \rm{N} \right)} \, \rm{mm} \, \left( \downarrow \right) $
    - $w_{\rm{E}} = \cfrac{375000}{EA \, \left( \rm{in} \, \rm{N} \right)} \, \rm{mm} \,  \left( \downarrow \right) $

    ```{figure} ./extension_data/verplaatsingen.svg
    :align: center
    :source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_williot
    :number:
    ```

    ::::::

## Meer voorbeelden

In hoofdstuk 2.1 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016` wordt de krachtenmethode in het algemeen behandeld. Specifiek voor vakwerkconstructies waarbij ook williot nodig is wordt behandeld in hoofdstuk 2.2.10.

## Instructies in collegevorm

Dit onderwerp is in [2025 in les 5](https://collegerama.tudelft.nl/Mediasite/Channel/public-ceg-ctb2210/watch/99cfa289d58d4986a4378be10efb40c31d?sortBy=most-recent) gepresenteerd in collegevorm tot 0:42:50. De opname in collegejaar 2026/2027 volgt na het college.

## Oefeningen
- Opgaves 2.40 en 2.41, in hoofdstuk 2.3 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.
Antwoorden zijn [hier beschikbaar](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/).