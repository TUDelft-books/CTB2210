````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze pagina is aangepast van https://oit.tudelft.nl/CT1000/2025/week_7/session_1/intro.html

```
````

# Begeleide oefening 2: Verplaatsingenmethode met vrijheidsgraden en matrixmethode

Gegeven is de volgende constructie:

```{figure} ./lesoefening1_data/constructie2.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1

Constructie
```

## Verplaatsingenmethode met vrijheidsgraden

Alle verplaatsingen kunnen met vergeet-me-nietjes worden beschreven uitgedrukt in de rotatie van $\rm{D}$.

```{figure} ./lesoefening1_data/phi_D.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1

Vrijheidsgraad $\varphi_D$
```

:::::{exercise}
:nonumber: true

Gegeven zijn 6 vergeet-me-nietjes:

```{figure} ./lesoefening1_data/vergeet-me-nietjes.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden

Vergeet-me-nietjes
```

```{h5p} https://tudelft.h5p.com/content/1292762106526728237/embed
```

:::::

De constructie wordt gesplitst in $\rm{D}$. Daarmee kunnen we het vrijlichaamsschema van beide delen en knoop $\rm{D}$ tekenen.

```{figure} ./lesoefening1_data/VLS.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1

Vrijlichaamsschema's van drie delen en knoop $\rm{D}$
```

:::::{exercise}
:nonumber: true

Los $M_{\rm{D}}^{\rm{AD}}$, $M_{\rm{D}}^{\rm{CD}}$ en $M_{\rm{D}}^{\rm{BD}}$ op als functie $\varphi_{\rm{D}}$.

```{h5p} https://tudelft.h5p.com/content/1292762148247859927/embed
```

:::::

:::::{exercise}
:nonumber: true

Los $\varphi_{\rm{D}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292762149380367767/embed
```

:::::

## Matrixmethode

```{figure} ./lesoefening1_data/constructie2.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1

Constructie
```

Gegeven is $\mathbf{u} = \begin{bmatrix} \varphi_{\rm{A}} & \varphi_{\rm{B}} & \varphi_{\rm{C}} & \varphi_{\rm{D}} \end{bmatrix}^T$.

:::::{exercise}
:nonumber: true

Bepaal de elementstijfheidsmatrix $\mathbf{K}$ voor element $\rm{AD}$ en $\rm{CD}$.

```{h5p} https://tudelft.h5p.com/content/1292762152044946837/embed
```

:::::

:::::{exercise}
:nonumber: true

Bepaal de elementstijfheidsmatrix $\mathbf{K}$ voor element $\rm{BD}$.

```{h5p} https://tudelft.h5p.com/content/1292762153223022427/embed
```

:::::

:::::{exercise}
:nonumber: true

Bepaal de globale stijfheidsmatrix $\mathbf{K}$.

```{h5p} https://tudelft.h5p.com/content/1292762154021337797/embed
```

:::::

:::::{exercise}
:nonumber: true

Bepaal de krachtvector $\mathbf{F}$.

```{h5p} https://tudelft.h5p.com/content/1292762155602115137/embed
```

:::::

:::::{exercise}
:nonumber: true

Bepaal de waarde van de vrijheidsgraden $\varphi_{\rm{B}}$, $\varphi_{\rm{C}}$ en $\varphi_{\rm{D}}$.

```{h5p} https://tudelft.h5p.com/content/1292762156953327747/embed
```

:::::