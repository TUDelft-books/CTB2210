# Instructie

Een constructie is statisch onbepaald wanneer deze niet meer enkel met evenwichtsvergelijkingen kan worden opgelost. Er kan hierbij onderscheid worden gemaakt tussen:

- Enkel oplegreacties kunnen worden bepaald (uitwendig statisch bepaald)
- Inwendige krachten kunnen worden bepaald (inwendig statisch bepaald)

De inwendige statisch bepaaldheid is meer werk om te berekenen. Als de constructie open is, dat wil zeggen dat er geen gesloten 'lussen' in de constructie zitten, is de inwendige statisch bepaaldheid gelijk aan de uitwendige statisch bepaaldheid. Je kan dan 

```{figure} ./determinancy_data/gesloten_vs_open.svg
---
name: gesloten_vs_open
align: center
number:
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
---

```

Als evenwichtsvergelijkingen niet genoeg zijn is een constructie statisch onbepaald. De mate van statisch onbepaaldheid wordt uitgedrukt in de graad van statisch onbepaaldheid.

Het is nodig de graad van statisch onbepaaldheid te bepalen om deze constructies met behulp van de krachtenmethode op te kunnen lossen.

Deze twee categorieën worden samen behandeld in hoofdstuk 4.5.2 en 4.5.3 van het boek *Mechanica: Evenwicht* {cite:p}`Hartsuijker1999`. Voor vakwerken is de analyse versimpeld zoals beschreven in hoofdstuk 9.2.2 van het boek *Mechanica: Evenwicht* {cite:p}`Hartsuijker1999`. Alhoewel de getoonde vergelijkingen met $r$, $v$ en $e$ simpel zijn, zijn ze niet volledig correct en leiden ze niet altijd tot de goede resultaten. Een aanpak die altijd werkt is hieronder getoond voor afzonderlijk uitwendig en inwendig statisch onbepaaldheid.

## Bepalen graad van uitwendig statisch onbepaaldheid

Voor de berekening van uitwendig statisch onbepaaldheid gelden de volgende stappen:

::::::{prf:algorithm} Graad van uitwendig statisch onbepaaldheid
:nonumber: true
:label: graad_uitwendig_stat_onbepaaldheid

1. Splits de constructie in alle vormvaste delen die ten opzichte van elkaar kunnen roteren als je de opleggingen zou weghalen. Teken het vrijlichaamsschema van deze scharnierende delen.
2. Tel het aantal onbekende krachten: de oplegreacties en verbindingskrachten in de scharnieren (de even grote maar tegengestelde reactiekrachten tellen niet apart mee)
3. Tel het evenwichtsvergelijkingen: 3 evenwichtsvergelijkingen per vormvaste deel van de constructie
4. De graad van statisch onbepaaldheid is het aantal oplegreacties + verbindingskrachten - aantal evenwichtsvergelijkingen

::::::

Als voorbeeld bepalen we de uitwendige statisch onbepaaldheid van onderstaande constructie.

::::::{prf:example}
:nonumber: true

```{figure} ./determinancy_data/Example.svg
---
name: example_sd
align: center
number:
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
figclass: sticky-margin
---

```

::::::

1. Splits de constructie in alle vormvaste delen die ten opzichte van elkaar kunnen roteren als je de opleggingen zou weghalen. Teken het vrijlichaamsschema van deze scharnierende delen.

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_1.svg
   ---
   name: example_sd_1
   align: center
   number:
   source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
   ---

   ```

   De constructie is onder te verdelen in twee vormvaste, scharnierend verbonden delen. De opleggingen zijn vervangen door oplegreacties en de scharnierende verbinding door een horizontale en verticale kracht (en reactiekrachten). De uitwendige kracht kan getekend worden, maar heeft geen invloed op de verdere berekeningen en werkt slechts op een van de twee delen.

   ::::::

2. Tel het aantal onbekende krachten: de oplegreacties en verbindingskrachten in de scharnieren (de even grote maar tegengestelde reactiekrachten tellen niet apart mee)

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_2.svg
   ---
   name: example_sd_2
   align: center
   number:
   source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
   ---
   
   ```

   Er zijn in totaal 6 oplegreacties en 2 verbindingskrachten. Let op: de verbindingskrachten zijn twee keer getoond, maar deze krachten zijn aan beide uiteinden van de verbinding gelijk, dus ze kunnen als één worden geteld.
   ::::::

