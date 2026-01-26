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

```{figure} oefening1_data/stat_onbepaaldheid.svg
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
````{tab-item} Horizontale oplegging bij A weggehaald en scharnier toegevoegd bij C

```{figure} ./oefening1_data/variant1.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2
```

Deze constructie is geen geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode want het is een mechanisme.
````

````{tab-item} Horizontale oplegging bij A en B weggehaald en rotatie vrijgemaakt bij B
```{figure} ./oefening1_data/variant2.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2
```

Deze constructie is geen geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode, want hoewel de constructie tweedegraads statisch onbepaald is zijn er zelfs drie statisch onbepaalde krachten toegevoegd. Daarmee is deze constructie sowieso een mechanisme geworden.
````

````{tab-item} Scharnierende oplegging bij A weggehaald
```{figure} ./oefening1_data/variant3.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2
```

Deze constructie is een geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode.
````

````{tab-item} Verticale en rotatie oplegging bij B weggehaald
```{figure} ./oefening1_data/variant4.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2
```

Deze constructie is een geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode. Het is alleen geen hele handige constructie omdat we geen vergeet-me-nietjes hebben die de vervormingen van deze constructie beschrijven.
````

````{tab-item} Horizontale oplegging bij A weggehaald en rotatie vrijgemaakt bij B.
```{figure} ./oefening1_data/variant5.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2
```

Deze constructie is een geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode. Het is alleen geen hele handige constructie omdat we geen vergeet-me-nietjes hebben die de vervormingen van deze constructie beschrijven.
````

````{tab-item} Verticale oplegging bij B weggehaald en scharnier toegevoegd bij C.
```{figure} ./oefening1_data/variant6.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2
```

Deze constructie is een geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode.
````

````{tab-item} Scharnier toegevoegd bij C en rotatie vrijgemaakt in B
```{figure} ./oefening1_data/variant7.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2
```

Deze constructie is een geldig statisch bepaald systeem om de constructie op te lossen met de krachtenmethode, het is tevens de methode van hoekveranderingsvergelijkingen.
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

::::{admonition} Oplossing
:class: solution, dropdown

De dwarskracht en het buigend moment net rechts van $\rm{C}$ kunnen worden bepaald met behulp van evenwicht:

```{figure} oefening1_data/VCMC.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2
```

$$
\sum F_{\rm{v}}^{\rm{DCA}} = 0 \to V_{\rm{C}}^{\rm{CD}} = 111.6 - A_{\rm{v}} \\
\sum \left. T \right|_{\rm{C}}^{\rm{DC}} = 0 \to M_{\rm{C}}^{\rm{CD}} = 446.4 - 4 \cdot A_{\rm{h}}
$$

De verplaatsing en rotatie van $\rm{C}$ kunnen worden bepaald met vergeet-me-nietjes en de steunpuntszetting van $\rm{B}$:

```{figure} oefening1_data/BC2.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2
```

$$
\begin{align*}
w_{\rm{C}} &= \cfrac{(111.6 - A_{\rm{v}}) \cdot 4^3}{3 \cdot 320000} + \cfrac{(446.4 - 4 \cdot A_{\rm{h}}) \cdot 4^2}{2 \cdot 320000} + 0.031 \\
w_{\rm{C}} &=-\cfrac{A_{\rm{h}}}{6400} - \cfrac{A_{\rm{v}}}{7680} + \cfrac{403}{6400} \\
w_{\rm{C}} &\approx -0.00015625 \cdot A_{\rm{h}} - 0.00013020833 \cdot A_{\rm{v}} + 0.06296875 \\
\varphi_{\rm{C}} &= \cfrac{(111.6 - A_{\rm{v}}) \cdot 4^2}{2 \cdot 320000} + \cfrac{(446.4 - 4 \cdot A_{\rm{h}}) \cdot 4}{320000} \\
\varphi_{\rm{C}} &= -\cfrac{A_{\rm{h}}}{16000} - \cfrac{A_{\rm{v}}}{25600} + \cfrac{3627}{320000} \\
\varphi_{\rm{C}} &= -0.0000625 \cdot A_{\rm{h}} - 0.0000390625 \cdot A_{\rm{v}} + 0.011334375
\end{align*}
$$

Nu kan de verplaatsing van $\rm{A}$ worden bepaald met de verticale verplaatsing van $\rm{C}$, door de rotatie van $\varphi_{\rm{C}}$ uit te breiden over ligger $\rm{AC}$ en de extra verplaatsing door $A_{\rm{h}}$:

```{figure} oefening1_data/AC2.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2
```

$$
\begin{align*}
w_{\rm{A_v}} &= w_{\rm{C}} \\
w_{\rm{A_v}} &=-\cfrac{A_{\rm{h}}}{6400} - \cfrac{A_{\rm{v}}}{7680} + \cfrac{403}{6400} \\
w_{\rm{A_v}} &\approx -0.00015625 \cdot A_{\rm{h}} - 0.00013020833 \cdot A_{\rm{v}} + 0.06296875 \\
w_{\rm{A_h}} &= \varphi_{\rm{C}} \cdot 4 - \cfrac{A_{\rm{h}} \cdot 4^3}{3 \cdot 320000} \\
w_{\rm{A_h}} &=-\cfrac{19 \cdot A_{\rm{h}}}{60000} - \cfrac{A_{\rm{v}}}{6400} + \cfrac{3627}{80000} \\
w_{\rm{A_h}} &\approx -0.00031666667 \cdot A_{\rm{h}} - 0.00015625 \cdot A_{\rm{v}} + 0.0453375
\end{align*}
$$


::::

:::::{exercise}
:nonumber: true

Los $A_{\rm{v}}$ en $A_{\rm{h}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292762004624970817/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

$$
\left\{
\begin{matrix}
{w_{\rm{A_v}}=0} \\
{w_{\rm{A_h}}=0}
\end{matrix}
\right.
\;\to\;
\begin{matrix}
{A_{\rm{v}} = 764.4 \ \rm{kN}} \\
{A_{\rm{h}} = -234 \ \rm{kN}}
\end{matrix}
$$

::::