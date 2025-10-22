# 15 september: TOZ

Gegeven is de volgende enkelvoudig statisch onbepaalde constructie:

```{figure} opgave_data/structure.svg
:align: center
```

:::::{exercise}
:label: TOZ_1
:nonumber: true

Welke van de volgende opties is geschikt om met de krachtenmethode de constructie door te rekenen?

- De inklemming bij $\rm{A}$ vervangen door een scharnier met een statisch onbepaald moment, met bijpassende vormveranderingsvoorwaarde
- Staaf $\rm{BD}$ splitsen en een statisch onbepaald normaalkrachtenpaar toevoegen, met bijpassende vormveranderingsvoorwaarde
- Staaf $\rm{CG}$ splitsen en een statisch onbepaald normaalkrachtenpaar toevoegen, met bijpassende vormveranderingsvoorwaarde
- Scharnier toevoegen tussen $\rm{A}$ en $\rm{D}$ met een statisch onbepaald momentenpaar, met bijpassende vormveranderingsvoorwaarde
- Scharnier toevoegen tussen $\rm{D}$ en $\rm{E}$ met een statisch onbepaald momentenpaar, met bijpassende vormveranderingsvoorwaarde
- Scharnier toevoegen tussen $\rm{E}$ en $\rm{G}$ met een statisch onbepaald momentenpaar, met bijpassende vormveranderingsvoorwaarde
- Scharnieroplegging bij $\rm{C}$ vervangen door een verticaal rolscharnier met een statisch onbepaald verticale kracht, met bijpassende vormveranderingsvoorwaarde

:::::

::::{solution} TOZ_1
:class: dropdown

```{figure} opgave_data/SB1.svg
:align: center
```

Er zijn 7 onbekende oplegreacties en 6 onbekende verbindingskrachten. Dat geeft een uitwendige graad van statisch onbepaaldheid van 1. Omdat deze constructie niet gesloten is, is de inwendige graad van statisch onbepaaldheid ook gelijk aan 1.

- De inklemming bij $\rm{A}$ vervangen door een scharnier met een statisch onbepaald moment, met bijpassende vormveranderingsvoorwaarde

    ```{figure} opgave_data/optie1.svg
    ---
    align: center
    ---
    ```

    Deze constructie is geen mechanisme dus een geschikte statisch bepaalde constructie.

- Staaf $\rm{BD}$ splitsen en een statisch onbepaald normaalkrachtenpaar toevoegen, met bijpassende vormveranderingsvoorwaarde

    ```{figure} opgave_data/optie2.svg
    ---
    align: center
    ---
    ```

    Deze constructie is geen mechanisme dus een geschikte statisch bepaalde constructie.

- Staaf $\rm{CG}$ splitsen en een statisch onbepaald normaalkrachtenpaar toevoegen, met bijpassende vormveranderingsvoorwaarde

    ```{figure} opgave_data/optie3.svg
    ---
    align: center
    ---
    ```

    Deze constructie is een mechanisme dus geen geschikte statisch bepaalde constructie.

- Scharnier toevoegen tussen $\rm{A}$ en $\rm{D}$ met een statisch onbepaald momentenpaar, met bijpassende vormveranderingsvoorwaarde

    ```{figure} opgave_data/optie4.svg
    ---
    align: center
    ---
    ```

    Deze constructie is geen mechanisme dus een geschikte statisch bepaalde constructie.

- Scharnier toevoegen tussen $\rm{D}$ en $\rm{E}$ met een statisch onbepaald momentenpaar, met bijpassende vormveranderingsvoorwaarde

    ```{figure} opgave_data/optie5.svg
    ---
    align: center
    ---
    ```

    Deze constructie is een mechanisme dus geen geschikte statisch bepaalde constructie.

- Scharnier toevoegen tussen $\rm{E}$ en $\rm{G}$ met een statisch onbepaald momentenpaar, met bijpassende vormveranderingsvoorwaarde

    ```{figure} opgave_data/optie6.svg
    ---
    align: center
    ---
    ```

    Deze constructie is een mechanisme dus geen geschikte statisch bepaalde constructie.

- Scharnieroplegging bij $\rm{C}$ vervangen door een verticaal rolscharnier met een statisch onbepaald verticale kracht, met bijpassende vormveranderingsvoorwaarde

    ```{figure} opgave_data/optie7.svg
    ---
    align: center
    ---
    ```
    
    Deze constructie is een mechanisme dus geen geschikte statisch bepaalde constructie.

::::

Gekozen wordt voor het volgende statisch bepaalde systeem:

```{figure} opgave_data/stat_b.svg
:align: center
```

:::::{exercise}
:label: TOZ_2
:nonumber: true

Wat is de normaalkracht in $\rm{BD}$ als functie van $B_{\rm{v}}$?

:::::

::::{solution} TOZ_2
:class: dropdown

```{figure} opgave_data/BD.svg
:align: center
```

$$
\begin{align}
\sum F_{\rm{v}}^{\rm{BD}} &= 0 \\
B_{\rm{v}} + N_{\rm{BD}}&= 0 \\
N_{\rm{BD}} &= -B_{\rm{v}}
\end{align}
$$

:::::

:::::{exercise}
:label: TOZ_3
:nonumber: true

Wat is de normaalkracht in $\rm{CG}$ als functie van $B_{\rm{v}}$?

:::::

::::{solution} TOZ_3
:class: dropdown

```{figure} opgave_data/CG_1.svg
:align: center
```

