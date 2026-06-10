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
[ ] Een willekeurige maar kleine waarde
> Onjuist, aangezien er geen kracht staat op de kabels, kan deze ook als pendelstaaf worden gemodelleerd? wat is de invloed van $EI$ op het vervormingsgedrag van de kabels?
[x] Een willekeurige waarde
> Exact, waarom maakt het voor de kabels niet uit wat de waarde is van EI? Waarom kunnen deze als pendelstaven worden gemodelleerd?
---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

De kabels zullen niet buigen omdat er geen krachten op staan en scharnierend verbonden zijn. Ze kunnen dus als pendelstaven worden gemodelleerd, waarbij de stijfheid in buiging geen invloed heeft op het gedrag van de constructie.

::::

% solution_end

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

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Een waarde van oneindig kan niet, dus een willekeurige maar grote waarde is de beste optie.
::::

% solution_end

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

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Hoewel er redelijk verstopt een optie is om een geroteerde roloplegging te modelleren, kan dit ook worden gedaan door een pendelstaaf dwars op de rolrichting van het rolscharnier toe te voegen. Deze pendelstaaf zal bij kleine verplaatsingen in één richting beweging toelaten, net als een roloplegging zou doen. De rekstijfheid van deze pendelstaaf moet groot genoeg zijn.

::::

::::{admonition} Uitwerking MatrixFramebestand
:class: solution, dropdown

Het bestand van dit voorbeeld is [hier](./lesoefeningen_data/lesoefening_3.mxf) te downloaden.

::::

% solution_end
