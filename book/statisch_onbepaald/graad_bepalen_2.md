# Begeleide oefening 2

Gegeven is de volgende constructie:

```{figure} ./graad_bepalen_data/Oefening_1.svg
---
align: center
figclass: sticky-margin
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
---
Constructie
```

Bepaal de graad van inwendig statisch onbepaaldheid. Hoewel je onderscheid kan maken tussen pendelstaven en reguliere staven en daarmee het aantal onbekende krachten en evenwichtsvergelijkingen minder wordt, vragen we je voor deze opgave om dat onderscheid eerst niet te maken. In het tweede deel van deze oefening 

## Geen onderscheid tussen pendelstaven en reguliere staven

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[6]
> Elk van de scharnierende opleggingen heeft $2$ oplegreacties.
M[34]
> Bij $\rm{A}$, onder $\rm{D}$, rondom $\rm{E}$ en rondom $\rm{G}$ zijn er geen momenten vanwege de scharnierende verbindingen. De andere aansluitingen hebben wel momenten.
M[40]
^^^
? Splits de constructie in alle losse knopen en staven, en teken het vrijlichaamsschema voor mogelijke krachten op de knopen. Houd daarbij rekening houdend met welke staven en opleggingen er aan de knopen verbonden zijn.

Er zijn {gap} onbekende oplegreacties en {gap} onbekende staafkrachten. Dat zijn {gap} onbekende krachten in totaal.
---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

```{figure} ./graad_bepalen_data/Oefening_2.svg
---
align: center
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
---
Aantal onbekende oplegreacties en staafkrachten op knopen
```

```{figure} ./graad_bepalen_data/Oefening_3.svg
---
align: center
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
---
Aantal onbekende staafkrachten op staven
```

Er zijn *6* onbekende oplegreacties en *34* onbekende staafkrachten. Dat zijn *40* onbekende krachten in totaal.

::::

% solution_end

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[15]
> Voor elke knoop waar momenten op werken zijn er $3$ evenwichtsvergelijkingen, voor de andere $2$.
M[21]
> Voor elke staaf zijn er $3$ evenwichtsvergelijkingen.
M[36]
^^^
? Splits de constructie in alle losse knopen en staven, en teken het vrijlichaamsschema voor mogelijke krachten op de knopen. Houd daarbij rekening houdend met welke staven en opleggingen er aan de knopen verbonden zijn.

Er zijn {gap} evenwichtsvergelijkingen vanuit knopen en {gap} vanuit staven. Dat zijn {gap} evenwichtsvergelijkingen in totaal.
---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Voor knoop $\rm{A}$, $\rm{E}$ en $\rm{G}$ zijn er enkel krachten in verticale en horizontale richting, dus zijn er $2$ evenwichtsvergelijkingen. Voor de anderen knopen zijn er ook momenten dus $3$ evenwichtsvergelijkingen per knoop. Dat geeft $\left( 2 +2 +2 +3+3+3 \right) = 15$ evenwichtsvergelijkingen vanuit knopen. Alle staven hebben drie evenwichtsvergelijkingen, dus dat geeft $\left( 7 \cdot 3 \right) = 21$ evenwichtsvergelijkingen vanuit staven. Dat zijn $36$ evenwichtsvergelijkingen in totaal.

```{figure} ./graad_bepalen_data/Oefening_4.svg
---
align: center
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
---
Aantal evenwichtsvergelijkingen voor de knopen
```

```{figure} ./graad_bepalen_data/Oefening_5.svg
---
align: center
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
---
Aantal evenwichtsvergelijkingen voor de staven
```

::::

% solution_end

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[4]
^^^
? De graad van statisch onbepaaldheid is het aantal oplegreacties + verbindingskrachten - aantal evenwichtsvergelijkingen

De constructie is {gap}ste/de graads uitwendig statisch onbepaald.
---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

$$40 - 36 = 4 $$

::::

% solution_end

## Wel onderscheid tussen pendelstaven en reguliere staven

Herhaal nu de berekening maar nu wel onderscheid maakt tussen pendelstaven en reguliere staven.

