````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze pagina is aangepast van https://oit.tudelft.nl/CT1000/2025/week_8/session_1/intro.html

```
````

# Begeleide oefening 1: Stijfheidsinvloeden met verplaatsingenmethode met vrijheidsgraden

Gegeven is de volgende constructie:

```{figure} ./oefening1_data/temp_infl.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2

Constructie
```

## Vermenigvuldigingsfactor

Voor de toepassing van de vermenigvuldigingsfactor gebruiken we de verplaatsingenmethode met vrijheidsgraden, andere opties zijn ook mogelijk:

```{figure} ./oefening1_data/phi_C.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2

Constructie met vrijheidsgraad $\varphi_C$ aangegeven
```

:::::{exercise}
:nonumber: true

Gegeven zijn 6 vergeet-me-nietjes:

```{figure} ../wintercursus_1/lesoefening1_data/vergeet-me-nietjes.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden

Vergeet-me-nietjes
```

```{h5p} https://tudelft.h5p.com/content/1292763061509985047/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Vergeet-me-nietje 3 en 4 zijn van toepassing op $\rm{AC}$ en $\rm{BC}$ aangezien $\rm{E}$ op z'n plek blijft (alleen roteert) en dus kan worden gezien als oplegging.

::::


:::::{exercise}
:nonumber: true

Los $M_{\rm{C}}^{\rm{AC}}$ en $M_{\rm{C}}^{\rm{BC}}$ op als functie $\varphi_{\rm{C}}$ en $n$.

```{h5p} https://tudelft.h5p.com/content/1292772348519402367/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Voor $\rm{AC}$ kan een statisch bepaald vergeet-me-nietje worden toegepast

```{figure} oefening1_data/AC.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2
```

$$\varphi_{\rm{C}} = \cfrac{M_{\rm{AC}} \cdot 4}{3 \cdot n \cdot 320000} \to M_{\rm{AC}} = 240000 \cdot n \cdot \varphi_{\rm{C}}$$

Voor $\rm{BC}$ kan een statisch onbepaald vergeet-me-nietje worden toegepast:

```{figure} oefening1_data/BC.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2
```

$$\varphi_{\rm{C}} = \cfrac{M_{\rm{AC}} \cdot 5}{4 \cdot 320000} \to M_{\rm{AC}} = 256000 \varphi_{\rm{C}}$$

::::

:::::{exercise}
:nonumber: true

Los $\varphi_{\rm{C}}$ op als functie van $n$.

```{h5p} https://tudelft.h5p.com/content/1292772355640589157/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

$\varphi_{\rm{C}}$ kan bepaald worden aan de hand van het vrijlichaamsschema van $\rm{DC}$:

```{figure} oefening1_data/Meven.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2
```

$$
\sum \left. T \right|_{\rm{C}}^{\rm{DC}} = 0 \to \varphi_{\rm{C}} = \cfrac{279}{10000 \cdot \left( 15 \cdot n + 16 \right)}
$$

::::

:::::{exercise}
:nonumber: true

Los $w_{\rm{D}}$ op als functie van $n$.

```{h5p} https://tudelft.h5p.com/content/1292772359322613707/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

De verplaatsing van $\rm{D}$ kan worden bepaald door de rotatie van $\varphi_{\rm{C}}$ over ligger $\rm{CD}$ te verlengen en de verticale verplaatsing door de belasting erbij op te tellen:

```{figure} oefening1_data/CD.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2
```

$$
\begin{align*}
w_{\rm{D}} &= \varphi_{\rm{C}} \cdot 4 + \cfrac{111.6 \cdot 4^3}{3 \cdot 320000} \\
w_{\rm{D}} & = \cfrac{93}{12500} + \cfrac{279}{2500 \cdot \left( 15 \cdot n + 16 \right)} \\
w_{\rm{D}} & = 0.00744 + \cfrac{0.1116}{15 \cdot n + 16}
\end{align*}
$$

::::

:::::{exercise}
:nonumber: true

Teken $w_{\rm{D}}$ als functie van $n$ voor $n$ variërend van 0 tot $\infty$.

:::::

::::{admonition} Oplossing
:class: solution, dropdown

```{figure} oefening1_data/plot.svg
:align: center
:source: https://github.com/TUDelft-books/CT1000/blob/2025/book/week_8/session_1/intro_data/berekeningen.py
```

::::

## Extreme gevallen

Voor het analyseren van de extreme gevallen analyseren we eerst de constructie zonder de methode voor de statisch onbepaaldheid direct toe te passen.

:::::{exercise}
:nonumber: true

Gegeven zijn 6 varianten van de constructie.

```{figure} ./oefening1_data/extreme_gevallen.svg
:align: center
:source: https://github.com/TUDelft-books/CT1000/blob/2025/book/week_8/session_1/intro_data/berekeningen.py
```

```{h5p} https://tudelft.h5p.com/content/1292772371515557127/embed
```

```{h5p} https://tudelft.h5p.com/content/1292772381952462747/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Voor $n \to \infty$, is er geen rotatie toegestaan in $\rm{C}$, wat de constructie reduceert tot een statisch bepaalde structuur:

```{figure} oefening1_data/CD.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2
```

Voor $n \to 0$, is er geen rotatiestijfheid in $\rm{AC}$, wat de constructie reduceert tot:

```{figure} oefening1_data/EI0.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2
```

::::


:::::{exercise}
:nonumber: true

Bepaal $w_{\rm{D}}$ voor de extreme gevallen.

```{h5p} https://tudelft.h5p.com/content/1292772385599932867/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Met een vergeet-me-nietje geeft $n \to \infty$ dit:

$$
\begin{align*}
w_{\rm{D}} &= \cfrac{111.6 \cdot 4^3}{3 \cdot 320000} \\
w_{\rm{D}} & = \cfrac{279}{2500 \cdot \left( 15 \cdot n + 16 \right)} \\
w_{\rm{D}} & = 0.00744
\end{align*}
$$

Dit kan ook worden afgeleid door de limiet te nemen van de eerder gevonden $w_{\rm{D}}$ als functie van $n$:

$$
\begin{align*}
\lim_{n \to \infty} w_{\rm{D}} &= \lim_{n \to \infty} \left( 0.00744 + \cfrac{0.1116}{15 \cdot n + 16} \right) \\
\lim_{n \to \infty} w_{\rm{D}}&= 0.00744 + 0 \\
\lim_{n \to \infty} w_{\rm{D}}&= 0.00744
\end{align*}
$$

Voor $n \to 0$, dit is een statisch bepaalde structuur welke kan worden opgelost met een methode naar keuze. Dit leidt tot:

$$
w_{\rm{D}} = 0.0144
$$

Dit kan ook worden afgeleid door de limiet te nemen van de eerder gevonden $w_{\rm{D}}$ als functie van $n$:

$$
\begin{align*}
\lim_{n \to 0} w_{\rm{D}} &= \lim_{n \to 0} \left( 0.00744 + \cfrac{0.1116}{15 \cdot n + 16} \right) \\
\lim_{n \to 0} w_{\rm{D}}&= 0.00744 + \cfrac{0.1116}{16} \\
\lim_{n \to 0} w_{\rm{D}}&= 0.0144
\end{align*}
$$

::::