3. Tel het evenwichtsvergelijkingen: 3 evenwichtsvergelijkingen per vormvaste deel van de constructie

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_3.svg
   ---
   name: example_sd_3
   align: center
   number:
   source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
   ---
   
   ```

   Er zijn twee vormvaste delen, dus 6 evenwichtsvergelijkingen

   ::::::

4. De graad van statisch onbepaaldheid is het aantal oplegreacties + verbindingskrachten - aantal evenwichtsvergelijkingen

   ::::::{prf:example}
   :nonumber: true

   De graad van uitwendig statisch onbepaalheid voor dit voorbeeld $6 + 2 - 6 = 2 $.

   ::::::

```{hide-sticky-margin}
```

```{index} Graag van inwendig statisch onbepaaldheid
```
## Bepalen graad van inwendig statisch onbepaaldheid
Voor de berekening van inwendig statisch onbepaaldheid gelden de volgende stappen:

::::::{prf:algorithm} Graad van inwendig statisch onbepaaldheid
:nonumber: true
:label: graad_inwendig_stat_onbepaaldheid

1. Controleer of de constructie open is. Als de constructie open is, dan is de inwendige statisch bepaaldheid gelijk aan de uitwendige statisch bepaaldheid en voldoet de simpelere berekening voor uitwendige statisch onbepaaldheid. Zo niet, ga verder met stap 2.
2. Splits de constructie in alle losse knopen en staven, en teken het vrijlichaamsschema voor mogelijke krachten op de knopen. Houd daarbij rekening houdend met welke staven en opleggingen er aan de knopen verbonden zijn.
3. Teken het vrijlichaamsschema voor de staven: teken de even grote maar tegengestelde reactiekrachten op de staven ten gevolge van de krachten op de knopen.
4. Tel het aantal onbekende krachten: oplegreacties en staafkrachten (de even grote maar tegengestelde reactiekrachten tellen niet apart mee)
5. Tel het aantal onafhankelijke evenwichtsvergelijkingen dat je op elk vrijlichaamsschema kan toepassen om de onbekende krachten te bepalen.
6. De graad van statisch onbepaaldheid is het aantal onbekende oplegreacties + onbekende staafkrachten - aantal evenwichtsvergelijkingen

Eventueel kan je ook nog onderscheid maken tussen pendelstaven en reguliere staven. In dat geval zijn er minder onbekende krachten, maar heb je per pendelstaaf ook maar 1 evenwichtsvergelijking. Let in dat geval op dat je bij de aansluitende knopen niet te veel evenwichtsvergelijkingen meeneemt.

::::::

::::::{prf:example}
:nonumber: true

```{figure} ./determinancy_data/Example_abc.svg
---
name: example_sd_abc
align: center
number:
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
figclass: sticky-margin
---

