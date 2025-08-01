# Instructie steunpuntszettingen

````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze theorie is aangepast van https://github.com/TUDelft-books/CEG-mechanics-BSc versie EN.
```
````

Steunpuntszettingen zorgen bij statisch bepaalde constructies niet voor krachten of vervormingen door rek, er zullen hoogstens verplaatsingen en rotaties van elementen als geheel plaatsvinden.

```{figure} ./theorie_data/SB.svg
:align: center

Statisch bepaalde constructie onder invloed van steunpuntszetting
```

Bij uitwendig statisch onbepaalde constructies zijn rekloze verplaatsingen en rotaties niet mogelijk. Echter, omdat voor het berekeningen van statisch onbepaalde constructies de verplaatsingen sowieso geëvalueerd moeten worden kunnen deze extra verplaatsingen daarin worden meegenomen zonder dat het oplossingsproces verandert. De steunpuntsverplaatsingen zullen bij de bepaling van verplaatsingen vanzelf terecht komen in de vormveranderingsvoorwaardes.

De toepassing van steunpuntszettingen op een statisch bepaalde constructie wordt in een voorbeeld getoond met de krachtenmethode, specifiek de hoekveranderingsvergelijkingen. Andere methodes zijn ook mogelijk.

````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Dit voorbeeld is aangepast van https://github.com/TUDelft-books/CT1000 versie CTB2210-2025.
```
```` 

::::::{prf:example}
:nonumber: true
:label: steunpunt_0

```{figure} ./theorie_data/constructie.svg
---
align: center
---
Voorbeeldconstructie
```

::::::

1. Bepaal de graad van statische bepaaldheid.

    ::::::{prf:example}
    :nonumber: true
    :label: steunpunt_1

    ```{figure} ./theorie_data/statisch_onbepaaldheid.svg
    ---
    align: center
    ---
    Er zijn 16 onbekende krachten en 14 evenwichtsvergelijkingen
    ```

    Deze constructie is dus 2e orde intern statisch onbepaald.

    ::::::

2. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij een pendelstaaf, of scharnieren toe te voegen: voeg onbekende statisch onbepaalde krachten en vervormingsvoorwaardes toe voor elke opleggging die je hebt weggenomen en scharnieren die je hebt toegevoegd. Let op dat je de constructie niet transformeert tot een (gedeeltelijk) mechanisme!

    ::::::{prf:example}
    :nonumber: true
    :label: steunpunt_2

    Er wordt hier gekozen voor hoekveranderingsvergelijkingen. Dat geeft dit statisch bepaalde systeem.

    ```{figure} ./theorie_data/SB-systeem.svg
    ---
    align: center
    ---
    Statisch bepaald systeem
    ```

    ::::::

3. Los de verplaatsing op in termen van de onbekende onbepaalde krachten zoals je normaal zou doen voor een statisch bepaalde constructie.

    ::::::{prf:example}
    :nonumber: true
    :label: steunpunt_3

    Met behulp van vergeet-me-nietjes kunnen de rotaties worden gevonden ten gevolge van de momenten en verdeelde belasting. De staaf roteert ook nog als geheel, deze rotatie moet ook worden meegenomen.

    - $\varphi _{\rm{B}}^{{\rm{AB}}}  = \cfrac{{ - {M_{\rm{B}}} \cdot 4}}{{3 \cdot EI}} + \cfrac{{17 \cdot {4^3}}}{{24 \cdot EI}} - \cfrac{{{w_{\rm{B}}}}}{4}  = -\cfrac{M_{\rm{B}}}{25500} -\cfrac{7}{1500}$
    - $\varphi _{\rm{B}}^{{\rm{BC}}}  = \cfrac{{{M_{\rm{B}}} \cdot 6}}{{3 \cdot EI}} - \cfrac{{{M_{\rm{C}}} \cdot 6}}{{6 \cdot EI}} + \cfrac{{{w_{\rm{B}}}}}{6} = \cfrac{M_{\rm{B}}}{17000} - \cfrac{M_{\rm{C}}}{34000} + \cfrac{1}{250}$
    - $\varphi_{\rm{C}} = -\cfrac{M_\text{B} \cdot 6}{3 \cdot EI} + \cfrac{M_\text{C} \cdot 6}{6 \cdot EI} + \cfrac{w_\text{B}}{6} = -\cfrac{M_{\rm{B}}}{34000} + \cfrac{M_{\rm{C}}}{17000} + \cfrac{1}{250}$

    De rotatie van $\rm{AB}$ (met de klok mee) heeft de omgekeerde richting als $\varphi _{\rm{B}}^{{\rm{AB}}}$ (tegen de klok in), terwijl de rotatie van $\rm{BC}$ (met de klok mee) dezelfde richting is als $\varphi _{\rm{B}}^{{\rm{BC}}}$ en $\varphi_{\rm{C}}$.

    ::::::

4. Gebruik je vormveranderingsvoorwaarden om de statisch onbepaalde krachten op te lossen

    ::::::{prf:example}
    :nonumber: true
    :label: steunpunt_4

    $\varphi _{\rm{B}}^{{\rm{AB}}} = \varphi _{\rm{B}}^{{\rm{BC}}}$ en $ \varphi_{\rm{C}} = 0$ geeft:

    - $M_{\rm{B}} = -128 \ \rm{kNm}$
    - $M_{\rm{C}} = -132 \ \rm{kNm}$

    ::::::

## Meer voorbeelden

In hoofdstuk 6.1 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016` worden steunpuntszettingen behandeld. Voorbeeld 6.1.3 kan worden overgeslagen

## Oefeningen
- Opgaves 6.1 - 6.18, 6.20, 6.22 - 6.24 in hoofdstuk 6.3 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`. Er zijn helaas geen antwoorden beschikbaar.