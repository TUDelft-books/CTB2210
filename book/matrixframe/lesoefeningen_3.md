# Begeleide oefening 3 

Gegeven is de volgende constructie:

```{figure} lesoefeningen_data/Structure_2.svg
---
align: center
---
Constructie
```

Bepaal de oplegreacties, verplaatsingen en het krachtsverloop in de constructie met MatrixFrame.

:::::{exercise}
:label: mf_2_1
:nonumber: true

Voer de geometrie in en ga verder met de profielgegevens.

```{h5p} https://tudelft.h5p.com/content/1292628194575324387/embed
```

```{h5p} https://tudelft.h5p.com/content/1292628196202543167/embed
```

:::::

% solution_start

::::{solution} mf_2_1
:class: dropdown

Vraag 1:

- $EI = 0$
  - Onjuist, MatrixFrame heeft een waarde ongelijk aan 0 nodig om de constructie door te kunnen rekenen. Heeft de waarde van EI invloed op je antwoord?
- Een willekeurige maar kleine waarde
  - Onjuist, aangezien er geen kracht staat op de kabels, kan deze ook als pendelstaaf worden gemodelleerd? wat is de invloed van EI op het vervormingsgedrag van de kabels?
- Een willekeurige waarde
  - Exact, waarom maakt het voor de kabels niet uit wat de waarde is van EI? Waarom kunnen deze als pendelstaven worden gemodelleerd?

Vraag 2:

- $EI = \infty$
  - Onjuist, een waarde van oneindig kan je niet invullen. Hoe kan je dat numeriek benaderen?
- Een willekeurige, maar grote, waarde
  - Correct, welke waarde kies je?
- Een willekeurige waarde
  - Onjuist, als je een kleine stijfheid invoert zal dat zeker geen oneindige waarde simuleren.
::::

% solution_end

:::::{exercise}
:label: mf_2_2
:nonumber: true

Ga verder met opleggingen.

```{h5p} https://tudelft.h5p.com/content/1292628203010084277/embed
```

:::::

% solution_start

::::{solution} mf_2_2
:class: dropdown

- Een pendelstaaf dwars op de rolrichting van het rolscharnier toevoegen
  - Correct, wat voor profielgegevens voeg je toe voor deze pendelstaaf?
- Roloplegging in zowel horizontale als verticale oplegging toevoegen
  - Onjuist, dan heb je er een reguliere scharnierende verbinding van gemaakt
- Er is geen alternatief
  - Onjuist, een pendelstaaf staat bij kleine verplaatsingen ook in één richting beweging toe.

::::

% solution_end

:::::{exercise}
:label: mf_2_3
:nonumber: true

Voer de scharnierende aansluitingen in, voer de linear-elastische berekening uit en bekijk de resultaten.

```{h5p} https://tudelft.h5p.com/content/1292628206080447537/embed
```

:::::

% solution_start

::::{solution} mf_2_3
:class: dropdown

- De maximale verplaatsing van BC in verticale richting is *0.27* m
- De maximale zakking van AD in verticale richting is *1.42* cm
- De grootste normaalkracht in de kabels is *303.08* kN

```{figure} lesoefeningen_data/image6.png
---
align: center
---
Maximale verplaatsing van BC
```

```{figure} lesoefeningen_data/image7.png
---
align: center
---
Maximale zakking van AD
```

```{figure} lesoefeningen_data/image8.png
---
align: center
---
Maximale zakking van AD
```


::::

% solution_end

