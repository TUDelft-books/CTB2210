# Oefenen

Nu gaan we aan de slag met een oefening.

````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze oefeningen is aangepast van  https://github.com/TUDelft-books/CT1000 versie CTB2210-2025.
```
````
## Oefening 1

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

Waarom zijn dit lastige constructies om op te lossen?

:::::

:::::{exercise}
:label: raam_1_2
:nonumber: true

Laten we de constructie oplossingen met hoekveranderingsvergelijkingen, door een scharnier toe te voegen bij hoek $\rm{C}$. Echter, daar werkt ook een uitwendig koppel. Het moment net links en onder $\rm{C}$ is dus niet gelijk aan elkaar. Als we het heel netjes zouden doen zouden we het scharnier net links of net onder het scharnier kunnen aanbrengen. Laten we de situatie bekijken met het scharnier net links van $\rm{C}$.

```{figure} ./lesoefeningen_data/scharnier_links_C.svg
:align: center

Statisch bepaald systeem met scharnier net links van $\rm{C}$
```

Gegeven is het vrijlichaamsschema van knoop $\rm{C}$:

```{figure} ./lesoefeningen_data/VLS_C_1.svg
:align: center

Vrijlichaamsschema van knoop $\rm{C}$ vergroot weergegeven
```

Wat is het moment $M_{\rm{C}}^{\rm{BC}}$?
:::::

Om het gedoe met dat scharnier net links/net onder $\rm{C}$ te voorkomen kunnen we het scharnier ook direct in C plaatsen. Deze aanpak wordt aangeraden.

```{figure} ./lesoefeningen_data/scharnier_in_C.svg
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

Hoeveel statisch onbepaalde krachten/momenten zijn er?

:::::

:::::{exercise}
:label: raam_1_4
:nonumber: true

Los de krachtsverdeling en verplaatsingen van deze constructie uit als functie van $M_{\rm{C}}^{\rm{AC}}$
:::::

:::::{exercise}
:label: raam_1_5
:nonumber: true

Los je vormveranderingsvoorwaarde op om $M_{\rm{C}}^{\rm{AC}}$ te vinden.

:::::

:::::{exercise}
:label: raam_1_5
:nonumber: true

Los nu overige krachtsverdeling op.

:::::

![alt text](image-2.png)