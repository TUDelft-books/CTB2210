````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze oefening is aangepast de [les van 7 oktober](https://oit.tudelft.nl/CT1000/2024/week_6/session_1/intro.html) van {cite:ts}`CT1000_2024`

```
```` 

# Begeleide oefening 2

Gegeven is de volgende constructie:

```{figure-start} ./lesoefeningen2_data/structure.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:figclass: sticky-margin
:number:
```

- $EI = \cfrac{1000}{3} \, \rm{kNm^2}$
- $EA >> EI $

```{figure-end}
```


::::{margin}
:::{note}
Zie ook de COZ opgaves van 8 september waar je dit al berekend hebt: [COZ opgave 2.3](../statisch_onbepaald/COZ3.md).
:::
::::

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[3]
^^^
?
De constructie is {gap}ste/de graads inwendig statisch onbepaald.

---
::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown
:name: stat_onbepaald_raamwerk

:::{fetch} {numref}`stat_onbepaald_raamwerk_1`
:::

Er zijn 25 onbekende krachten

:::{fetch} {numref}`stat_onbepaald_raamwerk_2`
:::

Er zijn 22 evenwichtsvergelijkingen



Dus de constructie is ($25 - 22=$) 3de graads statisch onbepaald. 


::::
% solution_end

::::::{admonition} Opgave
:class: exercise

Gegeven is de volgende mogelijke aangepaste constructie:

```{figure} ./lesoefeningen2_data/aanpassing1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

:::::{question}
:nocaption:
:showanswer:
:columns: 1


Is deze constructie statisch bepaald, statisch onbepaald of een mechanisme?
---
[x] Deze constructie is statisch bepaald.
[ ] Deze constructie is statisch onbepaald.
> Er zijn drie aanpassingen gedaan, waarvan elke aanpassing de graad van statische onbepaaldheid met 1 verlaagd.
[ ] Deze constructie is een mechanisme.
> Er zijn geen globale of lokale mechanismes! Het scharnier halverwege $\rm{B}$ en $\rm{C}$ kan niet vrij bewegen aangezien staaf $\rm{AB}$ weerstand biedt voor de rotatie van knoop $\rm{B}$.
---

:::::

:::::{question}
:type: no-input
:nocaption:
:showanswer:

Schets de mogelijke vervormingen ten gevolge van de verdeelde belasting:

---
=

```{figure} ./lesoefeningen2_data/aanpassing1_verplaatsing.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

---

:::::

:::::{question}
:nocaption:
:showanswer:
:columns: 1

Is deze aangepaste constructie een goede keuze voor de krachtenmethode?
---
[ ] Ja
> De zakking van het scharnier halverwege $\rm{B}$ en $\rm{C}$ maakt het lastiger om de verplaatsingen te berekenen.
[x] Het kan, maar er zijn betere opties
[ ] Nee
> Deze constructie is statisch bepaald en daarmee geschikt!
---

:::::

::::::

::::::{admonition} Opgave
:class: exercise

Gegeven is de volgende mogelijke aangepaste constructie:

```{figure} ./lesoefeningen2_data/aanpassing2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

:::::{question}
:nocaption:
:showanswer:
:columns: 1


Is deze constructie statisch bepaald, statisch onbepaald of een mechanisme?
---
[x] Deze constructie is statisch bepaald.
> Er zijn slechts 2 aanpassingen gedaan, waarvan elke aanpassing de graad van statische onbepaaldheid met 1 verlaagd.
[ ] Deze constructie is statisch onbepaald.
[ ] Deze constructie is een mechanisme.
> Er zijn geen globale of lokale mechanismes!
---

:::::

:::::{question}
:nocaption:
:showanswer:
:columns: 1

Is deze aangepaste constructie een goede keuze voor de krachtenmethode?
---
[ ] Ja
> De constructie is nog niet statisch bepaald.
[ ] Het kan, maar er zijn betere opties
> De constructie is nog niet statisch bepaald.
[x] Nee
---

:::::

::::::

::::::{admonition} Opgave
:class: exercise

Gegeven is de volgende mogelijke aangepaste constructie:

```{figure} ./lesoefeningen2_data/aanpassing3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

:::::{question}
:nocaption:
:showanswer:
:columns: 1


Is deze constructie statisch bepaald, statisch onbepaald of een mechanisme?
---
[x] Deze constructie is statisch bepaald.
[ ] Deze constructie is statisch onbepaald.
> Er zijn drie aanpassingen gedaan, waarvan elke aanpassing de graad van statische onbepaaldheid met 1 verlaagd.
[ ] Deze constructie is een mechanisme.
> Er zijn geen globale of lokale mechanismes! $\rm{BC}$ kan niet vrij roteren om $\rm{B}$ vanwege de starre verbindingen met de andere staven
---

:::::

:::::{question}
:type: no-input
:nocaption:
:showanswer:

Schets de mogelijke vervormingen ten gevolge van de verdeelde belasting:

---
=

```{figure} ./lesoefeningen2_data/aanpassing3_verplaatsing.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

---

:::::

:::::{question}
:nocaption:
:showanswer:
:columns: 1

Is deze aangepaste constructie een goede keuze voor de krachtenmethode?
---
[ ] Ja
> De inwendige krachten bij $\rm{D}$ en $\rm{B}$ zijn niet direct vanzelfsprekend. Daarnaast vereist het berekenen van de verplaatsing van $\rm{A}$ een aantal stappen evenals de starre rotatie van $\rm{BAD}$.
[x] Het kan, maar er zijn betere opties
[ ] Nee
> Deze constructie is statisch bepaald en daarmee geschikt!
---

:::::

::::::

::::::{admonition} Opgave
:class: exercise

Gegeven is de volgende mogelijke aangepaste constructie:

```{figure} ./lesoefeningen2_data/aanpassing4.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

:::::{question}
:nocaption:
:showanswer:
:columns: 1


Is deze constructie statisch bepaald, statisch onbepaald of een mechanisme?
---
[x] Deze constructie is statisch bepaald.
[ ] Deze constructie is statisch onbepaald.
> Er zijn drie aanpassingen gedaan, waarvan elke aanpassing de graad van statische onbepaaldheid met 1 verlaagd.
[ ] Deze constructie is een mechanisme.
> Er zijn geen globale of lokale mechanismes!
---

:::::

:::::{question}
:type: no-input
:nocaption:
:showanswer:

Schets de mogelijke vervormingen ten gevolge van de verdeelde belasting:

---
=

```{figure} ./lesoefeningen2_data/aanpassing4_verplaatsing.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

---

:::::

:::::{question}
:nocaption:
:showanswer:
:columns: 1

Is deze aangepaste constructie een goede keuze voor de krachtenmethode?
---
[x] Ja
[ ] Het kan, maar er zijn betere opties
> De verplaatsingen zijn eenvoudig te berekenen met vergeet-me-nietjes waarbij de invloed van de krachten zich zelfs beperkt tot individuele staven.
[ ] Nee
> Deze constructie is statisch bepaald en daarmee geschikt!
---

:::::

::::::

::::::{admonition} Opgave
:class: exercise

Gegeven is de volgende mogelijke aangepaste constructie:

```{figure} ./lesoefeningen2_data/aanpassing5.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

:::::{question}
:nocaption:
:showanswer:
:columns: 1


Is deze constructie statisch bepaald, statisch onbepaald of een mechanisme?
---
[ ] Deze constructie is statisch bepaald.
> Hoewel het scharnier in $\rm{B}$ verlaagt de statisch onbepaaldheid met 2 leidt dat in combinatie met de aangepaste oplegging tot een mechanisme.
[ ] Deze constructie is statisch onbepaald.
> De aanpassing in het scharnier in $\rm{B}$ verlaagt de statisch onbepaaldheid met 2 en de aanpassing in de oplegging verlaagt de statisch onbepaaldheid met 1. Maar tot heeft ook nog andere effecten!
[x] Deze constructie is een mechanisme.
---

:::::

:::::{question}
:nocaption:
:showanswer:
:columns: 1

Is deze aangepaste constructie een goede keuze voor de krachtenmethode?
---
[ ] Ja
> De constructie is nog niet statisch bepaald.
[ ] Het kan, maar er zijn betere opties
> De constructie is nog niet statisch bepaald.
[x] Nee
---

:::::

::::::

Er wordt gekozen voor het volgende statisch bepaalde systeem inclusief vormveranderingsvoorwaarden:

```{figure-start} ./lesoefeningen2_data/structure2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:figclass: sticky-margin
:number:
```

- $EI = \cfrac{1000}{3} \, \rm{kNm^2}$
- $EA >> EI $
```{figure-end}
```

:::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Schets de mogelijke vervormingen ten gevolgde van de momenten bij $\rm{D}$
---
=

```{figure} ./lesoefeningen2_data/vervorming_1.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

---

:::::

:::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Schets de mogelijke vervormingen ten gevolgde van $M_{\rm{B}}^{\rm{BD}}$.
---
=

```{figure} ./lesoefeningen2_data/vervorming_2.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

:::{note}
Merk op dat de verplaatsingen zijn getekend alsof het scharnier net links van knoop $\rm{B}$ zit hoewel het scharnier net iets verder van de knoop is afgebeeld.
:::

---

:::::

:::::{question} Opgave
:type: no-input
:admonition:
:class: exercise
:nocaption:
:showanswer:

Schets de mogelijke vervormingen ten gevolgde van $M_{\rm{B}}^{\rm{AB}}$.
---
=

```{figure} ./lesoefeningen2_data/vervorming_3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode_raamwerk
:number:
```

:::{note}
Merk op dat de verplaatsingen zijn getekend alsof het scharnier net linksonder knoop $\rm{B}$ zit hoewel het scharnier net iets verder van de knoop is afgebeeld.
:::

---

:::::

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[0.006]
M[0]
M[0]
M[0]
M[-0.008]
M[-0.004]
M[0]
M[0]
M[-0.004]
M[-0.008]
M[0]
M[0]
M[0]
M[0]
M[0.01]
M[0]
M[0]
M[0.006]
M[-0.006]
M[0.297]
^^^
? Bepaal de hoeken $\varphi_{\rm{D}}^{\rm{AD}}$, $\varphi_{\rm{D}}^{\rm{BD}}$, $\varphi_{\rm{B}}^{\rm{BD}}$, $\varphi_{\rm{B}}^{\rm{AB}}$ en $\varphi_{\rm{B}}$ als functie van $M_{\rm{D}}$, $M_{\rm{B}}^{\rm{BD}}$ en $M_{\rm{B}}^{\rm{AB}}$, met de momenten in $\rm{kNm}$ en $\varphi$ in $\rm{rad}$.

- $\varphi_{\rm{D}}^{\rm{AD}} \left( M_{\rm{D}}, M_{\rm{B}}^{\rm{BD}}, M_{\rm{B}}^{\rm{AB}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{D}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{BD}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{AB}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$
- $\varphi_{\rm{D}}^{\rm{BD}} \left( M_{\rm{D}}, M_{\rm{B}}^{\rm{BD}}, M_{\rm{B}}^{\rm{AB}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{D}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{BD}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{AB}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$
- $\varphi_{\rm{B}}^{\rm{BD}} \left( M_{\rm{D}}, M_{\rm{B}}^{\rm{BD}}, M_{\rm{B}}^{\rm{AB}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{D}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{BD}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{AB}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$
- $\varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{D}}, M_{\rm{B}}^{\rm{BD}}, M_{\rm{B}}^{\rm{AB}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{D}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{BD}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{AB}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$
- $\varphi_{\rm{B}} \left( M_{\rm{D}}, M_{\rm{B}}^{\rm{BD}}, M_{\rm{B}}^{\rm{AB}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{D}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{BD}} + $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kNm}}\right) \cdot M_{\rm{B}}^{\rm{AB}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$

---

::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

De uitdrukkingen voor de hoekverdraaiingen worden gevonden met behulp van de vergeet-mij-nietjes voor een ligger op twee steunpunten belast door een koppel en door een verdeelde belasting, de positieve richtingen worden genomen zoals in de figuur aangegeven. 

$$ \varphi_{\rm{D}}^{\rm{AD}} \left( M_{\rm{D}}\right) = \cfrac{M_{\rm{D}} \cdot 6}{3 \cdot \cfrac{1000}{3}} = 0.006 \cdot M_{\rm{D}} $$
$$ \varphi_{\rm{D}}^{\rm{BD}} \left( M_{\rm{D}}, M_{\rm{B}}^{\rm{BD}} \right) = - \cfrac{M_{\rm{D}} \cdot 8}{3 \cdot \cfrac{1000}{3}} - \cfrac{M_{\rm{B}}^{\rm{BD}} \cdot 8}{6 \cdot \cfrac{1000}{3}} = -0.008 \cdot  M_{\rm{D}} -0.004 \cdot M_{\rm{B}}^{\rm{BD}} $$
$$ \varphi_{\rm{B}}^{\rm{BD}} \left( M_{\rm{D}}, M_{\rm{B}}^{\rm{BD}} \right) = - \cfrac{M_{\rm{D}} \cdot 8}{6 \cdot \cfrac{1000}{3}} - \cfrac{M_{\rm{B}}^{\rm{BD}} \cdot 8}{3 \cdot \cfrac{1000}{3}} = -0.004 \cdot  M_{\rm{D}} -0.008 \cdot M_{\rm{B}}^{\rm{BD}} $$
$$ \varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{B}}^{\rm{AB}} \right) = \cfrac{M_{\rm{B}}^{\rm{AB}} \cdot 10}{3 \cdot \cfrac{1000}{3}} = 0.01 \cdot M_{\rm{B}}^{\rm{AB}} $$
$$ \varphi_{\rm{B}}^{\rm{BC}} \left( M_{\rm{B}}^{\rm{BD}}, M_{\rm{B}}^{\rm{AB}} \right) = \cfrac{\left(M_{\rm{B}}^{\rm{BD}} - M_{\rm{B}}^{\rm{AB}}\right) \cdot 6}{3 \cdot \cfrac{1000}{3}} + \cfrac{11 \cdot 6^3}{24 \cdot \cfrac{1000}{3}} = 0.006 \cdot M_{\rm{B}}^{\rm{BC}} - 0.006 \cdot M_{\rm{B}}^{\rm{AB}} + 0.297 $$

::::

% solution_end

:::::{exercise}
:label: raam_2_5
:nonumber: true

Los met de vormveranderingsvoorwaarden en evenwichtsvergelijking de onbekenden $M_{\rm{D}}$, $M_{\rm{B}}^{\rm{BD}}$, $M_{\rm{B}}^{\rm{AB}}$ en $M_{\rm{B}}^{\rm{BC}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292652282254607197/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

Er zijn 4 onbekenden en 4 vergelijkingen. De vergelijkingen bestaan uit de momentenevenwichtsvergelijking uit de vorige deelvraag en de onderstaande vormveranderingsvoorwaarden:

$$ \varphi _ {\rm{B}} ^{\rm{BC}} = \varphi _ {\rm{B}} ^{\rm{AB}} \rightarrow 0.01 \cdot M_{\rm{B}}^{\rm{AB}} = 0.006 \cdot M_{\rm{B}}^{\rm{BC}} + 0.297 $$
$$ \varphi _ {\rm{B}} ^{\rm{AB}} = \varphi _ {\rm{B}} ^{\rm{BD}} \rightarrow 0.01 \cdot M_{\rm{B}}^{\rm{AB}} = -0.004 \cdot  M_{\rm{D}} -0.008 \cdot M_{\rm{B}}^{\rm{BD}} $$
$$ \varphi _ {\rm{D}} ^{\rm{AD}} = \varphi _ {\rm{D}} ^{\rm{BD}} \rightarrow  0.006 \cdot M_{\rm{D}} = -0.008 \cdot  M_{\rm{D}} -0.004 \cdot M_{\rm{B}}^{\rm{BD}} $$

Hieruit volgt:

$$ M_{\rm{D}} = 5 \rm{kNm} $$
$$ M_{\rm{B}}^{\rm{BD}} = -17.5 \rm{kNm} $$
$$ M_{\rm{B}}^{\rm{AB}} = 12 \rm{kNm} $$
$$ M_{\rm{B}}^{\rm{BC}} = -29.5 \rm{kNm} $$

::::

% solution_end

:::::{exercise}
:label: raam_2_6
:nonumber: true

Los de volledige krachtsverdeling op.

```{h5p} https://tudelft.h5p.com/content/1292652285215101017/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

$$ M_{\rm{A}} = 0 \rm{kNm} $$
$$ M_{\rm{halverwege} \ \rm{BC}} = 34.75 \rm{kNm} (◡) $$ 
$$ N_{\rm{BD}} \approx 0.83  \rm{kN} $$
$$ B_{\rm{v}} \approx 41.60 \rm{kN} $$

::::

% solution_end
