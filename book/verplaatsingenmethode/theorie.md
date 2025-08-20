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

```{figure} ./theorie_data/kin_eq_load_SB.svg
:align: center

Kinematisch equivalente belasting die tot dezelfde rek en kromming leidt als rek door lineaire uitzetting
```



## Meer voorbeelden


## Oefeningen
