# Begeleide oefening 2

Gegeven is de volgende constructie:

```{figure} ./lesoefening_data/structure.svg
:align: center

Constructie
```

We gaan deze constructie doorrekenen met behulp van differentiaalvergelijkingen

:::::{exercise}
:label: temp_2_1
:nonumber: true

Wat is $\kappa_{\rm{T}}$?

```{h5p} https://tudelft.h5p.com/content/1292671259091838977/embed
```

:::::

::::{solution} temp_2_1
:class: dropdown

$$\kappa^T = -\cfrac{\alpha \cdot T}{h} = - \cfrac{0.0001 \cdot 30}{0.2} = -0.015 \ m^{-1}$$

::::

:::::{exercise}
:label: temp_2_2
:nonumber: true

Bepaal met behulp van de differentiaalvergelijkingen de uitdrukkingen voor de snedekrachten en verplaatsingen. Merk op dat twee randvoorwaarden direct twee integratieconstantes geven.

```{h5p} https://tudelft.h5p.com/content/1292671251572754907/embed
```

:::::

::::{solution} temp_2_2
:class: dropdown
Voor deze constructie gelden den onderstaande randvoorwaarden:

$$ w \left( 0 \right) = 0 $$
$$ M \left( 0 \right) = +6 \rm{kNm} $$
$$ w \left( 8 \right) = 0 $$
$$ \varphi \left( 8 \right) = 0 $$

Hieruit volgt voor de snedekrachten en verplaatsingen:

$$ V\left( x  \right) = C_1 $$ 
$$ M\left( x  \right) = C_1 \cdot x + 6 $$
$$ \kappa \left( x \right) = \cfrac{M}{EI} = \cfrac{3}{800} \cdot C_1 \cdot x + \cfrac{6 \cdot 3}{800} - 0.015 = 0.00375 \cdot C_1 \cdot x + 0.0075 $$
$$ \varphi \left( x \right) = 0.001875  C_1 \cdot x^2 + 0.0075 \cdot x + C_3 $$
$$ w \left( x \right) = -0.000625 \cdot C_1 \cdot x^3 -0.00375 \cdot x^2 - C_3 \cdot x + 0 $$

::::

:::::{exercise}
:label: temp_2_3
:nonumber: true

Bepaal de waardes van de integratieconstantes

```{h5p} https://tudelft.h5p.com/content/1292671264027013177/embed
```

:::::

::::{solution} temp_2_3
:class: dropdown

$$ C_1 = -0.375 $$
$$ C_3 = -0.015 $$

::::

:::::{exercise}
:label: temp_2_4
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292671266355957267/embed
```

:::::

::::{solution} temp_2_4
:class: dropdown

Als de temperatuur verder toeneemt, dan wordt de absolute waarde van maximale verplaatsing eerst kleiner dan groter. 

::::

:::::{exercise}
:label: temp_2_5
:nonumber: true

Waar is het moment gelijk aan 0 en waar is het buigpunt?

...

Wat ken je zeggen over de locatie van deze twee punten.

...


:::::