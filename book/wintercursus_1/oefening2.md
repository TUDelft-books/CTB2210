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

:::::::{admonition} Oplossing
:class: solution, dropdown

Punt $\rm{D}$ blijft op z'n plek, dus kan gezien worden als oplegging die niet verplaatst.

:::::::

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

:::::::{admonition} Oplossing
:class: solution, dropdown

Voor deel $\rm{AB}$ kan een statisch onbepaalde vergeet-me-nietje worden gebruikt om de rotatie van $\rm{D}$ als functie van het moment $M_{\rm{D}}^{\rm{AD}}$ te vinden:

```{figure} lesoefening1_data/AD.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1
```

$$
\varphi_{\rm{D}} = \cfrac{M_{\rm{D}}^{\rm{AD}} \cdot 5}{4 \cdot 120000} = \cfrac{M_{\rm{D}}^{\rm{AD}}}{96000}
$$

Omschrijven van deze relatie geeft:

$$
M_{\rm{D}}^{\rm{AD}} = 96000 \cdot \varphi_{\rm{D}}
$$

Voor deel $\rm{CD}$ kan een statisch bepaalde vergeet-me-nietje worden gebruikt:


```{figure} lesoefening1_data/CD2.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1
```

$$
\varphi_{\rm{D}} = -\cfrac{M_{\rm{D}}^{\rm{CD}} \cdot 5}{3 \cdot 120000} = -\cfrac{M_{\rm{D}}^{\rm{CD}}}{72000}
$$

Omschrijven van deze relatie geeft:

$$
M_{\rm{D}}^{\rm{CD}} = -72000 \cdot \varphi_{\rm{D}}
$$

Tot slot, voor deel $\rm{DB}$ kan hetzelfde statisch bepaalde vergeet-me-nietje worden gebruikt:

```{figure} lesoefening1_data/BD2.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1
```

$$
\varphi_{\rm{D}} = - \cfrac{M_{\rm{D}}^{\rm{BD}} \cdot 2}{3 \cdot 120000} - \cfrac{29 \cdot 2}{6 \cdot 120000} = -\cfrac{M_{\rm{D}}^{\rm{BD}}}{180000} - \cfrac{29}{360000}
$$

Omschrijven van deze relatie geeft:
$$
M_{\rm{D}}^{\rm{BD}} = -180000 \cdot \varphi_{\rm{D}} - 14.5
$$

:::::::

:::::{exercise}
:nonumber: true

