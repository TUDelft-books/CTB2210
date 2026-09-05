# Begeleide oefening 1

Gegeven is de volgende constructie:

```{figure} lesoefeningen_data/structure_1.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/matrixframe
---

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


