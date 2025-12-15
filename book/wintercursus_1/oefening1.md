````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze pagina is aangepast van https://oit.tudelft.nl/CT1000/2025/week_7/session_1/intro.html

```
````

# Begeleide oefening 1: Krachtenmethode en verplaatsingenmethode met statisch onbepaalde verplaatsingen

Gegeven is de volgende constructie:

```{figure} ./lesoefening1_data/constructie.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2

Constructie
```

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292761970500067547/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Ja, want de constructie is open. Het wel of niet hebben van scharnieren beïnvloedt niet het verschil tussen uitwendige en inwendige statisch onbepaaldheid

::::

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292761973993222987/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Er zijn 4 onbekende oplegreacties en 1 onbekende verbindingskrachten. Dat zijn 5 onbekende krachten in totaal.

Als je 3 onbekende oplegreacties hebt geantwoord omdat je de horizontale oplegreactie bij B al hebt geëlimineerd is dat ook goed. Het aantal evenwichtsvergelijkingen is dan ook eentje minder
::::

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292761975857105107/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Er zijn 4 evenwichtsvergelijkingen.

Als je 3 hebt geantwoord omdat je deze al hebt gebruikt om de horizontale evenwichtsvergelijking bij B te elimineren is dat ook goed.
::::

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292761976954444857/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

De constructie is 1ste graads uitwendig statisch onbepaald

::::

:::::{exercise}
:nonumber: true

Welke van de volgende statisch bepaalde systemen kan gebruikt worden voor toepassing van de krachtenmethode, en voor sommige systemen voor toepassing van de verplaatsingenmethode met statisch onbepaalde verplaatsingen?

```{h5p} https://tudelft.h5p.com/content/1292761985601316837/embed
```

:::::

:::::::{admonition} Oplossing
:class: solution, dropdown

`````{tab-set}
````{tab-item} Pendelstaaf doorgesneden net onder C

```{figure} ./lesoefening1_data/optie1.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

Deze constructie is een geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode of verplaatsingenmethode met statisch onbepaalde verplaatsingen.
````

````{tab-item} Horizontale oplegging bij D weggehaald
```{figure} ./lesoefening1_data/optie2.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

Deze constructie is geen geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode, want de constructie is een mechanisme.
````

````{tab-item} Verticale oplegging bij D weggehaald
```{figure} ./lesoefening1_data/optie3.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

Deze constructie is een geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode.
````

````{tab-item} Verticale oplegging bij B weggehaald
```{figure} ./lesoefening1_data/optie4.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

Deze constructie is een geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode.
````

````{tab-item} Verticale oplegging bij B weggehaald
```{figure} ./lesoefening1_data/optie4.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

Deze constructie is een geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode. Deze constructie is echter niet zo handig, omdat er geen vergeet-me-nietjes zijn voor ligger $ABC$
````

````{tab-item} Horizontale oplegging bij B weggehaald
```{figure} ./lesoefening1_data/optie5.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

Deze constructie is geen geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode, want de constructie is een mechanisme.
````

````{tab-item} Horizontale oplegging bij B weggehaald
```{figure} ./lesoefening1_data/optie6.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

Deze constructie is een geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode.
````

````{tab-item} Scharnier toegevoegd tussen B en C
```{figure} ./lesoefening1_data/optie7.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

Deze constructie is een geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode of verplaatsingenmethode met statisch onbepaalde verplaatsingen.
````

````{tab-item} Scharnier toegevoegd tussen C en D
```{figure} ./lesoefening1_data/optie8.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

Deze constructie is geen geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode of verplaatsingenmethode met statisch onbepaalde verplaatsingen, want de constructie is een mechanisme.
````

`````

:::::::

## Krachtenmethode

Er wordt gekozen voor het volgende statisch bepaalde systeem:

```{figure} ./lesoefening1_data/statisch_onbepaald_krachtenmethode.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
Statistisch bepaalde constructie
```

:::::{exercise}
:nonumber: true

Los $w_{\rm{C}}^{\rm{BC}}$ en $w_{\rm{C}}^{\rm{CD}}$ op als functie $N_{\rm{CD}}$.

```{h5p} https://tudelft.h5p.com/content/1292762000009609427/embed
```

:::::

:::::::{admonition} Oplossing
:class: solution, dropdown