```

Als voorbeeld bepalen we de inwendige statisch onbepaaldheid van deze constructie.

::::::

1. Controleer of de constructie open is. Als de constructie open is, dan is de inwendige statisch bepaaldheid gelijk aan de uitwendige statisch bepaaldheid en voldoet de simpelere berekening voor uitwendige statisch onbepaaldheid. Zo niet, ga verder met stap 2.

   ::::::{prf:example}
   :nonumber: true

   De constructie is gesloten vanwege de lus $\rm{BDC}$. De inwendige statisch bepaaldheid is dus niet gelijk aan de uitwendige statisch bepaaldheid en de simpelere berekening voor uitwendige statisch onbepaaldheid kan niet worden gebruikt. Er moet verder worden gegaan met stap 2.

   ::::::

2. Splits constructie in alle losse knopen en staven, en teken het vrijlichaamsschema voor mogelijke krachten op de knopen. Houd daarbij rekening houdend met welke staven en opleggingen er aan de knopen verbonden zijn.

   ::::::{prf:example}
   :nonumber: true

   De constructie bestaat uit 4 knopen:
   - Op knoop $\rm{A}$ en $\rm{B}$ werken onbekende oplegreacties.
   - Knoop $\rm{A}$ is een scharnierende oplegging en uiteinde dus daar werken geen buigende momenten.
   - In knoop $\rm{B}$ kunnen er buigende momenten optreden vanuit $\rm{BC}$ en $\rm{BD}$ en in evenwicht zijn, alhoewel de oplegging een scharnier is.
   - Op knoop $\rm{C}$ werkt vanuit staaf $\rm{DB}$ geen buigend moment vanwege de scharnierende verbinding.
   - Knoop $\rm{D}$ is scharnierend, dus hier werken geen buigende momenten op.
   
   De uitwendige kracht kan getekend worden, maar heeft geen invloed op de verdere berekeningen. Dit geeft dus:

   ```{figure} ./determinancy_data/Example_4.svg
   ---
   name: example_sd_4
   align: center
   number:
   source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
   ---
   
   ```

   ::::::

3. Teken het vrijlichaamsschema voor de staven: teken de even grote maar tegengestelde reactiekrachten op de staven ten gevolge van de krachten op de knopen.

   ::::::{prf:example}
   :nonumber: true

   De krachten en momenten zoals getekend op de knopen kunnen in tegengestelde richting op de staven worden getekend.

   ```{figure} ./determinancy_data/Example_5.svg
   ---
   name: example_sd_5
   align: center
   source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
   number:
   ---
   
   ```

   ::::::

4. Tel het aantal onbekende krachten: oplegreacties en staafkrachten (de even grote maar tegengestelde reactiekrachten tellen niet apart mee)

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_6.svg
   ---
   name: example_sd_6
   align: center
   source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
   number:
   ---

   ```

   Er zijn $\left(2+2\right)=4$ onbekende oplegreacties en $\left( 2 + 3 + 3 + 2 + 2 + 2 +3 +3\right)=20$ onbekende staafkrachten.

   ::::::

5. Tel het aantal onafhankelijke evenwichtsvergelijkingen dat je op elk vrijlichaamsschema kan toepassen om de onbekende krachten te bepalen.

   ::::::{prf:example}
   :nonumber: true

   ```{figure} ./determinancy_data/Example_9.svg
   ---
   name: example_sd_9
   align: center
   source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
   number:
   ---
   
   ```

   - Van de knopen werken er op knoop $\rm{A}$ en $\rm{D}$ geen momenten, dus die zijn enkel met verticaal en evenwicht te bepalen.
   - Op de knopen $\rm{B}$ en $\rm{C}$ werken er wel momenten, dus daar zijn $3$ evenwichtsvergelijkingen nodig om de krachten te bepalen.
   - Omdat de staven starre lichamen zijn, zijn daar ook $3$ evenwichtsvergelijkingen nodig om de krachten te bepalen.
   
   In totaal zijn er dus $\left(2 + 3 +3 + 3 +2 + 3 + 3 +3 \right) = 22$ evenwichtsvergelijkingen

   ::::::

6. De graad van statisch onbepaaldheid is het aantal onbekende oplegreacties + onbekende staafkrachten - aantal evenwichtsvergelijkingen

   ::::::{prf:example}
   :nonumber: true

   De graad van inwendig statisch onbepaalheid voor dit voorbeeld $ 4 + 20 - 22 = 2 $.

   ::::::

```{hide-sticky-margin}
```

## Instructies in collegevorm

Dit onderwerp is [in 2025 in les 1](https://collegerama.tudelft.nl/Mediasite/Channel/public-ceg-ctb2210/watch/fc174f1ac52e415bb30998603fd2b4351d?sortBy=most-recent) gepresenteerd in collegevorm van 0:34:40 tot 1:00:40. De opname in collegejaar 2026/2027 volgt na het college.

## Opgaves in boek
- Opgaves 4.11 - 4.22, van hoofdstuk 4 van het boek *Mechanica: Evenwicht* {cite:p}`Hartsuijker1999`. Negeer de vragen over kinematisch bepaaldheid. Antwoorden zijn beschikbaar op [deze website](https://icozct.tudelft.nl/TUD_CT/bookanswers/vol1/Chapter4/).
- Opgave  9.6, van hoofdstuk 9 van het boek *Mechanica: Evenwicht* {cite:p}`Hartsuijker1999`. Negeer de vragen over kinematisch bepaaldheid. Antwoorden zijn beschikbaar op [deze website](https://icozct.tudelft.nl/TUD_CT/bookanswers/vol1/Chapter9/).