Los $\varphi_{\rm{D}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292762149380367767/embed
```

:::::

:::::::{admonition} Oplossing
:class: solution, dropdown

Het momentenevenwicht in knoop $\rm{D}$ geeft:

```{figure} lesoefening1_data/D.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1
```

$$
\begin{align*}
M_{\rm{D}}^{\rm{AD}} - M_{\rm{D}}^{\rm{CD}} - M_{\rm{D}}^{\rm{BD}} + 29 &= 0 \\
\varphi_{\rm{D}} &= \cfrac{-1}{8000} \approx -1.25 \cdot 10^{-4} \ \rm{rad}
\end{align*}
$$

:::::::

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

:::::::{admonition} Oplossing
:class: solution, dropdown

De stijheidsmatrix is definiëerd als $\mathbf{K^{\rm{(e)}}} = \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2EI}{L} \\ \cfrac{2EI}{L} & \cfrac{4EI}{L}  \end{bmatrix}$. Dit geeft:


$$
\mathbf{K^{\rm{AD}}} = \mathbf{K^{\rm{AD}}} = \begin{bmatrix} \cfrac{4 \cdot 120000}{5} & \cfrac{2 \cdot 120000}{5} \\ \cfrac{2 \cdot 120000}{5} & \cfrac{4 \cdot 120000}{5}  \end{bmatrix} = \begin{bmatrix} 96000 & 48000 \\ 48000 & 96000  \end{bmatrix}
$$

:::::::

:::::{exercise}
:nonumber: true

Bepaal de elementstijfheidsmatrix $\mathbf{K}$ voor element $\rm{BD}$.

```{h5p} https://tudelft.h5p.com/content/1292762153223022427/embed
```

:::::

:::::::{admonition} Oplossing
:class: solution, dropdown

$$
\mathbf{K^{\rm{BD}}} = \begin{bmatrix} \cfrac{4 \cdot 120000}{2} & \cfrac{2 \cdot 120000}{2} \\ \cfrac{2 \cdot 120000}{2} & \cfrac{4 \cdot 120000}{2}  \end{bmatrix} = \begin{bmatrix} 240000 & 120000 \\ 120000 & 240000  \end{bmatrix}
$$

:::::::

:::::{exercise}
:nonumber: true

Bepaal de globale stijfheidsmatrix $\mathbf{K}$.

```{h5p} https://tudelft.h5p.com/content/1292762154021337797/embed
```

:::::

:::::::{admonition} Oplossing
:class: solution, dropdown

Alle stijfheidsmatrices kunnen worden samengevoegd in de globale stijfheidsmatrix $\mathbf{K}$.  Hierbij worden de kolommen en rijen gekoppeld aan de juiste vrijheidsgraden. We beginnen met element $\rm{AD}$, dat knopen $\rm{A}$ en $\rm{D}$ koppelt (rij en kolom 1 en 4):

$$
\mathbf{K} = 
\begin{bmatrix}
96000 & 0 & 0 & 48000\\
0 & 0 & 0 & 0\\
0 & 0 & 0 & 0\\
48000 & 0 & 0 & 96000\\
\end{bmatrix}
$$

Nu voegen we het tweede element $\rm{CD}$ toe, dat knopen $\rm{C}$ en $\rm{D}$ koppelt (rij en kolom 3 en 4):

$$
\mathbf{K} =
\begin{bmatrix}
96000 & 0 & 0 & 48000\\
0 & 0 & 0 & 0\\
0 & 0 & 96000 & 48000\\
48000 & 0 & 48000 & 192000\\
\end{bmatrix}
$$

Tot slot voegen we het derde element $\rm{BD}$ toe, dat knopen $\rm{B}$ en $\rm{D}$ koppelt (rij en kolom 2 en 4):

$$
\mathbf{K} =
\begin{bmatrix}
96000 & 0 & 0 & 48000\\
0 & 240000 & 0 & 120000\\
0 & 0 & 96000 & 48000\\
48000 & 120000 & 48000 & 432000\\
\end{bmatrix}
$$

:::::::

:::::{exercise}
:nonumber: true

Bepaal de krachtvector $\mathbf{F}$.

```{h5p} https://tudelft.h5p.com/content/1292762155602115137/embed
```

:::::

:::::::{admonition} Oplossing
:class: solution, dropdown
Now, the force vector can be defined. First the external forces are added:

$$
\mathbf{f} =
\begin{bmatrix}
0 \\
29 \\
0 \\
-29
\end{bmatrix}
$$

Vervolgens worden de opleggingen toegevoegd. De oplegging bij $\rm{A}$ levert een moment op van $M_{\rm{A}}$. Dit geeft de volgende krachtvector:

$$
\mathbf{f} =
\begin{bmatrix}
M_{\rm{A}} \\
29 \\
0 \\
-29
\end{bmatrix}
$$

:::::::

:::::{exercise}
:nonumber: true

Bepaal de waarde van de vrijheidsgraden $\varphi_{\rm{A}}$, $\varphi_{\rm{B}}$, $\varphi_{\rm{C}}$ en $\varphi_{\rm{D}}$.

```{h5p} https://tudelft.h5p.com/content/1292762156953327747/embed
```

:::::

:::::::{admonition} Oplossing
:class: solution, dropdown

Het hele systeem kan nu worden opgelost met de volgende vergelijking:
$$
\begin{bmatrix}
96000 & 0 & 0 & 48000\\
0 & 240000 & 0 & 120000\\
0 & 0 & 96000 & 48000\\
48000 & 120000 & 48000 & 432000\\
\end{bmatrix}
\begin{bmatrix}
0 \\
\varphi_{\rm{B}} \\
\varphi_{\rm{C}} \\
\varphi_{\rm{D}}
\end{bmatrix}
=
\begin{bmatrix}
M_{\rm{A}} \\
29 \\
0 \\
-29
\end{bmatrix}
$$

Om de onbekende rotaties op te lossen, kan de eerste rij en kolom worden verwijderd:

$$
\begin{bmatrix}
240000 & 0 & 120000\\
0 & 96000 & 48000\\
120000 & 48000 & 432000\\
\end{bmatrix}
\begin{bmatrix}
\varphi_{\rm{B}} \\
\varphi_{\rm{C}} \\
\varphi_{\rm{D}}
\end{bmatrix}
=
\begin{bmatrix}
29 \\
0 \\
-29
\end{bmatrix}
$$

Dit geeft:

$$
\begin{bmatrix}
\varphi_{\rm{B}} \\
\varphi_{\rm{C}} \\
\varphi_{\rm{D}}
\end{bmatrix}
=
\begin{bmatrix}
\cfrac{7}{19200} \\
\cfrac{1}{16000} \\
\cfrac{-1}{8000}
\end{bmatrix}
\approx
\begin{bmatrix}
3.65 \cdot 10^{-4} \\
6.25 \cdot 10^{-5} \\
-1.25 \cdot 10^{-4}
\end{bmatrix}
$$

:::::::
