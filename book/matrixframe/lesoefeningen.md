# Begeleide oefening 1

Gegeven is de volgende constructie:

```{figure} lesoefeningen_data/structure_1.svg
---
align: center
---
Constructie
```

Bepaal de oplegreacties en het krachtsverloop in de constructie met MatrixFrame.

:::::{exercise}
:label: mf_1_1
:nonumber: true

Voer de geometrie in en ga verder met de profielgegevens.

```{h5p} https://tudelft.h5p.com/content/1292628057313860177/embed
```

:::::

% solution_start

::::{solution} mf_1_1
:class: dropdown

- Ik vul geen profielgegevens in
  - Onjuist, MatrixFrame heeft profielgegevens nodig. Als je deze constructie met de hand zou uitrekenen, zou je dan stijfheidsgegevens nodig hebben voor de oplegreacties en krachtsverdeling?
- Ik verzin zelf wat
  - Exact! Waarom maakt het niet uit welke waardes je invult?
- Ik kan het juiste antwoord niet bepalen, want de profielgegevens zijn vereist
  - Onjuist, voor het bepalen van de oplegreacties en krachtsverdeling zou je geen stijfheidsgegevens nodig moeten hebben, alhoewel MatrixFrame dat wel vereist. Maakt het uit welke waardes je invult?

::::

% solution_end

:::::{exercise}
:label: mf_1_2
:nonumber: true

Voer de opleggingen in en ga verder met de scharnierende aansluitingen.

```{h5p} https://tudelft.h5p.com/content/1292628065481210467/embed
```

:::::

% solution_start

::::{solution} mf_1_2
:class: dropdown

- Rondom A is gelijk aan *0*
- Rondom B is gelijk aan *1/2*
- Rondom C is gelijk aan *2/3*
- Rondom D is gelijk aan *1*

::::

% solution_end

:::::{exercise}
:label: mf_1_3
:nonumber: true

Voer de linear-elastische berekening uit en bekijk de resultaten.

```{h5p} https://tudelft.h5p.com/content/1292628082183016877/embed
```

:::::

% solution_start

<!---
Heb je de goede resultaten? Rond of op 2 decimalen en gebruik een . als decimaalteken.

-->

::::{solution} mf_1_3
:class: dropdown

- De oplegreactie bij A is *5.67* kN (positief omhoog, negatief omlaag).
- Het maximale absolute moment in de constructie is *77.64* kNm.
- De maximale absolute dwarskracht in de constructie is *59.72* kN.

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

% solution_end