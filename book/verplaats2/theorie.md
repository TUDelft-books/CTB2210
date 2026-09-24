# Instructie

Een groot nadeel van de krachtenmethode is dat je de statisch onbepaalde constructie moet aanpassen tot een statisch bepaalde constructie. Dat kan soms lastig zijn. Bij de verplaatsingenmethode is dat niet nodig. In plaats van de constructie op te lossen voor een statisch onbepaalde kracht, lossen we de constructie op voor één of meerdere onafhankelijke vrijheidsgraden die de vervorming van de constructie bepalen.

::::::{prf:algorithm} Verplaatsingenmethode
:nonumber: true
:label: verplaatsingenmethode_algoritme_2

1. Kies één of meerdere onafhankelijke vrijheidsgraden die de vervorming van de constructie bepalen en splits de constructie in het deel dat volgens die vrijheidsgraden vervormd en de overige delen. Kies de vrijheidsgraden zo dat:
    - De delen van de gesplitste constructie zo eenvoudig mogelijk zijn om te analyseren, het liefst op basis van vergeet-me-nietjes en verlengingen van staven. Voor de vergeet-me-nietjes kan een uitgebreide set gebruikt worden, inclusief statisch onbepaalde constructies en constructies met steunpuntszettingen.
    - De gekozen vrijheidsgraden samen de vervorming van de hele constructie bepalen.
    - De vrijheidsgraden onafhankelijk zijn: de vervormingen die optreden door een vrijheidsgraad volgen niet ook uit een of meerdere andere vrijheidsgraden.
2. Bereken de krachten in de splitsing in termen van de onbekende vrijheidsgraden. Als je meerdere vrijheidsgraden hebt gedefinieerd, bereken dan de invloed van elke vrijheidsgraad los waarbij de andere vrijheidsgraden aan nul worden gesteld.
3. Gebruik evenwichtsvoorwaarden om de vrijheidsgraden op te lossen.

::::::

De toepassing van deze verplaatsingenmethode op een statisch onbepaalde constructie wordt in een voorbeeld getoond.

::::::{prf:example}
:nonumber: true
:label: verplaats_2_0

```{figure} ./theorie_data/structure.svg
---
align: center
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
number:
figclass: sticky-margin
---

```

::::::

