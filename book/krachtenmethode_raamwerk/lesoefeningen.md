# Begeleid oefening 1

Gegeven is de volgende 1ste graads statisch onbepaalde constructie:

```{figure} ./lesoefeningen_data/oefening_1.svg
:align: center

Constructie
```

:::::{exercise}
:label: raam_1_1
:nonumber: true

Gegeven zijn de volgende statisch bepaalde systeem.

```{figure} ./lesoefeningen_data/statisch_bepaalde_systemen.svg
:align: center

Twee statisch bepaalde systemen
```

```{h5p} https://tudelft.h5p.com/content/1292652217804730007/embed
```

:::::

% solution_start

::::{solution} raam_1_1
:class: dropdown

- Met het koppel is het niet mogelijk verplaatsingen te berekenen.
- Er zijn geen vergeet-me-nietjes voor deze situatie.
  - Juist, de vorm van deze constructie als geheel én delen ervan zijn geen vergeet-me-nietjes. 
- Het is überhaupt niet mogelijk verplaatsingen te berekeningen.

::::

% solution_end

:::::{exercise}
:label: raam_1_2
:nonumber: true

Laten we de constructie oplossing met hoekveranderingsvergelijkingen, door een scharnier toe te voegen bij hoek $\rm{C}$. Daar werkt echter ook een uitwendig koppel. Het moment net links en onder $\rm{C}$ is dus niet gelijk aan elkaar. Als we het heel netjes zouden doen zouden we het scharnier net links of net onder het scharnier kunnen aanbrengen. Laten we de situatie bekijken met het scharnier net links van $\rm{C}$.

```{figure} ./lesoefeningen_data/scharnier_links_C.svg
:align: center

Statisch bepaald systeem met scharnier net links van $\rm{C}$
```

Gegeven is het vrijlichaamsschema van knoop $\rm{C}$:

```{figure} ./lesoefeningen_data/VLS_C_1.svg
:align: center

Vrijlichaamsschema van knoop $\rm{C}$ vergroot weergegeven
```

```{h5p} https://tudelft.h5p.com/content/1292652219570406177/embed
```

:::::

% solution_start

::::{solution} raam_1_2
:class: dropdown

$M _{\rm{C}} ^{\rm{BC}} \left( M _{\rm{C}} ^{\rm{AC}} \right) = M _{\rm{C}} ^{\rm{AC}} + 30$. 

::::

% solution_end

Om het gedoe met dat scharnier net links/net onder $\rm{C}$ te voorkomen kunnen we het scharnier ook direct in C plaatsen. Deze aanpak wordt aangeraden.

```{figure} ./lesoefeningen_data/scharnier_in_C.svg
:name: statisch_onbepaald_C
:align: center

Statisch bepaald systeem met scharnier in $\rm{C}$
```

Nadeel van deze aanpak is dat de locatie van het scharnier niet meer match met de momenten in het vrijlichaamsschema. Echter is de situatie praktisch ongewijzigd. Merk op dat de richtingen van de momenten in het vrijlichaamsschema van $\rm{C}$ omgedraaid zijn ten opzichte van de momenten in het statisch bepaalde systeem:

```{figure} ./lesoefeningen_data/VLS_C_2.svg
:align: center

Vrijlichaamsschema van knoop $\rm{C}$ vergroot weergegeven
```

:::::{exercise}
:label: raam_1_3
:nonumber: true

Ga uit van [het statisch bepaalde systeem met het scharnier in $\rm{C}$](statisch_onbepaald_C)?

```{h5p} https://tudelft.h5p.com/content/1292652221281662937/embed
```

:::::

% solution_start

::::{solution} raam_1_3
:class: dropdown

Er is 1 statisch onbepaald moment, omdat de twee verschillende momenten van elkaar afhankelijk zijn door het momentenevenwicht van knoop C.  

::::

% solution_end

:::::{exercise}
:label: raam_1_4
:nonumber: true

Los de verplaatsingen van deze constructie uit als functie van $M_{\rm{C}}^{\rm{AC}}$ en $M_{\rm{C}}^{\rm{BC}}$

```{h5p} https://tudelft.h5p.com/content/1292652223605026557/embed
```

:::::

% solution_start

::::{solution} raam_1_4
:class: dropdown

De uitdrukkingen voor de hoekverdraaiingen kunnen worden gevonden met behulp van het vergeet-mij-nietje voor een ligger op twee steunpunten belast door een koppel. 

$$ \varphi_{\rm{C}}^{\rm{AC}} \left( M_{\rm{C}}^{\rm{AC}} \right) = \cfrac{M_{\rm{C}}^{\rm{AC}} \cdot 6}{3 \cdot 2000} = 0.001 \cdot M_{\rm{C}}^{\rm{AC}} $$
$$ \varphi_{\rm{C}}^{\rm{BC}} \left( M_{\rm{C}}^{\rm{BC}} \right) = - \cfrac{M_{\rm{C}}^{\rm{BC}} \cdot \sqrt{13}}{3 \cdot \cfrac{2000 \cdot \sqrt{13}}{3}} = -0.0005 \cdot M_{\rm{C}}^{\rm{BC}} $$

::::

% solution_end

:::::{exercise}
:label: raam_1_5
:nonumber: true

Los je vormveranderingsvoorwaarde op samen met je eerder opgestelde evenwichtsvergelijking om $M_{\rm{C}}^{\rm{AC}}$ en $M_{\rm{C}}^{\rm{BC}}$ te vinden.


```{h5p} https://tudelft.h5p.com/content/1292652234901684787/embed
```

:::::

% solution_start

::::{solution} raam_1_5
:class: dropdown

De vormveranderingsvoorwaarde is: $\varphi_{\rm{C}}^{\rm{AC}} = \varphi_{\rm{C}}^{\rm{BC}} \rightarrow 0.001 \cdot M_{\rm{C}}^{\rm{AC}} = -0.0005 \cdot M_{\rm{C}}^{\rm{BC}}$


Hieruit en uit de eerder opgestelde momentenevenwichtsvergelijking volgt: $M_{\rm{C}}^{\rm{AC}} = -10 \rm{kNm}$ en $M_{\rm{C}}^{\rm{BC}} = 20 \rm{kNm}$. 

::::

% solution_end

````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze oefeningen zijn aangepast van https://github.com/TUDelft-books/CT1000 versie CTB2210-2025.
```
````
