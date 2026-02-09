# 26 januari: Tentamenopdracht


Je eigen indiening en de beoordeling daarvan is hier te vinden: [<img height="12px" src="../figures/ANS.svg" alt="ANS"> tentamenopdracht Statisch onbepaalde constructies](https://ans.app/universities/1/courses/577550/assignments/1629414/go_to).

Gegeven is de volgende constructie:

```{figure} ./exam_data/constructie.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam_SOB_2
```

:::::{exercise}
:nonumber: true

Laat zien dat deze constructie enkelvoudig statisch onbepaald is.

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Voor deze constructie is de inwendige statisch onbepaaldheid gelijk aan de uitwendig statisch onbepaaldheid, dat hoeft niet expliciet benoemd te worden. Beide aanpakken zijn correct. In dit geval komt de berekening 5 onbekende oplegreacties - 1 scharnieren - 3 evenwichtsvergelijkingen ook uit, dus wordt ook goed gerekend.

```{figure} ./exam_data/splitsen.svg
:align: center
```

Er zijn 5 onbekenden en 4 evenwichtsvergelijkingen, daarmee is de constructie enkelvoudig statisch onbepaald.

::::

:::::{exercise}
:nonumber: true

Geef vier geldige varianten om deze constructie statisch bepaald te maken ten behoeve van de krachtenmethode of verplaatsingenmethode met statisch onbepaalde verplaatsingen. Geef bij elk van de varianten aan wat je statisch onbepaalde kracht(en) is/zijn.

De volgende variant is al gegeven en kan dus niet één van de vier varianten zijn:

```{figure} ./exam_data/geen_optie.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam_SOB_2
```

Zorg voor vier verschillende varianten: je aanpassingen moeten elk een ander onderdeel van de constructie aanpassen.

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Een aantal mogelijk opties zijn:

```{figure} ./exam_data/variant1.svg
:align: center
```

```{figure} ./exam_data/variant2.svg
:align: center
```

```{figure} ./exam_data/variant3.svg
:align: center
```

```{figure} ./exam_data/variant4.svg
:align: center
```

::::

Gegeven is de volgende statisch bepaalde variant, waarbij de vormveranderingsvoorwaarde nog niet bepaald is.

```{figure} ./exam_data/statisch_bepaald.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam_SOB_2
```

:::::{exercise}
:nonumber: true

Bepaal met de gegeven statisch bepaalde variant het moment in $\rm{A}$ met behulp van de krachtenmethode.

:::::

::::{admonition} Oplossing
:class: solution, dropdown

De vormveranderingsvoorwaarde is dat de rotatie in $\rm{A}$ gelijk is aan nul: $\varphi_{\rm{A}} = 0$.

Als eerste wordt de invloed van de extensie van $\rm{BC}$ op de rotatie in $\rm{A}$ bepaald.

```{figure} ./exam_data/phi_1.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam_SOB_2
```

Evenwicht geeft:

```{figure} ./exam_data/VLS_AC.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam_SOB_2
```

$$
\sum {T_{\rm{A}}} = 0 \to N_{\rm{BC}} = -50 + \frac{1}{3} \cdot A_{\rm{m}}
$$

Verlenging van een staaf geeft:

$$
\Delta L_{\rm{BC}} = -\cfrac{3}{64} + \cfrac{1}{3200} \cdot A_{\rm{m}}
$$

Williot geeft:

```{figure} ./exam_data/williot.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam_SOB_2
```

$$
w_{\rm{B}} = -\cfrac{5}{64} + \cfrac{3}{16000} \cdot A_{\rm{m}} \, \left( \uparrow \right)
$$

Aanname van kleine rotaties geeft:

$$
\varphi_{\rm{A,} \, \rm{t.g.v.} \, \rm{extensie} \, \rm{BC}} = - \frac{1}{64} + \cfrac{1}{9600} \cdot A_{\rm{m}} \, \left( \circlearrowleft \right)
$$

Vervolgens kan ook de invloed van de buiging van $\rm{AB}$ ten gevolge van $\rm{A}$ bepaald worden.

```{figure} ./exam_data/phi_2.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam_SOB_2
```

Vergeet-me-nietje geeft:

$$
\varphi_{\rm{A,} \, \rm{t.g.v.} \, \rm{buiging} \, \rm{AC} \, \rm{t.g.v.} \, \rm{A_{\rm{m}}}} = \cfrac{1}{12000} \cdot A_{\rm{m}} \, \left( \circlearrowleft \right)
$$

En tot slot de invloed van de buiging van $\rm{AB}$ ten gevolge van de verdeelde belasting.

```{figure} ./exam_data/phi_3.svg
:align: center
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam_SOB_2
```

Vergeet-me-nietje geeft:

$$
\varphi_{\rm{A,} \, \rm{t.g.v.} \, \rm{buiging} \, \rm{AC} \, \rm{t.g.v.} \, \rm{verdeelde} \, \rm{belasting}} = \cfrac{1}{320} \, \left( \circlearrowright \right)
$$

De vormveranderingsvoorwaarde kan nu worden opgesteld:

$$
\begin{align*}
0 &= \varphi_{\rm{A}} \\
0 &= \varphi_{\rm{A,} \, \rm{t.g.v.} \, \rm{extensie} \, \rm{BC}} + \varphi_{\rm{A,} \, \rm{t.g.v.} \, \rm{buiging} \, \rm{AC} \, \rm{t.g.v.} \, \rm{A_{\rm{m}}}} - \varphi_{\rm{A,} \, \rm{t.g.v.} \, \rm{buiging} \, \rm{AC} \, \rm{t.g.v.} \, \rm{verdeelde} \, \rm{belasting}} \\
0 &= - \cfrac{3}{160} + \cfrac{3}{16000} \cdot A_{\rm{m}} \\
A_{\rm{m}} &= 100 \, \rm{kNm} \, \left( ◠ \right)
\end{align*}
$$

::::

:::::{exercise}
:nonumber: true

Geef aan hoe je deze constructie zou kunnen oplossen met de verplaatsingenmethode met vrijheidsgraden:
- Welke vrijheidsgraad/vrijheidsgraden definieer je?
- Welk(e) vergeet-me-nietje(s) heb je bij die vrijheidsgraad/vrijheidsgraden dan nodig om de constructie op te lossen?

Je hoeft geen berekeningen te maken.

:::::

::::{admonition} Oplossing
:class: solution, dropdown

Twee onafhankelijke vrijheidsgraden:
- Verticale verplaatsing van $\rm{C}$
- Rotatie van staaf $\rm{AC}$ in uiteinde $\rm{B}$

Met bijbehorende vergeet-me nietjes voor $\rm{AC}$:

  - Voor invloed van verdeelde belasting op dwarskracht net links van $\rm{C}$. 

    ```{figure} ./exam_data/VMN_1.svg
    :align: center
    :source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam_SOB_2
    ```

  - Voor invloed van rotatie van $\rm{C}$

    ```{figure} ./exam_data/VMN_2.svg
    :align: center
    :source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam_SOB_2
    ```

  - Voor invloed van verplaatsing van $\rm{C}$.

    ```{figure} ./exam_data/VMN_3.svg
    :align: center
    :source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/exam_SOB_2
    ```

Voor $\rm{BC}$ is geen vergeet-me-nietje nodig.

::::
