# Begeleid oefenen

Nu gaan we aan de slag met een oefening.

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze oefening is aangepast van https://github.com/TUDelft-books/CEG-mechanics-BSc versie CTB2210-2025.
```
````

## Oefening 1

Gegeven is de volgende constructie:

```{figure} ../_git/github.com_TUDelft-books_CEG-mechanics-BSc/CTB2210-2025/book/statically_inderminate/force_method/bending_data/Example.svg
:align: center

Constructie
```

Bepaal de krachtsverdeling en verplaatsingen.

:::::{exercise}
:label: balk_1_1
:nonumber: true

Ga uit van het volgende statisch bepaalde systeem:

```{figure} ../_git/github.com_TUDelft-books_CEG-mechanics-BSc/CTB2210-2025/book/statically_inderminate/force_method/bending_data/SB-systeem2.svg
:align: center

Statisch bepaalde constructie met vormveranderingsvoorwaarde
```

Los de krachtsverdeling en verplaatsingen van deze constructie op als functie van $A_{\rm{v}}$

```{h5p} https://tudelft.h5p.com/content/1292636025372301087/embed
```

:::::

% solution_start

::::{solution} balk_1_1
:class: dropdown

```{figure} lesoefeningen_data/VrijlichaamsschemaBC.svg
---
align: center
---
Vrijlichaamsschema van deel BC
```
$$ M_{\rm{B}} \left( A_{\rm{v}} \right) = 4 \cdot A_{\rm{v}} -200 $$

De hoekverdraaiing bij B, $\varphi_{\rm{B}}$, kan worden bepaald uit $M_{\rm{B}}$ met behulp van het vergeet-mij-nietje voor een ligger op twee steunpunten belast door een koppel.

$$ \varphi_{\rm{B}} \left( A_{\rm{v}} \right) = \cfrac{1}{3} \cdot \cfrac{\(4 \cdot A_{\rm{v}} -200\) \cdot6}{\cfrac{16}{3} \cdot 10^3} = 0.0015 \cdot A_{\rm{v}} -0.0750 $$

De zakking in A, $w_{\rm{A}}$, kan worden bepaald door deel AB bij B schuin in te klemmen met hoek \varphi_{\rm{B}} en de zakkingen ten gevolge van de verdeelde belasting en $A_{\rm{v}} in rekening te brengen. Hiervoor worden het vergeet-mij-nietje voor een uitkragende ligger met een verdeelde belasting en het vergeet-mij-nietje voor een uitkragende ligger belast door een puntlast gebruikt:

$$ w_{\rm{A}} \left( A_{\rm{v}} \right) = \varphi_{\rm{B}} \cdot 4 - \cfrac{25 \cdot 4^4}{8 \cdot \cfrac{16}{3} \cdot 10^3} + \cfrac{A_{\rm{v}} \cdot 4^3}{3 \cdot \cfrac{16}{3} \cdot 10^3}  =0.01 \cdot A_{\rm{v}} -0.45 $$

::::

% solution_end

:::::{exercise}
:label: balk_1_2
:nonumber: true

Los de vormveranderingsvoorwaarde op om $A_{\rm{v}}$ te vinden.

```{h5p} https://tudelft.h5p.com/content/1292636567761480237/embed
```

:::::

% solution_start

::::{solution} balk_1_2
:class: dropdown

De vormveranderingsvoorwaarde is: $w_{\rm{A}} = 0.01 \cdot A_{\rm{v}} -0.45 = 0$. 

Hieruit volgt $A_{\rm{v}} = 45 \rm{kN}$

::::

% solution_end

:::::{exercise}
:label: balk_1_3
:nonumber: true

Los nu de andere oplegreacties op en bepaal de momenten en verplaatsingen.

```{h5p} https://tudelft.h5p.com/content/1292636572692927547/embed
```

:::::

% solution_start

::::{solution} balk_1_3
:class: dropdown

Nu $A_{\rm{v}}$ bekend is kunnen de andere oplegreacties worden opgelost, $B_{\rm{v}}$ en $C_{\rm{v}}$ worden omhoog positief aangenomen. De gebruikte vergelijkingen zijn:

$$ \sum \left. T \right|  _ {\rm{C}} = -45 \cdot 10 + 25 \cdot 4 \cdot 8 - B_{\rm{v}} \cdot 6 = 0 \rightarrow B_{\rm{v}} = 58.3 \rm{kN} $$ 

$$ \sum F_ {\rm{v}} = 45 - 4 \cdot 25 + 58.3 + C_{\rm{v}} = 0 \rightarrow C_{\rm{v}} = -3.3 \rm{kN} $$

$M_{\rm{B}}$ kan worden bepaald uit de momentensom om B van deel AB, dit geeft: $M_{\rm{B}} = - 20 \rm{kNm}$. $M_{\rm{halverwege \ AB}}$ kan op vergelijkbare wijze worden bepaald uit de momentensom om het punt halverwege AB: $M_{\rm{halverwege \ AB}} = 40 \rm{kNm}$. 

De zakking halverwege AB, $w_{\rm{halverwege} \ \rm{AB}}$, kan op verschillende manieren worden gevonden. Hier wordt deze bepaald met behulp van het het vergeet-mij-nietje voor een ligger op twee steunpunten belast door een koppel en het vergeet-mij-nietje voor een ligger op twee steunpunten met een verdeelde belasting. 

$$ w_{\rm{halverwege \ AB}} = \cfrac{5}{384} \cdot \cfrac{25 \cdot 4^4}{\cfrac{16}{3}} - \cfrac{1}{16} \cdot \cfrac{20 \cdot 4^2}{\cfrac{16}{3}} = 12 \rm{mm} $$

De zakking halverwege BC kan worden bepaald met behulp van het vergeet-mij-nietje voor een ligger op twee steunpunten belast door een koppel:

$$ w_{\rm{halverwege \ BC}} =  - \cfrac{1}{16} \cdot \cfrac{20 \cdot 6^2}{\cfrac{16}{3}} = -8 \rm{mm} $$

::::

% solution_end

## Oefening 2

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

:::::{exercise}
:label: balk_2_4
:nonumber: true

Los je vormveranderingsvoorwaarde op om $B_{\rm{v}}$ te vinden.

```{h5p} https://tudelft.h5p.com/content/1292642094940904187/embed
```

:::::

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

:::::{exercise}
:label: balk_2_6
:nonumber: true

Los je vormveranderingsvoorwaarde op om $M_{\rm{C}}$ te vinden.

```{h5p} https://tudelft.h5p.com/content/1292642615022517117/embed
```

:::::

### Krachtsverdeling en verplaatsingen statisch onbepaald systeem

:::::{exercise}
:label: balk_2_7
:nonumber: true

Los nu de volledige krachtsverdeling en verplaatsingen op met de resultaten van een of beide van je statisch onbepaalde systemen.

```{h5p} https://tudelft.h5p.com/content/1292642621332227027/embed
```

:::::