::::{question} Opgave
:variant: multiple-select
:columns: 4
:admonition:
:class: exercise
:nocaption:
:showanswer:

Welke staaf/staven zijn pendelstaven?
---
[ ] $\rm{AD}$
> Bij $\rm{D}$ is $\rm{AD}$ niet scharnierend verbonden.
[ ] $\rm{DB}$
> Bij $\rm{B}$ is $\rm{BD}$ niet scharnierend verbonden.
[ ] $\rm{DE}$
> Bij $\rm{D}$ is $\rm{DE}$ niet scharnierend verbonden.
[ ] $\rm{BE}$
> Bij $\rm{E}$ is $\rm{BE}$ niet scharnierend verbonden.
[x] $\rm{EG}$
[ ] $\rm{EC}$
> Bij $\rm{C}$ is $\rm{EC}$ niet scharnierend verbonden.
[ ] $\rm{CG}$
> Bij $\rm{C}$ is $\rm{CG}$ niet scharnierend verbonden.
---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Alleen staaf $\rm{EG}$ gaat van een scharnierende verbinding naar een scharnierende verbinding.

::::

% solution_end

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[6]
M[32]
> De dwarskrachten aan de uiteindes van $\rm{EG}$ komen nu te vervallen.
M[38]
^^^
? Splits de constructie in alle losse knopen en staven, en teken het vrijlichaamsschema voor mogelijke krachten op de knopen. Houd daarbij rekening houdend met welke staven en opleggingen er aan de knopen verbonden zijn.

Er zijn {gap} onbekende oplegreacties en {gap} onbekende staafkrachten. Dat zijn {gap} onbekende krachten in totaal.
---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

```{figure} ./graad_bepalen_data/Oefening_2_2.svg
---
align: center
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
---
Aantal onbekende oplegreacties en staafkrachten op knopen
```

```{figure} ./graad_bepalen_data/Oefening_3_2.svg
---
align: center
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
---
Aantal onbekende staafkrachten op staven
```

Er zijn *6* onbekende oplegreacties en *32* onbekende staafkrachten. Dat zijn *38* onbekende krachten in totaal.

Door de pendelstaaf zijn er 2 minder onbekende krachten.

::::

% solution_end

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[15]
> Op alle knopen werken nog minstens twee krachten in verschillende richtingen.
M[19]
> Voor de pendelstaaf zijn nu niet $3$ maar $1$ evenwichtsvergelijking toepasbaar.
M[34]
^^^
? Splits de constructie in alle losse knopen en staven, en teken het vrijlichaamsschema voor mogelijke krachten op de knopen. Houd daarbij rekening houdend met welke staven en opleggingen er aan de knopen verbonden zijn.

Er zijn {gap} evenwichtsvergelijkingen vanuit knopen en {gap} vanuit staven. Dat zijn {gap} evenwichtsvergelijkingen in totaal.
---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Hoewel er minder krachten werken op knoop $\rm{E}$ en $\rm{G}$ dan voorheen, zijn er nog steeds $2$ evenwichtsvergelijkingen toepasbaar omdat er nog krachten in verschillende richtingen werken.

```{figure} ./graad_bepalen_data/Oefening_4_2.svg
---
align: center
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
---
Aantal evenwichtsvergelijkingen voor de knopen
```

Voor de staaf $\rm{EG}$ is nu nog maar één evenwichtsvergelijking nodig (krachtevenwicht in de richting van de pendelstaaf). Dat zijn dus $2$ evenwichtsvergelijkingen minder dan voorheen.

```{figure} ./graad_bepalen_data/Oefening_5_2.svg
---
align: center
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/graad_statisch
---
Aantal evenwichtsvergelijkingen voor de staven
```

::::

% solution_end


::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[4]
^^^
? De graad van statisch onbepaaldheid is het aantal oplegreacties + verbindingskrachten - aantal evenwichtsvergelijkingen

De constructie is {gap}ste/de graads uitwendig statisch onbepaald.
---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

$$38 - 34 = 4 $$

Dus de pendelstaaf heeft er niet voor gezorgd dat de constructie meer of minder statisch onbepaald is.

::::

% solution_end