$$
\begin{align}
\sum \left. T \right|_{\rm{E}}^{\rm{EG}} &= 0 \\
84 \cdot 4 - N_{\rm{CG}} \cdot 8 &= 0 \\
N_{\rm{CG}} &= 42 \ \rm{kN}
\end{align}
$$

::::

:::::{exercise}
:label: TOZ_4
:nonumber: true

Wat is de dwarskracht net links van $\rm{D}$ als functie van $B_{\rm{v}}$ is gelijk aan?

:::::

::::{solution} TOZ_4
:class: dropdown

```{figure} opgave_data/DG_1.svg
:align: center
```

$$
\begin{align}
\sum F_{\rm{v}}^{\rm{DG}} &= 0 \\
V_{\rm{D}}^{\rm{AD}}-B_{\rm{v}} - 84 + 42 &= 0 \\
V_{\rm{D}}^{\rm{AD}} &= B_{\rm{v}} + 42
\end{align}
$$

::::

:::::{exercise}
:label: TOZ_5
:nonumber: true

Wat is het moment in $\rm{D}$ als functie van $B_{\rm{v}}$ is gelijk aan?

:::::

::::{solution} TOZ_5
:class: dropdown

```{figure} opgave_data/DG_2.svg
:align: center
```

$$
\begin{align}
\sum \left. T \right|_{\rm{D}}^{\rm{DG}} &= 0 \\
M_{\rm{D}} + 84 \cdot 8 - 42 \cdot 12 &= 0 \\
M_{\rm{D}} &= -168 \ \rm{kNm}
\end{align}
$$
::::

:::::{exercise}
:label: TOZ_6
:nonumber: true

Wat is de zakking in $\rm{D}$ als functie van $B_{\rm{v}}$?

:::::

::::{solution} TOZ_6
:class: dropdown

De verplaatsing in $\rm{D}$ volgt uit een vergeet-me-nietje:

```{figure} ./opgave_data/AD.svg
:align: center
```

$$
\begin{align}
w_{\rm{D}} &= \cfrac{168 \cdot 4^2}{2 \cdot 64000} + \cfrac{\left( B_{\rm{v}} + 42 \right) \cdot 4^3}{3 \cdot 64000} \\
w_{\rm{D}} &= \cfrac{1}{3000} \cdot B_{\rm{v}} + 0.035 \\
w_{\rm{D}} & \approx 0.000333 \cdot B_{\rm{v}} + 0.035
\end{align}
$$

::::

:::::{exercise}
:label: TOZ_7
:nonumber: true

Wat is $B_{\rm{v}}$?

:::::

::::{solution} TOZ_7
:class: dropdown

De verplaatsing van $\rm{B}$ kan worden gevonden met de verlenging van een staaf door axiale krachten:

```{figure} ./opgave_data/wB.svg
:align: center
```

$$
\begin{align}
w_{\rm{B}} &= - w_{\rm{D}} - \Delta L_{\rm{BD}} \\
w_{\rm{B}} &= - w_{\rm{D}} -  \cfrac{-B_{\rm{v}} \cdot 8}{4000} \\
w_{\rm{B}} &= \cfrac{7}{3000} \cdot B_{\rm{v}} + 0.035 \\
w_{\rm{B}} & \approx 0.00233\cdot B_{\rm{v}} + 0.035 \\
\end{align}
$$

De vormveranderingsvoorwaarde geeft:

$$
\begin{align}
w_{\rm{B}} &= 0 \\
\cfrac{7}{3000} \cdot B_{\rm{v}} + 0.035 &= 0 \\
B_{\rm{v}} &= -15 \ \rm{kN}
\end{align}
$$

::::

:::::{exercise}
:label: TOZ_8
:nonumber: true

Wat is $w_{\rm{E}}$?

:::::

::::{solution} TOZ_8
:class: dropdown

De verplaatsing van $\rm{B}$ kan worden gevonden met de verlenging van een staaf door axiale krachten:

```{figure} ./opgave_data/wB.svg
:align: center
```

De verplaatsing van $\rm{D}$  volgt uit de eerder opgestelde formule. De rotatie van $\rm{D}$ volgt uit hetzelfde vergeet-me-nietje:

$$
\begin{align}
\varphi_{\rm{D}} &= \cfrac{168 \cdot 4}{64000} + \cfrac{\left( -15 + 42 \right) \cdot 4^2}{2 \cdot 64000} \\
\varphi_{\rm{D}} &= 0.03 \ \rm{rad}
\end{align}
$$

De dwarskracht in $\rm{DE}$ in $\rm{E}$ is gelijk aan:

```{figure} ./opgave_data/VE.svg
:align: center
```

$$
\begin{align}
\sum F_{\rm{v}}^{\rm{EG}} &= 0 \\
V_{\rm{E}}- 84 + 42 &= 0 \\
V_{\rm{E}} &= 42 \ \rm{kN}
\end{align}
$$

De verplaatsing van $\rm{E}$ volgt dan uit de verplaatsing van $\rm{D}$, het kwispeleffect door de rotatie van $\rm{D}$ en de extra verplaatsing door de dwarskracht in $\rm{E}$:

```{figure} ./opgave_data/we.svg
:align: center
```

$$
\begin{align}
w_{\rm{E}} &= w_{\rm{D}} + \varphi_{\rm{D}} \cdot 4 + \cfrac{ 42 \cdot 4^3}{3 \cdot 64000} \\
w_{\rm{E}} &= 0.0995 \ \rm{m} \\
\end{align}
$$

::::