1. Kies één of meerdere onafhankelijke vrijheidsgraden die de vervorming van de constructie bepalen en splits de constructie in het deel dat volgens die vrijheidsgraden vervormd en de overige delen. Kies de vrijheidsgraden zo dat:
    - De delen van de gesplitste constructie zo eenvoudig mogelijk zijn om te analyseren, het liefst op basis van vergeet-me-nietjes en verlengingen van staven. Voor de vergeet-me-nietjes kan een uitgebreide set gebruikt worden, inclusief statisch onbepaalde constructies en constructies met steunpuntszettingen.
    - De gekozen vrijheidsgraden samen de vervorming van de hele constructie bepalen.
    - De vrijheidsgraden onafhankelijk zijn: de vervormingen die optreden door een vrijheidsgraad volgen niet ook uit een of meerdere andere vrijheidsgraden.

    ::::::{prf:example}
    :nonumber: true
    :label: verplaats_2_1

    Als we de vervormingen van de hele constructie schetsen:

    ```{figure} ./theorie_data/schets.svg
    ---
    align: center
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    number:
    ---
    ```

    Zien we dat punt $\rm{B}$ een verplaatsing en rotatie heeft. Met de verplaatsing en rotatie van $\rm{B}$ kan de verplaatsing van de hele constructie worden bepaald. De rotatie van $\rm{C}$ volgt daar dan vanzelf uit.

    We kunnen de vergeet-me-nietjes herkennen in de vervormingen van de afzonderlijke vrijheidsgraden en belasting. De nummering komt overeen met de nummering in het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.

    - De rotatie van $\rm{B}$ geeft de volgende verplaatsing:

        ```{figure} ./theorie_data/verplaats_1.svg
        :align: center
        :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
        :number:
        ```

        Welke kan worden beschreven met:

        :::::{grid}
        :class-container: center-grid

        ::::{grid-item}
        :columns: auto
        
        ```{figure-start} ./theorie_data/verplaats_1_VMN1.svg
        :align: center
        :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
        :number:
        :name: verplaats_1_VMN1
        ```

        Komt overeen met vergeet-me-nietje (7).

        ```{figure-end}
        ```

        ::::

        ::::{grid-item}
        :columns: auto
        
        ```{figure-start} ./theorie_data/verplaats_1_VMN2.svg
        :align: center
        :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
        :number:
        :name: verplaats_1_VMN2
        ```

        Komt overeen met het horizontaal gespiegelde vergeet-me-nietje (4).

        ```{figure-end}
        ```

        ::::
        
        :::::

    - De verplaatsing van $\rm{B}$ geeft de volgende verplaatsing:

        ```{figure} ./theorie_data/verplaats_2.svg
        :align: center
        :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
        :number:
        ```

        Welke kan worden beschreven met:

        :::::{grid}
        :class-container: center-grid

        ::::{grid-item}
        :columns: auto
        
        ```{figure-start} ./theorie_data/verplaats_2_VMN1.svg
        :align: center
        :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
        :number:
        :name: verplaats_2_VMN1
        ```

        Komt overeen met vergeet-me-nietje (g).

        ```{figure-end}
        ```

        ::::

        ::::{grid-item}
        :columns: auto
        
        ```{figure-start} ./theorie_data/verplaats_2_VMN2.svg
        :align: center
        :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
        :number:
        :name: verplaats_2_VMN2
        ```

        Komt overeen met het verticaal gespiegelde vergeet-me-nietje (4) waarbij de inklemming aan de linkerkant is verplaatst in plaats van de roloplegging aan de rechterkant.

        ```{figure-end}
        ```

        ::::
        
        :::::

    - De verplaatsing ten gevolge van de puntlast van $44.8 \ \rm{kN}$ geeft de volgende verplaatsing:

        ```{figure} ./theorie_data/verplaats_3.svg
        :align: center
        :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
        :number:
        ```

        Waarvan de vervorming van $\rm{BC}$ kan worden beschreven met:
        
        :::::{grid}
        :class-container: center-grid

        ::::{grid-item}
        :columns: auto

        ```{figure-start} ./theorie_data/verplaats_3_VMN.svg
        :align: center
        :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
        :number:
        :name: verplaats_3_VMN
        ```

        Komt overeen met vergeet-me-nietje (8).

        ```{figure-end}
        ```

        ::::
        :::::

    We kiezen dus voor de verplaatsing $w_{\rm{B}}$ en de rotatie $\varphi_{\rm{B}}$ van knoop $\rm{B}$ als onafhankelijke vrijheidsgraden en splitsen de constructie in $\rm{B}$. De verplaatsingen van $\rm{B}$ staan vast met de vrijheidsgraden, en de andere delen worden daarvan gesplitst.

    ```{figure} ./theorie_data/splits.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    :number:
    :figclass: sticky-margin
    ```

    ::::::

