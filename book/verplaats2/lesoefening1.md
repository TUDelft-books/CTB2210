````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze pagina is aangepast van [de les van 14 oktober van het vak CT1000](https://oit.tudelft.nl/CEG-mechanics-BSc/NL/statically_inderminate/force_method/bending.html) van {cite:ts}`CT1000_2024`.

```
```` 

# Begeleide oefening 1

Gegeven is de volgende constructie:

```{figure-start} lesoefening_data/constructie.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_1
:number:
:figclass: sticky-margin
```

$ EA = \cfrac{25}{14} \ \rm{MN}$

```{figure-end}
```

Waarvoor de horizontale en verticale verplaatsingen van scharnier $\rm{S}$ als vrijheidsgraden worden genomen, met positief naar rechts en naar beneden.

```{figure-start} lesoefening_data/displaced.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_1
:number:
:figclass: sticky-margin
```

$ EA = \cfrac{25}{14} \ \rm{MN}$

```{figure-end}
```

::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Schets de vervormde constructie ten gevolge van de nog onbekende verplaatsingen van knoop $\rm{S}$.
---
=
```{figure} lesoefening_data/vervormd.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_1
:number:
```

---

::::

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
> De staven zullen wel degelijk kunnen roteren. Als er een beetje verticale verplaatsing van $\rm{S}$ plaatsvindt zullen de horizontale staven niet meer horizontaal staan. Echter is dat geen onafhankelijke vrijheidsgraad, maar kan worden afgeleid uit de horizontale en verticale verplaatsing van $\rm{S}$.
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
> Correct, je weet al precies waar $\rm{S}$ heen gaat, dus hebt geen Williot nodig om de rotatie van de staven te bepalen.
---

::::

::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Splits de constructie en teken de vervormingen van elk van de drie staven inclusief de bijbehorende verplaatsingen en krachten.
---
=
```{figure} lesoefening_data/gesplitst.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_1
:number:
```

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
M[0]
MAPE[-6250/7;1;3]
M[0]
M[0]
MAPE[-1500/7;1;3]
MAPE[-2000/7;1;3]
M[0]
^^^
? Bepaal de normaalkrachten in de drie staven in de constructie als functie van de verplaatsingen $u_{\rm{S,h}}$ en $u_{\rm{S,v}}$.

- $ N_{\rm{AS}} \left( u_{\rm{S,h}} , u_{\rm{S,v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot u_{\rm{S,h}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot u_{\rm{S,v}} + $ {gap} $ \left(\rm{in \ kN}\right) $
- $ N_{\rm{SB}} \left( u_{\rm{S,h}} , u_{\rm{S,v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot u_{\rm{S,h}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot u_{\rm{S,v}} + $ {gap} $ \left(\rm{in \ kN}\right) $
- $ N_{\rm{SC}} \left( u_{\rm{S,h}} , u_{\rm{S,v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot u_{\rm{S,h}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kN}}{\rm{m}}\right) \cdot u_{\rm{S,v}} + $ {gap} $ \left(\rm{in \ kN}\right) $
---

::::


::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Teken het vrijlichaamsschema van knoop $\rm{S}$ met de knopen in de richting zoals hierboven berekend.
---
=
```{figure} lesoefening_data/vrijlichaamsschema_S.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_1
:number:
```

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

::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Teken de vervormde constructie op schaal.
---
=
```{figure} lesoefening_data/vervormd_schaal.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_1
:number:
```

---

::::
