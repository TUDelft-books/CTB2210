````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze theorie is aangepast van https://github.com/TUDelft-books/CT1000 versie 2024.
```
````

# Instructie

Bij de **krachten**methode maak je gebruik van vormveranderingsvoorwaardes om de statisch onbepaalde **krachten** te bepalen. Echter, met dezelfde aanpak kan je ook evenwichtsvoorwaardes opstellen om statisch onbepaalde **verplaatsingen** op te lossen: de **verplaatsingen**methode. Dit kan nuttig zijn omdat een enkele evenwichtsvoorwaarde soms al kan voldoen tegenover meerdere vormveranderingsvoorwaardes.

De stappen zijn zeer vergelijkbaar met de krachtenmethode, met als enige verschil dat we geen opleggingen weg kunnen nemen omdat de statisch onbepaalde verplaatsing daar gelijk moet zijn aan 0.

1. Bepaal de graad van statische bepaaldheid.
2. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij pendelstaven of scharnieren toe te voegen: voeg onbekende statisch onbepaalde verplaatsingen toe en evenwichtsvoorwaarden toe voor elke aansluiting van de pendelstaven die je hebt weggenomen en scharnieren die je hebt toegevoegd. Let op dat je de constructie niet transformeert tot een (gedeeltelijk) mechanisme!

    `````{tab-set}
    ````{tab-item} Weghalen oplegging
    % Figures from https://github.com/TUDelft-books/CEG-mechanics-BSc/blob/EN/book/statically_inderminate/force_method/force_method_data/Tekening1.vsdx
    ```{figure} theorie_data/verplaats_1.svg
    :align: center
    ```
    ````
    ````{tab-item} Toevoegen scharnieren
    ```{figure} theorie_data/verplaats_3.svg
    :align: center
    ```
    ````
    `````

3. Los de krachten op in termen van de onbekende onbepaalde verplaatsingen.
4. Gebruik je evenwichtsvoorwaarden om de statisch onbepaalde verplaatsingen op te lossen.

De toepassing van de verplaatsingenmethode wordt getoond op onderstaande voorbeeld.

::::::{prf:example}
:nonumber: true
:label: verpl_0

% figure from https://github.com/TUDelft-books/CT1000/blob/2025-draft/book/week_7/session_1/intro_data/Tekening1.vsdx

```{figure} ./theorie_data/structure.svg
---
align: center
---
Voorbeeldconstructie
```
::::::

1. Bepaal de graad van statische bepaaldheid.

    ::::::{prf:example}
    :nonumber: true
    :label: verpl_1

    Voor ons voorbeeld zijn we geïnteresseerd in de interne krachtenverdeling, dus moeten we de graad van interne statische onbepaaldheid evalueren.

    ```{figure} ./theorie_data/stat_onbepaald_krachten.svg
    ---
    align: center
    ---
    Er zijn 20 onbekende krachten.
    ```

    ```{figure} ./theorie_data/stat_onbepaald_vergel.svg
    ---
    align: center
    ---
    Er zijn 18 evenwichtsvergelijkingen.
    ```

    Deze constructie is dus 2e orde intern statisch onbepaald.

    ::::::

2. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij pendelstaven of scharnieren toe te voegen: voeg onbekende statisch onbepaalde verplaatsingen toe en evenwichtsvoorwaarden toe voor elke aansluiting van de pendelstaven die je hebt weggenomen en scharnieren die je hebt toegevoegd. Let op dat je de constructie niet transformeert tot een (gedeeltelijk) mechanisme!

    ::::::{prf:example}
    :nonumber: true
    :label: verpl_2

    Er zijn geen pendelstaven in deze constructie, dus de enige optie is het toevoegen van scharnier. Twee scharnieren net links en rechts van $\rm{D}$ komt op hetzelfde neer als één scharnier in $\rm{D}$, leidend tot het volgende statisch bepaalde systeem.

    ```{figure} ./theorie_data/static_deter.svg
    ---
    align: center
    ---
    Statisch onbepaalde systeem met statisch onbepaalde verplaatsing $\varphi_{\rm{D}}$ en evenwichtsvergelijking $-M_{\rm{D}}^{\rm{AD}} + M_{\rm{D}}^{\rm{BD}} + M_{\rm{D}}^{\rm{CD}} = 0$
    ```

    ::::::

3. Los de krachten op in termen van de onbekende onbepaalde verplaatsingen.

    ::::::{prf:example}
    :nonumber: true
    :label: verpl_3

    Elk van de krachten $M_{\rm{D}}^{\rm{AD}}$, $M_{\rm{D}}^{\rm{CD}}$, $M_{\rm{D}}^{\rm{BD}}$ kan nu worden uitgedrukt als functie van $\varphi_{\rm{D}}$ met behulp van vergeet-me-nietjes:

    - Voor $\rm{AD}$: $\varphi_{\rm{D}} = \cfrac{5M_{\rm{D}}^{\rm{AD}}}{3 EI} + \cfrac{ 15 \cdot 5}{6 EI}$.
    - Voor $\rm{BD}$: $\varphi_{\rm{D}} = - \cfrac{2M_{\rm{D}}^{\rm{BD}}}{3 EI} - \cfrac{ 12 \cdot 2^3}{24 EI}$
    - Voor $\rm{CD}$: $\varphi_{\rm{D}} = - \cfrac{5M_{\rm{D}}^{\rm{CD}}}{3 EI}$

    Dit kan worden omgeschreven naar:

    - $M_{\rm{D}}^{\rm{AD}} = 72000 \varphi_{\rm{D}} - 7.5  $
    - $M_{\rm{D}}^{\rm{DB}} = - 180000 \varphi_{\rm{D}} - 6 $
    - $M_{\rm{D}}^{\rm{CD}} = - 72000 \varphi_{\rm{D}}$

    ::::::

4. Gebruik je evenwichtsvoorwaarden om de statisch onbepaalde verplaatsingen op te lossen.

    ::::::{prf:example}
    :nonumber: true
    :label: verpl_4

    Invullen van onze uitdrukkingen voor de momenten in onze evenwichtsvergelijking $-M_{\rm{D}}^{\rm{AD}} + M_{\rm{D}}^{\rm{BD}} + M_{\rm{D}}^{\rm{CD}} = 0$ geeft: $\varphi_{\rm{D}} = \cfrac{5}{9EI} = \cfrac{1}{216000} = 4.63 \cdot 10^{-6} \rm{ rad}$

    Eventueel kan nu ook de momentenverdeling worden gevonden:
    - $M_{\rm{D}}^{\rm{AD}} = -\cfrac{43}{6} \approx -7.17 \rm{ kNm}$
    - $M_{\rm{D}}^{\rm{DB}} = -\cfrac{41}{6} \approx -6.83 \rm{ kNm}$
    - $M_{\rm{D}}^{\rm{DC}} = -\cfrac{1}{3} \approx - 0.333 \rm{ kNm} $

    ::::::

## Meer voorbeelden


## Oefeningen
