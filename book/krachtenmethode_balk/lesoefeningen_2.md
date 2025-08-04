# Begeleide oefening 2

Gegeven is de volgende constructie

```{figure} ./lesoefeningen_data/structure.svg
:align: center

Constructie
```

Bepaal de krachtsverdeling en verplaatsingen.

:::::{exercise}
:label: balk_2_1
:nonumber: true

Wat is de graad van inwendig statisch onbepaaldheid?

```{h5p} https://tudelft.h5p.com/content/1292636677784672607/embed
```

:::::

::::{solution} balk_2_1
:class: dropdown

De constructie is *1*ste/de graads inwendig statisch onbepaald

::::

:::::{exercise}
:label: balk_2_2
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292636680849554767/embed
```

:::::

::::{solution} balk_2_2
:class: dropdown

- Weghalen verticale oplegging bij A
  - Inderdaad, er is geen vergeet-me-nietje die voor dat statisch bepaalde systeem de verplaatsingen geeft
- Toevoegen scharnier bij A
  - Inderdaad, er is geen vergeet-me-nietje die voor dat statisch bepaalde systeem de verplaatsingen geeft
- Toevoegen scharnier bij C
  - Er zijn wel degelijk vergeet-me-nietjes voor deze situatie, maar het rechter deel zal echter ook nog roteren rondom B
- Weghalen verticale oplegging bij B

::::

### Statisch bepaald systeem 1

:::::{exercise}
:label: balk_2_3
:nonumber: true

Ga uit van het volgende statisch bepaalde systeem:

```{figure} ./lesoefeningen_data/SB-1.svg
:align: center

Statisch bepaalde constructie met vormveranderingsvoorwaarde
```

Los de krachtsverdeling en verplaatsingen van deze constructie uit als functie van $B_{\rm{v}}$

```{h5p} https://tudelft.h5p.com/content/1292642090947945297/embed
```

:::::

% solution_start

::::{solution} balk_2_3
:class: dropdown

Met behulp van het gegeven vrijlichaamsschema kunnen de dwarskracht net links van C, het moment in C en de dwarskracht net links van B worden bepaald als functie van $B_{\rm{v}}$:

$$ V_{\rm{C}}^{\rm{AC}} \left( B_{\rm{v}} \right) = -1 \cdot B_{\rm{v}} + 54 $$
$$ M_{\rm{C}} \left( B_{\rm{v}} \right) = -3 \cdot B_{\rm{v}} $$ 
$$ V_{\rm{B}}^{\rm{BC}} \left( B_{\rm{v}} \right) = -1 \cdot B_{\rm{v}} $$

De zakking, $w_{\rm{C}}$, en rotatie, $\varphi_{\rm{C}}$, in C kunnen worden gevonden door de kracht $B_{\rm{v}}$ te verplaatsen van B naar C met toevoeging van een moment, zie het onderstaande vrijlichaamsschema:

```{figure} ./lesoefeningen_data/VrijlichaamsschemaAC_1.svg
:align: center

Vrijlichaamsschema van deel AC
```

Met behulp van de vergeet-mij-nietjes voor een uitkragende ligger belast door een kracht en een koppel wordt gevonden:

$$ w_{\rm{C}} \left( B_{\rm{v}} \right) = \cfrac{\left(54 - B_{\rm{v}} \right) \cdot 3^3}{3 \cdot 1800} - \cfrac{3 \cdot B_{\rm{v}} \cdot 3^2}{2 \cdot 1800} = -0.0125 \cdot B_{\rm{v}} + 0.27 $$
$$ \varphi_{\rm{C}} \left( B_{\rm{v}} \right) = \cfrac{\left(54 - B_{\rm{v}} \right) \cdot 3^2}{2 \cdot 1800} - \cfrac{3 \cdot B_{\rm{v}} \cdot 3}{1800} = -0.0075 \cdot B_{\rm{v}} + 0.135 $$

De zakking in B, $w_{\rm{B}}$, is dan gelijk aan:

$$ w_{\rm{B}} \left( B_{\rm{v}} \right) = w_{\rm{C}} + \varphi_{\rm{C}} \cdot 3 - \cfrac{B_{\rm{v}} \cdot 3^3}{3 \cdot 900} = -0.045 \cdot B_{\rm{v}} + 0.675 $$

::::

% solution_end

:::::{exercise}
:label: balk_2_4
:nonumber: true

Los je vormveranderingsvoorwaarde op om $B_{\rm{v}}$ te vinden.

```{h5p} https://tudelft.h5p.com/content/1292642094940904187/embed
```

:::::

% solution_start

::::{solution} balk_2_6
:class: dropdown

De vormveranderingsvoorwaarde is: $w_{\rm{B}} = -0.045 \cdot B_{\rm{v}} + 0.675 = 0$. 

Hieruit volgt dat $B_{\rm{v}} = 15 \rm{kN}$

::::

% solution_end

### Statisch bepaald systeem 2

:::::{exercise}
:label: balk_2_5
:nonumber: true

Ga nu uit van het volgende statisch bepaalde systeem:

```{figure} ./lesoefeningen_data/SB-2.svg
:align: center

