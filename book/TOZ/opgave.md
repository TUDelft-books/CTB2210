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

```{figure} opgave_data/SB.svg
:align: center
```

:::::{exercise}
:label: TOZ_2
:nonumber: true

Wat is de normaalkracht in $\rm{BD}$ als functie van $B_{\rm{v}}$? Ga uit van $\rm{kN}$ en $\rm{m}$ voor de eenheden.

:::::

::::{solution} TOZ_2
:class: dropdown

```{figure} opgave_data/N_BD_berekenen.svg
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

Wat is de normaalkracht in $\rm{CG}$ als functie van $B_{\rm{v}}$? Ga uit van $\rm{kN}$ en $\rm{m}$ voor de eenheden.

:::::

::::{solution} TOZ_3
:class: dropdown

```{figure} opgave_data/N_CG_berekenen.svg
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