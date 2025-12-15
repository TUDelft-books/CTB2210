````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze pagina is aangepast van https://oit.tudelft.nl/CT1000/2025/week_8/session_1/intro.html

```
````

# Begeleide oefening 2: Steunpuntszettingen met krachtenmethode

Gegeven is de volgende constructie:

```{figure} ./oefening1_data/supp_settlement.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2

Constructie
```

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292772401151751837/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

De constructie is open, dus de graad van uitwendige statisch onbepaaldheid is gelijk aan de graad van inwendige statisch onbepaaldheid.

::::

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292772402864340307/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Er zijn 5 onbekende oplegreacties:

```{figure} intro_data/stat_onbepaaldheid.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2

Vrijlichaamsschema van de gehele constructie met 5 onbekende oplegreacties
```

::::

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292772403342515597/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Er zijn 3 evenwichtsvergelijkingen.

::::

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292772403877668617/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

De constructie is 2de graads statisch onbepaald.

::::

:::::{exercise}
:nonumber: true

Welke van de volgende statisch bepaalde systemen kan gebruikt worden voor toepassing van de krachtenmethode?

```{h5p} https://tudelft.h5p.com/content/1292772408785381147/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

`````{tab-set}
````{tab-item} Pendelstaaf doorgesneden net onder C

```{figure} ./oefening1_data/variant1.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

Deze constructie is een geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode of verplaatsingenmethode met statisch onbepaalde verplaatsingen.
````

````{tab-item} Horizontale oplegging bij D weggehaald
```{figure} ./oefening1_data/variant2.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

Deze constructie is geen geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode, want de constructie is een mechanisme.
````

````{tab-item} Verticale oplegging bij D weggehaald
```{figure} ./oefening1_data/variant3.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

Deze constructie is een geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode.
````

````{tab-item} Verticale oplegging bij B weggehaald
```{figure} ./oefening1_data/variant4.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

Deze constructie is een geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode. Deze constructie is echter niet zo handig, omdat er geen vergeet-me-nietjes zijn voor ligger $ABC$
````

````{tab-item} Horizontale oplegging bij B weggehaald
```{figure} ./oefening1_data/variant5.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

Deze constructie is geen geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode, want de constructie is een mechanisme.
````

````{tab-item} Horizontale oplegging bij B weggehaald
```{figure} ./oefening1_data/variant6.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

Deze constructie is een geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode.
````

````{tab-item} Scharnier toegevoegd tussen B en C
```{figure} ./oefening1_data/variant7.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

Deze constructie is een geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode of verplaatsingenmethode met statisch onbepaalde verplaatsingen.
````

`````
::::

We gaan rekenen met de volgende statisch bepaalde constructie

```{figure} oefening1_data/stat_bepaald.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2

Statisch bepaalde constructie
```

:::::{exercise}
:nonumber: true

Los de krachtsverdeling en verplaatsingen van deze constructie op als functie van 
$A_{\rm{v}}$ en $A_{\rm{h}}$.

```{h5p} https://tudelft.h5p.com/content/1292772429918274017/embed
```

:::::

:::::{exercise}
:nonumber: true

Los $A_{\rm{v}}$ en $A_{\rm{h}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292762004624970817/embed
```

:::::