Statisch bepaalde constructie met vormveranderingsvoorwaarde
```

Los de krachtsverdeling en verplaatsingen van deze constructie uit als functie van $M_{\rm{C}}$

```{h5p} https://tudelft.h5p.com/content/1292642608547530667/embed
```

:::::

% solution_start

::::{solution} balk_2_5
:class: dropdown

De uitdrukkingen voor $B_{\rm{v}}$ en $V_{\rm{C}}^{\rm{AC}}$ kunnen worden afgeleid uit evenwicht van het deel BC.

$$ \sum \left. T \right| _ {\rm{C}} ^{\rm{CB}} = - 3 \cdot B_{\rm{v}} - M_{\rm{C}} = 0 \rightarrow B_{\rm{v}} = - \cfrac{1}{3} \cdot M_{\rm{C}} $$
$$ V_{\rm{C}}^{\rm{AC}} = B_{\rm{v}} + 54 = - \cfrac{1}{3} \cdot M_{\rm{C}} + 54 $$

De rotatie net links van C, $\varphi_{\rm{C}}^{\rm{AC}}$, en de zakking in C $w_{\rm{C}}$ kunnen worden bepaald met de vergeet-mij-nietjes voor een uitkragende ligger belast door een koppel en door een puntlast, zie het onderstaande vrijlichaamsschema:

```{figure} ./lesoefeningen_data/VrijlichaamsschemaAC_2.svg
:align: center

Vrijlichaamsschema van deel AC
```

$$ \varphi_{\rm{C}}^{\rm{AC}} \left( M_{\rm{C}} \right) = - \cfrac{M_{\rm{C}} \cdot 3}{1800} + \cfrac{\left( - \cfrac{1}{3} \cdot M_{\rm{C}} + 54 \right) \cdot 3^2}{2 \cdot 1800} = -0.0025 \cdot M_{\rm{C}} + 0.135 $$

$$ w_{\rm{C}} \left( M_{\rm{C}} \right) = - \cfrac{M_{\rm{C}} \cdot 3^2}{2 \cdot 1800} + \cfrac{\left( - \cfrac{1}{3} \cdot M_{\rm{C}} + 54 \right) \cdot 3^3}{3 \cdot 1800} = -0.00417 \cdot M_{\rm{C}} + 0.27 $$

De rotatie net rechts van C, $\varphi_{\rm{C}}^{\rm{BC}}$, wordt veroorzaakt door buiging van deel BC ten gevolge van $M_{\rm{C}}$ en door de zakking in C, $w_{\rm{C}}$. De rotatie ten gevolge van de buiging kan worden bepaald met behulp van het vergeet-mij-nietje voor een ligger op twee steunpunten belast door een koppel. 

$$ \varphi_{\rm{C}}^{\rm{BC}} \left( M_{\rm{C}} \right) = - \cfrac{w_{\rm{C}}}{3} + \cfrac{M_{\rm{C}} \cdot 3}{3 \cdot 900} = 0.0025 \cdot M_{\rm{C}} -0.09 $$

::::

% solution_end

:::::{exercise}
:label: balk_2_6
:nonumber: true

Los je vormveranderingsvoorwaarde op om $M_{\rm{C}}$ te vinden.

```{h5p} https://tudelft.h5p.com/content/1292642615022517117/embed
```

:::::

% solution_start

::::{solution} balk_2_6
:class: dropdown

De vormveranderingsvoorwaarde is: $\varphi_{\rm{C}}^{\rm{AC}} = \varphi_{\rm{C}}^{\rm{BC}} \rightarrow -0.0025 \cdot M_{\rm{C}} + 0.135 = 0.0025 \cdot M_{\rm{C}} -0.09$. 

Hieruit volgt $M_{\rm{C}} = 45 \rm{kNm}$. 

::::

% solution_end

### Krachtsverdeling en verplaatsingen statisch onbepaald systeem

:::::{exercise}
:label: balk_2_7
:nonumber: true

Los nu de volledige krachtsverdeling en verplaatsingen op met de resultaten van een of beide van je statisch onbepaalde systemen.

```{h5p} https://tudelft.h5p.com/content/1292642621332227027/embed
```

:::::

% solution_start

::::{solution} balk_2_7
:class: dropdown

De onbekenden kunnen worden opgelost met verticaal- en momentenevenwicht van de hele constructie en met behulp van de eerder opgestelde vergelijkingen.

$$ A_{\rm{v}} = -39 \rm{kN} $$
$$ A_{\rm{m}} = 72 \rm{kNm} $$
$$ B_{\rm{v}} = -15 \rm{kN} $$
$$ M_{\rm{A}} = -72 \rm{kNm} $$ 
$$ M_{\rm{C}} = 45 \rm{kNm} $$
$$ V_{\rm{AC}} = 39 \rm{kN} $$
$$ V_{\rm{CB}} = -15 \rm{kN} $$
$$ w_{\rm{C}} = 82.5 \rm{mm} $$
$$ \varphi_{\rm{C}} = 0.0225 \rm{rad} $$ 

::::

% solution_end