# Oefenen

Nu gaan we aan de slag met een oefening.

Gegeven is de volgende constructie:

```{figure} lesoefeningen_data/structure.svg
---
align: center
---
Constructie
```

Bepaal de oplegreacties en het snedekrachtenlijnen. Je gaat dit doen voor drie verschillende statisch onbepaalde krachten.

:::::{exercise}
:label: km_vak_1_1
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292633373580570237/embed
```

:::::

% solution_start

::::{solution} km_vak_1_1
:class: dropdown

```{figure} lesoefeningen_data/onbekenden.svg
---
align: center
---
Er zijn 22 onbekende krachten
```

```{figure} lesoefeningen_data/vergelijkingen.svg
---
align: center
---
Er zijn 21 evenwichtsvergelijkingen
```

Dus de constructie is 1ste graads statisch onbepaald

::::

% solution_end

:::::{exercise}
:label: km_vak_1_2
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292633398746509087/embed
```

:::::

% solution_start

::::{solution} km_vak_1_2
:class: dropdown

- Weghalen oplegging bij A
- Weghalen oplegging bij B
  - Inderdaad! Als je de hele oplegging weghaalt heb je een mechanisme wat naar links en rechts kan bewegen!
- Weghalen oplegging bij C
- Toevoegen scharnier bij B (in doorgaande liggen DBEG)
- Toevoegen scharnier bij E (in doorgaande liggen DBEG)
  - Inderdaad, als je hier een scharnier toevoegt krijg je een mechanisme waarbij EG om E kan draaien
- Splitsen constructie in pendelstaaf AD
- Splitsen constructie in pendelstaaf CE

::::

% solution_end

## Statisch onbepaalde kracht $B_{\rm{v}}$

:::::{exercise}
:label: km_vak_1_3
:nonumber: true

Neem als statisch onbepaalde kracht de verticale oplegreactie bij B (positief omhoog).

```{h5p} https://tudelft.h5p.com/content/1292634255950574927/embed
```

:::::

% solution_start

::::{solution} km_vak_1_1
:class: dropdown

De vormveranderingsvoorwaarde is $w_B = 0$.

::::

% solution_end

:::::{exercise}
:label: km_vak_1_4
:nonumber: true

Bepaal achtereenvolgens de normaalkrachten en verplaatsingen als functie van $B_{\rm{v}}$.

```{h5p} https://tudelft.h5p.com/content/1292634246594651717/embed
```

:::::

% solution_start

::::{solution} km_vak_1_1
:class: dropdown

```{figure} lesoefeningen_data/Vrijlichaamsschema1.svg
---
align: center
---

Vrijlichaamsschema met $B_{\rm{v}}$ als statisch onbepaalde.

```
De gebruikte vergelijkingen zijn:

$$ \sum M \textbar _ {\rm{E}} = 5 \cdot N_{\rm{AD}} - 2 \cdot B_{\rm{v}} - 3 \cdot F =0 $$ 
$$ \sum F _ {\rm{v}} = - N_{\rm{AD}} + B_{\rm{v}} + N_{\rm{CE}} - F = 0 $$
$$ w_{\rm{E}} = - \Delta l_{\rm{CE}} = \cfrac{-N_{\rm{CE}} \cdot l_{\rm{CE}}}{EA} $$
$$ w_{\rm{D}} = \Delta l_{\rm{AD}} = \cfrac{-N_{\rm{AD}} \cdot l_{\rm{AD}}}{EA} $$ 
$$ w_{\rm{B}} = w_{\rm{D}} + \cfrac{3}{5} \cdot \left( w_{\rm{E}} - w_{\rm{D}} \right) = \cfrac{3}{5} \cdot w_{\rm{E}} + \cfrac{2}{5} \cdot w_{\rm{D}} $$

Hieruit volgt:

$$ N_{\rm{AD}} = 0.4 \cdot B_{\rm{v}} + 15.6 $$
$$ N_{\rm{CE}} = - 0.6 \cdot B_{\rm{v}} + 41.6 $$
$$ w_{\rm{E}} = 0.0006 \cdot B_{\rm{v}} - 0.0416 $$
$$ w_{\rm{E}} = 0.0004 \cdot B_{\rm{v}} - 0.0156 $$
$$ w_{\rm{B}} = 0.00052 \cdot B_{\rm{v}} - 0.01872 $$

::::

% solution_end

:::::{exercise}
:label: km_vak_1_5
:nonumber: true

Los met de vormveranderingsvoorwaarde de statisch onbepaalde kracht $B_{\rm{v}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292634259801752997/embed
```

:::::

% solution_start

::::{solution} km_vak_1_1
:class: dropdown

Oplossen van de vergelijkingen geeft:

$$ B_{\rm{v}} = 36 \rm{kN} $$
$$ N_{\rm{AD}} = 30 \rm{kN} $$
$$ N_{\rm{CE}} = 20 \rm{kN} $$
$$ w_{\rm{E}} = -2 \rm{cm} $$
$$ w_{\rm{D}} = 3 \rm{cm} $$
$$ w_{\rm{B}} = 0 $$

::::

% solution_end

## Statisch onbepaald moment $M_{\rm{B}}$

:::::{exercise}
:label: km_vak_1_6
:nonumber: true

Neem als statisch onbepaalde kracht het moment $M_{\rm{B}}$ (positief zorgt voor trek aan de onderkant).

```{h5p} https://tudelft.h5p.com/content/1292634286050413117/embed
```

:::::

% solution_start

::::{solution} km_vak_1_1
:class: dropdown

De vormveranderingsvoorwaarde is: $ \rm{phi} _ {\rm{{B aan de kant van BD}}} = \rm{phi} _ {\rm{{B aan de kant van BE}}} $

::::

% solution_end


:::::{exercise}
:label: km_vak_1_7
:nonumber: true

Bepaal achtereenvolgens de normaalkrachten en verplaatsingen als functie van $M_{\rm{B}}$.

```{h5p} https://tudelft.h5p.com/content/1292634293341890027/embed
```

:::::

:::::{exercise}
:label: km_vak_1_8
:nonumber: true

Los met de vormveranderingsvoorwaarde de statisch onbepaalde kracht $M_{\rm{B}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292634306404351337/embed
```

:::::

## Statisch onbepaalde normaalkracht $N_{\rm{AD}}$

:::::{exercise}
:label: km_vak_1_9
:nonumber: true

Neem als statisch onbepaalde kracht de normaalkracht $N_{\rm{AD}}$ door de pendelstaaf in het scharnier los te maken van de balk.

```{h5p} https://tudelft.h5p.com/content/1292634312901581657/embed
```

:::::

:::::{exercise}
:label: km_vak_1_10
:nonumber: true

Bepaal achtereenvolgens de normaalkrachten en verplaatsingen als functie van $N_{\rm{AD}}$.

```{h5p} https://tudelft.h5p.com/content/1292634315769955647/embed
```

:::::

:::::{exercise}
:label: km_vak_1_11
:nonumber: true

Los met de vormveranderingsvoorwaarde de statisch onbepaalde kracht $N_{\rm{AD}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292634317462305007/embed
```

:::::
