# Extra tentamenopdracht

Deze tentamenopgave werd niet aangeboden aan de reguliere groep studenten.

Gegeven is de volgende constructie:

```{figure} intro_data/structure.svg
:align: center
```

:::::{exercise}
:label: exam_stat_indet_2025_1
:nonumber: true

Laat zien dat deze constructie enkelvoudig statisch onbepaald is.
:::::

::::{admonition} Solution
:class: solution, dropdown


```{figure} intro_data/stat_deter.svg
:align: center
```

Voor deze constructie is de inwendige statisch onbepaaldheid gelijk aan de uitwendig statisch onbepaaldheid.

Er zijn 8 onbekenden en 6 evenwichtsvergelijkingen, waarmee is de constructie enkelvoudig statisch onbepaald.

**Constructie niet uit elkaar in scharniende delen**

```{figure} exam_data/niet-uit-elkaar.svg
:align: center
```


::::

:::::{exercise}
:label: exam_stat_indet_2025_2
:nonumber: true

Geef twee geldige varianten om deze constructie statisch bepaald te maken ten behoeve van de krachtenmethode of verplaatsingenmethode met statisch onbepaalde verplaatsingen. Zorg voor twee verschillende varianten: je aanpassingen moeten elk een ander onderdeel van de constructie aanpassen.
Geef bij elk van de varianten de benodigde vergelijking(en) om de statisch onbepaalde kracht(en) of statisch onbepaalde verplaatsing(en) mee te kunnen bepalen.


:::::

::::{admonition} Oplossing
:class: solution, dropdown

Een scharnier toevoegen in hetzelfde segment of een pendelstaaf loshalen in hetzelfde segment telt niet als een geldige variant.

Een aantal mogelijk opties zijn

```{figure} ./intro_data/SB1.svg
:align: center
```

```{figure} ./intro_data/SB2.svg
:align: center
```

::::

:::::{exercise}
:label: exam_stat_indet_2025_3
:nonumber: true

Bepaal de verticale oplegreactie in $\rm{A}$ met behulp van de krachtenmethode of verplaatsingenmethode.

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Als voorbeeld is de krachtenmethode toegepast met het volgende statisch bepaalde system bekeken, maar andere methodes zijn ook goed:

```{figure} ./intro_data/SB3.svg
:align: center
```

De temperatuursinvloed kan worden meegenomen met een kinematisch equivalente belasting op $\rm{ADC}$:

$$ M^{\rm{T}} = 7875 \cdot 10^{-5} \cdot \cfrac{37.5}{0.25} = 11.8125 \ \rm{kNm}$$

Deze moet worden aangebracht op beide uiteindes van $\rm{ADC}$ om tot een constante kromming te komen.

```{figure} ./intro_data/temp.svg
:align: center
```

De verlenging van $\rm{BD}$ kan nu gevonden worden met de verlenging van een staaf:

```{figure} ./intro_data/BD.svg
:align: center
```

$$ \Delta L_{\rm{BD}} = \cfrac{N^{\rm{BD}} \cdot 5}{2000} = \cfrac{N^{\rm{BD}}}{400} = 0.0025 N^{\rm{BD}}$$

De verplaatsing $w_{\rm{D}}^{\rm{BD}}$ kan nu worden gevonden met williot:

```{figure} ./intro_data/Williot.svg
:align: center
```

$$ w_{\rm{D}}^{\rm{BD}} = -\cfrac{N^{\rm{BD}}}{400} \cdot \cfrac{5}{4} = -\cfrac{N^{\rm{BD}}}{320} = -0.003125 N^{\rm{BD}} $$

De verplaatsing $w_{\rm{D}}^{\rm{ADC}}$ en rotatie $\varphi_{\rm{A}}$ kan nu worden gevonden met vergeet-me-nietjes:

```{figure} ./intro_data/ADC.svg
:align: center
```

$$
\begin{align*}
w_{\rm{D}}^{\rm{ADC}} &= \cfrac{M_{\rm{A}} \cdot 6^2}{16 \cdot 7875} - 2\cdot \cfrac{11.8125 ^2}{16 \cdot 7875} + \cfrac{N^{\rm{BD}} \cdot \cfrac{4}{5} \cdot 6^3}{48 \cdot 7875} \\
w_{\rm{D}}^{\rm{ADC}} &= \cfrac{M_{\rm{A}}}{3500} + \cfrac{2 \cdot N^{\rm{BD}}}{4375} - \cfrac{27}{4000}\\
w_{\rm{D}}^{\rm{ADC}} &\approx 0.0002857 M_{\rm{A}} + 0.0004571 N^{\rm{BD}} - 0.00675 \\
\varphi_{\rm{A}} &= \cfrac{M_{\rm{A}} \cdot 6}{3 \cdot 7875} - \cfrac{11.8125 \cdot 6}{6 \cdot 7875} - \cfrac{11.8125 \cdot 6}{3 \cdot 7875} + \cfrac{N^{\rm{BD}} \cdot \cfrac{4}{5} \cdot 6^2}{16 \cdot 7875} \\
\varphi_{\rm{A}} &= \cfrac{M_{\rm{A}} \cdot 2}{7875} + \cfrac{N^{\rm{BD}}}{4375} - \cfrac{9}{2000}\\
\varphi_{\rm{A}} &\approx 0.000254 M_{\rm{A}} + 0.0002286 N^{\rm{BD}} - 0.0045
\end{align*}
$$

Solving for the displacement conditions gives:

$$
\left\{
\begin{matrix}
{w_{\rm{D}}^{\rm{ADC}}=w_{\rm{D}}^{\rm{BD}}} \\
{\varphi_{\rm{A}}=0}
\end{matrix}
\right.
\;\to\;
\begin{matrix}
{M_{\rm{A}} = \cfrac{13671}{800} = 17.08875 \ \rm{kNm}} \\
{N_{\rm{BD}} = 0.7 \ \rm{kN}}
\end{matrix}
$$

De verticale oplegreactie in $\rm{A}$ kan nu worden gevonden met evenwichtsvergelijkingen:

```{figure} ./intro_data/Av.svg
:align: center
```

$$
\sum \left. T \right|_{\rm{C}}^{\rm{ADC}} = 0 \to A_{\rm{v}} = -\cfrac{4109}{1600} = -2.568125 \ \rm{kN} \left(\downarrow\right)
$$

::::