2. Bereken de krachten in de splitsing in termen van de onbekende vrijheidsgraden. Als je meerdere vrijheidsgraden hebt gedefinieerd, bereken dan de invloed van elke vrijheidsgraad los waarbij de andere vrijheidsgraden aan nul worden gesteld.

    ::::::{prf:example}
    :nonumber: true
    :label: verplaats_2_2

    Per vrijheidsgraad wordt de invloed op de snedekrachten in knoop $\rm{B}$ berekend.

    - Allereerst wordt de invloed van de rotatie $\varphi_{\rm{B}}$ op gedeelte $\rm{AB}$ bekeken. Daarvoor geldt het volgende vergeet-me-nietje:

      :::{fetch} {numref}`verplaats_1_VMN1`
      :::

      Waarvan we het uitwendig moment en de oplegreactie nodig hebben als functie van de rotatie. In onze constructie komt dat overeen met het inwendige moment en de dwarskracht op dat uiteinde:

      ```{figure} ./theorie_data/VMN1_krachten.svg
      :align: center
      :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
      :number:
      ```

      Hieruit volgt:

      - $\varphi = \cfrac{1}{4} \cfrac{M_{\rm{B,1}} \cdot L}{EI} \to M_{\rm{B,1}} = \varphi_{\rm{B}} \cdot \cfrac{4EI}{L} = \varphi_{\rm{B}} \cdot \cfrac{4 \cdot 1500}{3} = 2000 \cdot \varphi_{\rm{B}}$
      - $V_{\rm{B,1}} = \cfrac{3}{2} \cfrac{M_{\rm{B,1}}}{L} = \cfrac{3}{2} \cdot \cfrac{2000 \cdot \varphi_{\rm{B}}}{3} = 1000 \cdot\varphi_{\rm{B}}$

    - Vervolgens wordt de invloed van de verplaatsing $w_{\rm{B}}$ op gedeelte $\rm{AB}$ bekeken. Daarvoor geldt het volgende vergeet-me-nietje:
      
      :::{fetch} {numref}`verplaats_2_VMN1`
      :::

      Waarvan we de beide oplegreacties bij $\rm{B}$ nodig hebben als functie van de verplaatsing. In onze constructie komt dat overeen met het inwendige moment en de dwarskracht op dat uiteinde:

      ```{figure} ./theorie_data/VMN2_krachten.svg
      :align: center
      :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
      :number:
      ```

      Hieruit volgt:

      - $M_{\rm{B,2}} = \cfrac{6 \cdot EI}{L^2} \cdot w_{\rm{B}} = \cfrac{6 \cdot 1500}{3^2} \cdot w_{\rm{B}} = 1000 \cdot w_{\rm{B}}$
      - $V_{\rm{B,2}} = \cfrac{12 \cdot EI}{L^3} \cdot w_{\rm{B}} = \cfrac{12 \cdot 1500}{3^3} \cdot w_{\rm{B}} = \cfrac{2000}{3} \cdot w_{\rm{B}}$

    - Aan de rechterkant beginnen we met de invloed van de rotatie $\varphi_{\rm{B}}$ op gedeelte $\rm{BC}$. Daarvoor geldt het volgende vergeet-me-nietje:
      
      :::{fetch} {numref}`verplaats_1_VMN2`
      :::

      Waarvan we het uitwendig moment en de oplegreactie nodig hebben als functie van de rotatie. In onze constructie komt dat overeen met het inwendige moment en de dwarskracht op dat uiteinde:

      ```{figure} ./theorie_data/VMN3_krachten.svg
      :align: center
      :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
      :number:
      ```

      Hieruit volgt:
      - $\varphi_{\rm{B}} = \cfrac{1}{3} \cfrac{M_{\rm{B,3}} \cdot L}{EI} \to M_{\rm{B,3}} = \varphi_{\rm{B}} \cdot \cfrac{3EI}{L} = \varphi_{\rm{B}} \cdot \cfrac{3 \cdot 3000}{3} = 3000 \cdot \varphi_{\rm{B}}$
      - $ \left. T \right|_{\rm{C}} = 0 \to V_{\rm{B,3}} = \cfrac{M_{\rm{B,3}}}{3} = 1000 \cdot \varphi_{\rm{B}}$

    - Ten derde wordt de invloed van de verplaatsing $w_{\rm{B}}$ op gedeelte $\rm{AB}$ bekeken. Daarvoor geldt het volgende vergeet-me-nietje, leidend tot snedekrachten in de getoonde richting:

      :::{fetch} {numref}`verplaats_2_VMN2`
      :::

      Waarvan we de beide oplegreacties bij $\rm{B}$ nodig hebben als functie van de verplaatsing. In onze constructie komt dat overeen met het inwendige moment en de dwarskracht op dat uiteinde:

      ```{figure} ./theorie_data/VMN4_krachten.svg
      :align: center
      :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
      :number:
      ```

      Hieruit volgt:
      - $M_{\rm{B,4}} = \cfrac{3 \cdot EI}{L^2} \cdot w_{\rm{B}} = \cfrac{3 \cdot 3000}{3^2} \cdot w_{\rm{B}} = 1000 \cdot w_{\rm{B}}$
      - $V_{\rm{B,4}} = \cfrac{3 \cdot EI}{L^3} \cdot w_{\rm{B}} = \cfrac{3 \cdot 3000}{3^3} \cdot w_{\rm{B}} = \cfrac{1000}{3} \cdot w_{\rm{B}}$

    - Tot slot moet ook nog de invloed van de puntlast van $44.8 \ \rm{kN}$ op gedeelte $\rm{BC}$ worden meegenomen:

      :::{fetch} {numref}`verplaats_3_VMN`
      :::

      Waarvan we de beide oplegreacties bij $\rm{B}$ nodig hebben als functie van de verplaatsing. In onze constructie komt dat overeen met het inwendige moment en de dwarskracht op dat uiteinde:

      ```{figure} ./theorie_data/VMN5_krachten.svg
      :align: center
      :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
      :number:
      ```

      Hieruit volgt:
      - $M_{\rm{B,5}} = \cfrac{3}{16} \cdot {F} \cdot L = \cfrac{3}{16} \cdot 44.8 \cdot 3 = 25.2 \ \rm{kNm}$
      - $V_{\rm{B,5}} = \cfrac{11}{16} \cdot {F} = \cfrac{11}{16} \cdot 44.8 = 30.8 \ \rm{kN}$
    ::::::