Het moment in $\rm{B}$ kan worden gevonden met behulp van evenwicht:

```{figure} lesoefening1_data/MB.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

$$
\sum \left. T \right|_{\rm{B}}^{\rm{BC}} = 0 \to M_{\rm{B}} = 3 \cdot N_{\rm{CD}}
$$

Met vergeet-me-nietjes kan de rotatie van $\rm{B}$ worden gevonden:

```{figure} lesoefening1_data/AB.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

$$
\varphi_{\rm{B}} = \cfrac{94.5 \cdot 4^3}{3 \cdot 420000} - \cfrac{N_{\rm{CD}} \cdot 4}{3 \cdot 420000} = \cfrac{3}{500} - \cfrac{N_{\rm{CD}}}{10500} \approx 0.006 - 9.52 \cdot 10^{-5} \cdot N_{\rm{CD}}
$$

De verplaatsing van $\rm{C}$ kan worden gevonden door de rotatie van $\rm{B}$ over de lengte van ligger $\rm{BC}$ door te trekken en daar nog extra doorbuiging door een vergeet-me-nietje bij op te tellen:

```{figure} lesoefening1_data/BCw.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

$$
w_{\rm{C}}^{\rm{BC}} = -\varphi_{\rm{B}} \cdot 3 + \cfrac{N_{\rm{CD}} \cdot 3^3}{3 \cdot 420000} = \cfrac{-9}{500} + \cfrac{1}{2000} \cdot N_{\rm{CD}} = -0.018 + 5 \cdot 10^{-4} \cdot N_{\rm{CD}}
$$

Voor het andere deel kan de verplaatsing van $\rm{C}$ worden gevonden met behulp van de relaties voor een staaf onder trek:

```{figure} lesoefening1_data/CD.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
```

$$
w_{\rm{C}}^{\rm{CD}} = -\cfrac{N_{\rm{CD}} \cdot 5}{1250} = -{1}{250} \cdot N_{\rm{CD}} = 0.004 \cdot N_{\rm{CD}}
$$

:::::::


:::::{exercise}
:nonumber: true

Los $N_{\rm{CD}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292762004624970817/embed
```

:::::

:::::::{admonition} Oplossing
:class: solution, dropdown

$$
\begin{align*}
w_{\rm{C}}^{\rm{BC}} \left( N_{\rm{CD}} \right) &= w_{\rm{C}}^{\rm{CD}} \left( N_{\rm{CD}} \right) \\
-0.018 + 5 \cdot 10^{-4} \cdot N_{\rm{CD}} &= -0.004 \cdot N_{\rm{CD}} \\
 N_{\rm{CD}} &= -4 \, \rm{kN}
\end{align*}
$$

:::::::

## Verplaatsingenmethode met statisch onbepaalde verplaatsingen

Er wordt gekozen voor het volgende statisch bepaalde systeem:

```{figure} ./lesoefening1_data/statisch_onbepaald_verplaatsingenmethode.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_2
Statistisch bepaalde constructie
```

:::::{exercise}
:nonumber: true

Los $N_{\rm{C}}^{\rm{BC}}$ en $N_{\rm{C}}^{\rm{CD}}$ op als functie $w_{\rm{C}}$.

```{h5p} https://tudelft.h5p.com/content/1292762009952181537/embed
```

:::::

:::::::{admonition} Oplossing
:class: solution, dropdown

Omschrijven van de relaties bij de krachtenmethode geeft:

$$
N_{\rm{C}}^{\rm{BC}} = 2000 \cdot w_{\rm{C}} + 36
$$

en

$$
N_{\rm{C}}^{\rm{CD}} = -250 \cdot w_{\rm{C}}
$$

:::::::


:::::{exercise}
:nonumber: true

Los $w_{\rm{C}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292762010395617757/embed
```

:::::

:::::::{admonition} Oplossing
:class: solution, dropdown

$$
\begin{align*}
N_{\rm{C}}^{\rm{BC}} \left( w_{\rm{C}} \right) &= N_{\rm{C}}^{\rm{CD}} \left( w_{\rm{C}} \right) \\
2000 \cdot w_{\rm{C}} + 36 &= -250 \cdot w_{\rm{C}} \\
w_{\rm{C}} &= \cfrac{-2}{125} = -0.016 \, \rm{m} 
\end{align*}
$$

:::::::