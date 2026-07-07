````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze pagina is aangepast van [deze instructie](https://oit.tudelft.nl/CEG-mechanics-BSc/NL/statically_inderminate/force_method/bending.html) van {cite:ts}`CEG_mechanics_BSc`.

```
```` 

# Begeleide oefening 1

Gegeven is de volgende constructie:

```{figure-start} ./bending_data/Example.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_balk
---

```

- $EI = \cfrac{16}{3} \ \rm{MNm^2}$
- $EA \gg EI $

```{figure-end}
```

Bepaal de krachtsverdeling en verplaatsingen.

Ga uit van het volgende statisch bepaalde systeem:

```{figure-start} ./bending_data/SB-systeem2.svg
---
align: center
figclass: sticky-margin
number:
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_balk
---

```

- $EI = \cfrac{16}{3} \ \rm{MNm^2}$
- $EA \gg EI $

```{figure-end}
```

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[4]
M[-200]
M[0.0015]
M[-0.075]
M[0.01]
M[-0.45]
^^^
? Bepaal de normaalkrachten in alle staven als functie van $A_{\rm{v}}$, met  $A_{\rm{v}}$ in $\rm{kN}$, $M_{\rm{B}}$ in $\rm{kNm}$, $\varphi_{\rm{B}}$ in $\rm{rad}$ en $w_{\rm{A}}$ in $\rm{m}$.

- $M_{\rm{B}} \left( A_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kNm}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{kNm}\right)$ (◠)
- $\varphi_{\rm{B}} \left( A_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$ (↻)
- $w_{\rm{A}} \left( A_{\rm{v}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{m}}{\rm{kN}}\right) \cdot A_{\rm{v}} + $ {gap} $\left(\rm{in} \, \rm{m}\right)$ (↑)


---

::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

```{figure} lesoefeningen_data/VrijlichaamsschemaBC.svg
---
align: center
number:
---
```

$$ M_{\rm{B}} \left( A_{\rm{v}} \right) = 4 \cdot A_{\rm{v}} -200 $$

De hoekverdraaiing bij B, $\varphi_{\rm{B}}$, kan worden bepaald uit $M_{\rm{B}}$ met behulp van het vergeet-mij-nietje voor een ligger op twee steunpunten belast door een koppel:

```{figure} lesoefeningen_data/BC.svg
---
align: center
number:
---
```

$$ \varphi_{\rm{B}} \left( A_{\rm{v}} \right) = \cfrac{1}{3} \cdot \cfrac{\left(4 \cdot A_{\rm{v}} -200\right) \cdot6}{\cfrac{16}{3} \cdot 10^3} = 0.0015 \cdot A_{\rm{v}} -0.0750 $$

De zakking in $\rm{A}$, $w_{\rm{A}}$, kan worden bepaald door deel $\rm{AB}$ bij $\rm{B}$ schuin in te klemmen met hoek $\varphi_{\rm{B}}$ en de zakkingen ten gevolge van de verdeelde belasting en $A_{\rm{v}}$ in rekening te brengen. Hiervoor worden het vergeet-mij-nietje voor een uitkragende ligger met een verdeelde belasting en het vergeet-mij-nietje voor een uitkragende ligger belast door een puntlast gebruikt:

$$ w_{\rm{A}} \left( A_{\rm{v}} \right) = \varphi_{\rm{B}} \cdot 4 - \cfrac{25 \cdot 4^4}{8 \cdot \cfrac{16}{3} \cdot 10^3} + \cfrac{A_{\rm{v}} \cdot 4^3}{3 \cdot \cfrac{16}{3} \cdot 10^3}  =0.01 \cdot A_{\rm{v}} -0.45 $$

::::

% solution_end

:::::{exercise}
:label: balk_1_2
:nonumber: true

Los de vormveranderingsvoorwaarde op om $A_{\rm{v}}$ te vinden.

```{h5p} https://tudelft.h5p.com/content/1292636567761480237/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

De vormveranderingsvoorwaarde is: $w_{\rm{A}} = 0.01 \cdot A_{\rm{v}} -0.45 = 0$. 

Hieruit volgt $A_{\rm{v}} = 45 \rm{kN}$

::::

% solution_end

:::::{exercise}
:label: balk_1_3
:nonumber: true

Los nu de andere oplegreacties op en bepaal de momenten en verplaatsingen.

```{h5p} https://tudelft.h5p.com/content/1292636572692927547/embed
```

:::::

% solution_start

::::{admonition} Oplossing
:class: solution, dropdown

Nu $A_{\rm{v}}$ bekend is kunnen de andere oplegreacties worden opgelost, $B_{\rm{v}}$ en $C_{\rm{v}}$ worden omhoog positief aangenomen. De gebruikte vergelijkingen zijn:

$$ \sum \left. T \right|  _ {\rm{C}} = -45 \cdot 10 + 25 \cdot 4 \cdot 8 - B_{\rm{v}} \cdot 6 = 0 \rightarrow B_{\rm{v}} = 58.3 \rm{kN} $$ 

$$ \sum F_ {\rm{v}} = 45 - 4 \cdot 25 + 58.3 + C_{\rm{v}} = 0 \rightarrow C_{\rm{v}} = -3.3 \rm{kN} $$

$M_{\rm{B}}$ kan worden bepaald uit de momentensom om B van deel AB, dit geeft: $M_{\rm{B}} = - 20 \rm{kNm}$. $M_{\rm{halverwege \ AB}}$ kan op vergelijkbare wijze worden bepaald uit de momentensom om het punt halverwege AB: $M_{\rm{halverwege \ AB}} = 40 \rm{kNm}$. 

De zakking halverwege AB, $w_{\rm{halverwege} \ \rm{AB}}$, kan op verschillende manieren worden gevonden. Hier wordt deze bepaald met behulp van het het vergeet-mij-nietje voor een ligger op twee steunpunten belast door een koppel en het vergeet-mij-nietje voor een ligger op twee steunpunten met een verdeelde belasting. 

$$ w_{\rm{halverwege \ AB}} = \cfrac{5}{384} \cdot \cfrac{25 \cdot 4^4}{\cfrac{16}{3}} - \cfrac{1}{16} \cdot \cfrac{20 \cdot 4^2}{\cfrac{16}{3}} = 12 \rm{mm} $$

De zakking halverwege BC kan worden bepaald met behulp van het vergeet-mij-nietje voor een ligger op twee steunpunten belast door een koppel:

$$ w_{\rm{halverwege \ BC}} =  - \cfrac{1}{16} \cdot \cfrac{20 \cdot 6^2}{\cfrac{16}{3}} = -8 \rm{mm} $$

::::

% solution_end