3. Gebruik evenwichtsvoorwaarden om de vrijheidsgraden op te lossen.

    ::::::{prf:example}
    :nonumber: true
    :label: verplaats_2_3

    Nu alle snedekrachten in $\rm{B}$ bekend zijn, kunnen we de evenwichtsvoorwaarden voor knoop $\rm{B}$ opstellen:

     ```{figure} ./theorie_data/evenwicht_B.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden
    :number:
    ```

    Dit geeft:
    
    $$
    \begin{aligned}
    \Sigma M &= 0 \\
    -M_{\rm{B,1}} - M_{\rm{B,2}} - M_{\rm{B,3}} + M_{\rm{B,4}} - M_{\rm{B,5}} &= 0 \\
    5000 \varphi_{\rm{B}} + 25.2 &= 0 \\
    \varphi_{\rm{B}} &= -0.00504 \ \rm{rad}
    \end{aligned}
    $$

    en:

    $$
    \begin{aligned}
    \Sigma F_{\rm{v}} &= 0 \\
    -V_{\rm{B,1}} - V_{\rm{B,2}} + V_{\rm{B,3}} + V_{\rm{B,4}} - V_{\rm{B,5}} &= 0 \\
    1000 w_{\rm{B}} - 30.8 &= 0 \\
    w_{\rm{B}} &= 0.0308 \ \rm{m} = 30.8 \ \rm{mm}
    \end{aligned}
    $$

    ::::::

## Meer voorbeelden
In hoofdstuk 4.1 en 4.3 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016` wordt deze verplaatsingenmethode behandeld.

## Zelfde instructies in collegevorm

Dit onderwerp is [in 2025 in les 11](https://collegerama.tudelft.nl/Mediasite/Channel/public-ceg-ctb2210/watch/5af52bfa489c4f579dcf83847e8329c71d?sortBy=most-recent) gepresenteerd in collegevorm tot 0:47:56. De opname in collegejaar 2026/2027 volgt na het college.

## Extra opgaves in boek
Opgaves 4.4 - 4.33, 4.35, 4.36 in hoofdstuk 4.5 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Er zijn helaas geen antwoorden beschikbaar. Je kan de constructies doorrekenen met MatrixFrame om je antwoorden te controleren.
