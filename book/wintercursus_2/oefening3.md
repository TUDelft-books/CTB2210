````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze pagina is aangepast van https://oit.tudelft.nl/CT1000/2025/week_8/session_1/intro.html

```
````

# Begeleide oefening 3: Temperatuursinvloeden met krachtenmethode

Gegeven is de volgende constructie:

```{figure} ./oefening1_data/temp.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2

Constructie
```

Als je [](./oefening2.md) hebt overgeslagen, maak dan alsnog de eerste paar vragen van [die oefening](./oefening2.md) om de graad van statische onbepaaldheid te bepalen en een statisch bepaalde constructie te kiezen.

```{figure} oefening1_data/stat_bepaald_temp.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2

Statisch bepaalde constructie
```

:::::{exercise}
:nonumber: true

Gegeven vier krommingsdiagrammen ten gevolge van temperatuursinvloeden:

```{figure} oefening1_data/kappaT.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2

Vier mogelijke krommingen ten gevolge van temperatuursinvloeden
```

```{h5p} https://tudelft.h5p.com/content/1292772461750466947/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

De temperatuur zorgt voor verlenging aan de bovenkant, dus kromming met de bolle kant naar boven. Daarnaast is de kromming constant over de lengte van de balk, dus optie 1 is correct.
::::

:::::{exercise}
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292772462811195267/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

$$\kappa^{\rm{T}} = \alpha \cfrac{\Delta T}{h} = 10^{-5} \cdot \cfrac{32}{0.2} = 0.0016 \, \rm{(1/m)}$$

::::

Gekozen wordt voor de volgende statisch bepaalde constructie met een kinematisch equivalente belasting om de temperatuursinvloeden van buiging te modelleren:

```{figure} oefening1_data/kinem.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/steunpunt_temp_stijfheid2

Statisch bepaalde constructie met kinematisch equivalente belasting. De extensie van staaf $\rm{BCD}$ wordt niet gemodelleerd met een kinematisch equivalente belasting.
```

De zakking en rotatie van $\rm{C}$ zijn berekend:

$$
\begin{align*}
w_{\rm{C}} &= \cfrac{(111.6 - A_{\rm{v}}) \cdot 5^3}{3 \cdot 320000} + \cfrac{(446.4 - 4 \cdot A_{\rm{h}}) \cdot 5^2}{2 \cdot 320000} + \cfrac{512 \cdot 5^2}{2 \cdot 320000} \\
w_{\rm{C}} &=-\cfrac{A_{\rm{h}}}{6400} - \cfrac{A_{\rm{v}}}{7680} + \cfrac{1663}{32000} \left(↓\right)\\
\varphi_{\rm{C}} &= \cfrac{(111.6 - A_{\rm{v}}) \cdot 5^2}{2 \cdot 320000} + \cfrac{(446.4 - 4 \cdot A_{\rm{h}}) \cdot 5}{320000} + \cfrac{512 \cdot 5}{320000} \\
\varphi_{\rm{C}} &= -\cfrac{A_{\rm{h}}}{16000} - \cfrac{A_{\rm{v}}}{25600} + \cfrac{6187}{320000} \left( ↺ \right)
\end{align*}
$$

:::::{exercise}
:nonumber: true

Bepaal de verplaatsing van $\rm{A}$.

```{h5p} https://tudelft.h5p.com/content/1292772452651361377/embed
```

:::::

::::{admonition} Oplossing
:class: solution, dropdown

De verplaatsing van $\rm{C}$ kan op [dezelfde manier worden berekend als eerder](./oefening2.md), maar nu inclusief de rek van $\rm{BC}$:

$$
\begin{align*}
w_{\rm{A_v}} &= w_{\rm{C}} \\
w_{\rm{A_v}} &=-\cfrac{A_{\rm{h}}}{6400} - \cfrac{A_{\rm{v}}}{7680} + \cfrac{1663}{32000} \\
w_{\rm{A_h}} &= \varphi_{\rm{C}} \cdot 4 - \cfrac{A_{\rm{h}} \cdot 4^3}{3 \cdot 320000} - \cfrac{1}{625} \\
w_{\rm{A_h}} &=-\cfrac{256003 \cdot A_{\rm{h}}}{12000} - \cfrac{A_{\rm{v}}}{6400} + \cfrac{6123}{80000}\\
\end{align*}
$$

::::

:::::{exercise}
:nonumber: true

Los $A_{\rm{v}}$ en $A_{\rm{h}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292772452994493917/embed
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
{A_{\rm{v}} \approx 400 \ \rm{kN}} \\
{A_{\rm{h}} \approx 0 \ \rm{kN}}
\end{matrix}
$$

::::
