````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze pagina is aangepast van https://oit.tudelft.nl/CT1000/2024/week_7/session_1/intro.html

% source files on https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_1

```
````

# Begeleide oefening 1

Gegeven is de volgende constructie:

```{figure} lesoefening_data/constructie.svg
:align: center

Constructie, $EA = \cfrac{12.5}{7} \ \rm{MN}$
```

Waarvoor de horizontale en verticale verplaatsingen van scharnier $\rm{S}$ als vrijheidsgraden worden genomen, met positief naar rechts en naar beneden.

```{figure} lesoefening_data/displaced.svg
:align: center
```

::::{question} Opgave
:label: verplaats2_1
:type: multiple-choice
:variant: single-select
:admonition:
:class: exercise
:nocaption:
:showanswer:

Waarom is het niet nodig de rotatie van $\rm{S}$ als vrijheidsgraad mee te nemen?
---
[x] De rotatie van een scharnier heeft geen betekenis.
[ ] De staven zullen niet roteren.
> De staven zullen wel degelijk kunnen roteren. Als er een beetje verticale verplaatsing van $\rm{S}$ plaatsvindt zullen de horizontale staven niet meer horizontaal staan. Echter is dat geen onafhankelijke vrijheidsgraad.
[ ] De constructie is statisch bepaald.
> Dit is irrelevant voor de vraag.
---

::::


::::{question} Opgave
:label: verplaats2_2
:type: multiple-choice
:variant: single-select
:admonition:
:class: exercise
:nocaption:
:showanswer:

Heb je hier Williot nodig om de verlenging/verkorting van de staven te bepalen?
---
[ ] Ja, je hebt Williot nodig om de rek in alle staven te bepalen.
> Incorrect, Williot is nodig als je niet weet hoeveel de staven roteren bij bekende verlenging/verkorting.
[ ] Ja, je hebt Williot alleen nodig om de verlenging/verkorting in staaf SC te bepalen en niet in de andere staven.
> Incorrect, Williot is nodig als je niet weet hoeveel de staven roteren bij bekende verlenging/verkorting
[x] Nee, je hebt geen Williot nodig.
> Correct, je weet precies waar S heen gaat, dus hebt geen Williot nodig om de rotatie van de staven te bepalen.
---

::::

::::{question} Opgave
:label: verplaats2_3
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
MAPE[2500/7;1;3]
M[0]
MAPE[-6250/7;1;3]
M[0]
MAPE[-1500/7;1;3]
MAPE[-2000/7;1;3]
^^^
? Bepaal de normaalkrachten in de drie staven in de constructie als functie van de verplaatsingen $u_{\rm{S,h}}$ en $u_{\rm{S,v}}$.

- $ N_{\rm{AS}} \left( u_{\rm{S,h}} , u_{\rm{S,v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot u_{\rm{S,h}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot u_{\rm{S,v}} $
- $ N_{\rm{SB}} \left( u_{\rm{S,h}} , u_{\rm{S,v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot u_{\rm{S,h}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot u_{\rm{S,v}} $
- $ N_{\rm{SC}} \left( u_{\rm{S,h}} , u_{\rm{S,v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot u_{\rm{S,h}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot u_{\rm{S,v}} $
---

::::


::::{question} Opgave
:label: verplaats2_4
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
MAP[-33.6;1]
MAP[270.2;1]

^^^
? Bepaal de waarde van de vrijheidsgraden $u_{\rm{S,h}}$ en $u_{\rm{S,v}}$.

- $ u_{\rm{S,h}} =  $ {gap} $ \rm{mm} $
- $ u_{\rm{S,v}} =  $ {gap} $ \rm{mm} $
---

::::


::::{question} Opgave
:label: verplaats2_5
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-12]
M[30]
M[-70]
^^^
? Bepaal de normaalkrachten in de drie staven.

- $ N_{\rm{AS}}  = $ {gap} $ \rm{kN}$
- $ N_{\rm{SB}} = $ {gap} $ \rm{kN}$
- $ N_{\rm{SC}} = $ {gap} $ \rm{kN}$
---

::::
