# Begeleide oefening 3 

Gegeven is de volgende constructie:

```{figure} lesoefeningen_data/Structure_2.svg
---
align: center
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/matrixframe
---
Constructie
```

Deze opgave hoef je niet volledig op te lossen met MatrixFrame vanwege de grootte van de constructie. Echter moet je wel weten hoe je een aantal bijzondere eigenschappen van deze constructie kan modelleren in MatrixFrame.

::::{question} Opgave
:admonition:
:class: exercise
:nocaption:
:showanswer:

Voor de profielgegevens, wat vul je in voor de buigstijfheid van de kabels?
---
[ ] $ EI = 0$
> Onjuist, MatrixFrame heeft een waarde ongelijk aan $0$ nodig om de constructie door te kunnen rekenen. Heeft de waarde van $EI$ invloed op je antwoord?
[ ] Een kleine waarde voor een benadering van $EI = 0$
> Een kleine waarde geeft geen benadering maar het exacte antwoord. Aangezien er geen kracht staat op de kabels, kan deze ook als pendelstaaf worden gemodelleerd? Wat is de invloed van $EI$ op het vervormingsgedrag van de kabels?
[x] Een willekeurige waarde
> Exact, waarom maakt het voor de kabels niet uit wat de waarde is van EI? Waarom kunnen deze als pendelstaven worden gemodelleerd?
---

::::


::::{question} Opgave
:admonition:
:class: exercise
:nocaption:
:showanswer:

Voor de profielgegevens, wat vul je in voor de buigstijfheid van $\rm{AC}$?
---
[ ] $ EI = \infty$
> Onjuist, een waarde van oneindig kan je niet invullen. Hoe kan je dat numeriek benaderen?
[x] Een willekeurige maar grote waarde
> Correct, welke waarde kies je?
[ ] Een willekeurige waarde
> Onjuist, als je een kleine stijfheid invoert zal dat zeker geen oneindige waarde simuleren.
---

::::


::::{question} Opgave
:admonition:
:class: exercise
:nocaption:
:showanswer:

Hoe kan je de geroteerde roloplegging modelleren?
---
[x] Een pendelstaaf dwars op de rolrichting van het rolscharnier toevoegen
> Correct, wat voor profielgegevens voeg je toe voor deze pendelstaaf?
[ ] Roloplegging in zowel horizontale als verticale oplegging toevoegen
> Onjuist, dan heb je er een reguliere scharnierende verbinding van gemaakt
[ ] Deze kan niet gemodelleerd worden.
> Onjuist, een pendelstaaf staat bij kleine verplaatsingen ook in één richting beweging toe.
---

::::

