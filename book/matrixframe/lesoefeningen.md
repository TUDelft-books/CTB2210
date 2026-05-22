# Begeleide oefening 1

Gegeven is de volgende constructie:

```{figure} lesoefeningen_data/structure_1.svg
---
align: center
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/matrixframe
---
Constructie
```

Bepaal de oplegreacties en het krachtsverloop in de constructie met MatrixFrame.

::::{question} Opgave
:admonition:
:class: exercise
:nocaption:
:showanswer:

Voer de geometrie in en ga verder met de profielgegevens. Welke profielgegeven vul je in om tot het juiste antwoord te komen?
---
[ ] Ik vul geen profielgegevens in.
> Onjuist, MatrixFrame heeft profielgegevens nodig. Als je deze constructie met de hand zou uitrekenen, zou je dan stijfheidsgegevens nodig hebben voor de oplegreacties en krachtsverdeling?
[x] Ik verzin zelf wat
> Exact! Waarom maakt het niet uit welke waardes je invult?
[ ] Ik kan het juiste antwoord niet bepalen, want de profielgegevens zijn vereist
> Onjuist, voor het bepalen van de oplegreacties en krachtsverdeling zou je geen stijfheidsgegevens nodig moeten hebben, alhoewel MatrixFrame dat wel vereist. Maakt het uit welke waardes je invult?
---

::::


% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Je kan zelf wat verzinnen omdat de constructie statisch bepaald is. De oplegreacties en krachtsverdeling zijn onafhankelijk van de stijfheidsgegevens van de constructie. Er zijn wel profielgegevens nodig om voor de berekening, maar deze kunnen willekeurig zijn.

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
M[0]
M[1;2]
M[2;3]
M[1]
^^^
? Voer de opleggingen in en ga verder met de scharnierende aansluitingen. Hoeveel scharnierende staafaansluitingen heb je nodig?

- Rondom A {gap} scharnierende aansluitingen
- Rondom B {gap} scharnierende aansluitingen
- Rondom C {gap} scharnierende aansluitingen
- Rondom D {gap} scharnierende aansluitingen
---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

- Rondom A moeten de staven star verbonden worden, dus daar zijn geen scharnierende aansluitingen nodig.
- Rondom B moeten de twee staven scharnierend aan elkaar verbonden worden. Dat kan met een scharnierende aansluiting op één uiteinde of op alle twee de uiteindes.
- Rondom C moeten de drie staven scharnierend aan elkaar verbonden worden. Dat kan met een scharnierende aansluiting op één uiteinde van elke staaf, of met een scharnierende aansluiting op twee van de drie staven.
- Rondom D moet één staaf scharnierend aan de doorlopende staaf verbonden worden. Dat kan met een scharnierende aansluiting op het uiteinde van de pendelstaaf.

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
MAP[5.67;0.1]
MAP[77.64;1]
MAP[59.72;1]
^^^
? Voer de linear-elastische berekening uit en bekijk de resultaten.

- De oplegreactie bij $\rm{A}$ is {gap} $\rm{kN}$ (positief omhoog, negatief omlaag).
- Het maximale absolute moment in de constructie is {gap} $\rm{kNm}$.
- De maximale absolute dwarskracht in de constructie is {gap} $\rm{kN}$.
---

::::


% solution_start


::::{admonition} Uitwerking
:class: solution, dropdown

```{figure} lesoefeningen_data/image.png
---
align: center
---
Oplegreacties
```

```{figure} lesoefeningen_data/image_1.png
---
align: center
---
Momenten
```

```{figure} lesoefeningen_data/image_2.png
---
align: center
---
Dwarskrachten
```

::::

::::{admonition} Uitwerking MatrixFramebestand
:class: solution, dropdown

Het bestand van dit voorbeeld is [hier](./lesoefeningen_data/lesoefening_1.mxe) te downloaden.

::::

% solution_end
