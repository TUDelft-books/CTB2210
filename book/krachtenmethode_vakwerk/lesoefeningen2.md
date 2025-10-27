````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze oefening is aangepast van https://oit.tudelft.nl/CT1000/2024/week_3/session_3/intro.html

% source files at https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/krachtenmethode_vakwerk_2

```
```` 

# Begeleide oefening

Gegeven is de volgende constructie:

```{figure} lesoefeningen_2_data/structure.svg
:align: center

Constructie, $EA = 3750 \ \rm{kN}$
```

Bepaal de verplaatsingen van de knopen.

:::::{exercise}
:label: vakwerk_1_1
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292634971733883797/embed
```

:::::


::::{admonition} Solution
:class: solution, dropdown

De constructie is *1*ste/de graads inwendig statisch onbepaald

::::



:::::{exercise}
:label: vakwerk_1_2
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292634953266684027/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

- Weghalen horizontale oplegging bij B
- Weghalen verticale oplegging bij B
  - Inderdaad! Als je de hele oplegging weghaalt heb je een mechanisme kan roteren rondom A.
- Splitsen constructie in pendelstaaf AC
  -Inderdaad, als je deze pendelstaaf weghaalt krijg je een mechanisme wat kan roteren om A en B.
- Splitsen constructie in pendelstaaf AD
- Splitsen constructie in pendelstaaf CE
  - Inderdaad, als je deze pendelstaaf weghaalt krijg je een mechanisme wat kan roteren om A en B.
- Splitsen constructie in pendelstaaf DE
  - Inderdaad, als je deze pendelstaaf weghaalt krijg je een mechanisme wat kan roteren om A en B.
- Toevoegen scharnier halverwege CD
  - Inderdaad, als je deze pendelstaaf weghaalt krijg je een lokaal mechanisme wat kan roteren om C en D.

::::



:::::{exercise}
:label: vakwerk_1_3
:nonumber: true

We kiezen voor een statisch onbepaalde kracht $B_{\rm{h}}$ (naar links positief) met de vormveranderingsvoorwaarde $w_{\rm{B,h}} = 0 $.

```{figure} lesoefeningen_2_data/SD.svg
:align: center

Statisch bepaalde constructie met vormveranderingsvoorwaarde
```

Bepaal de normaalkrachten in alle staven als functie van $B_{\rm{h}}$.

```{h5p} https://tudelft.h5p.com/content/1292635090407938947/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

De staafkrachten worden opgelost, beginnende bij de krachten in de staven $\rm{BE}$ en $\rm{BD}$:

```{figure} lesoefeningen_2_data/FBD_B.svg
:align: center

Vrijlichaamsschema van knoop B $\rm{B}$
```

$$
\begin{array}{c}
\sum {{F_{\rm{v}}} = 0}  \to {N_{{\rm{BE}}}} = -6.25{\rm{ kN}}\\
\sum {{F_{\rm{h}}} = 0}  \to {N_{{\rm{BD}}}} =  3.75 - {B_{\rm{h}}}
\end{array}
$$

```{figure} lesoefeningen_2_data/FBD_B_sol.svg
:align: center

Vrijlichaamsschema van knoop $\rm{B}$ met de opgeloste staafkrachten
```

Vervolgens wordt een snede gemaakt door de staven $\rm{AD}$, $\rm{CD}$ en $\rm{CE}$:

```{figure} lesoefeningen_2_data/FBD_AC.svg
:align: center

Vrijlichaamsschema van deel $\rm{AC}$
```

$$
\begin{array}{c}
\sum {{F_{\rm{v}}} = 0}  \to {N_{{\rm{CD}}}} =  - 6.25{\rm{ kN}}\\
{\sum {\left. T \right|} _{\rm{D}}} = 0 \to {N_{CE}} =  - 7.5{\rm{ kN}}\\
\sum {{F_{\rm{h}}} = 0}  \to {N_{{\rm{AD}}}} = 11.25 - {B_{\rm{h}}}
\end{array}
$$

```{figure} lesoefeningen_2_data/FBD_AC_sol.svg
:align: center

Vrijlichaamsschema van deel $\rm{AC}$ met de berekende staafkrachten
```

Daarna wordt knoopevenwicht van $\rm{D}$ beschouwd:

```{figure} lesoefeningen_2_data/FBD_D.svg
:align: center

Vrijlichaamsschema van knoop $\rm{D}$
```

$$\sum {{F_{\rm{v}}} = 0}  \to {N_{{\rm{DE}}}} =  6.25{\rm{ kN}}$$

```{figure} lesoefeningen_2_data/FBD_D_sol.svg
:align: center

Vrijlichaamsschema van knoop $\rm{D}$ met de opgeloste staafkracht
```

En ten slotte knoop $\rm{C}$:

```{figure} lesoefeningen_2_data/FBD_C.svg
:align: center

Vrijlichaamsschema van knoop $\rm{C}$
```

$$\sum {{F_{\rm{v}}} = 0}  \to {N_{{\rm{AC}}}} =  - 18.75{\rm{ kN}}$$

```{figure} lesoefeningen_2_data/FBD_C_sol.svg
:align: center

Vrijlichaamsschema van knoop $\rm{C}$ met de opgeloste staafkracht
```


::::



:::::{exercise}
:label: vakwerk_1_4
:nonumber: true

Bepaal de verlenging/verkorting in alle staven als functie van $B_{\rm{h}}$.

```{h5p} https://tudelft.h5p.com/content/1292635092328991097/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

Nu kan voor elk element de verlenging / verkorting worden berekend:

$$\Delta L = \frac{{NL}}{{EA}} \to \begin{array}{c}
{\Delta {L_{{\rm{AC}}}} =  - 0.025 \ {\rm{ m}}}\\
{\Delta {L_{{\rm{CE}}}} =  - 0.012\ {\rm{ m}}}\\
{\Delta {L_{\rm{BE}}} = \cfrac{1}{{120}} \approx  - 0.00833\ {\rm{ m}}}\\
{\Delta {L_{{\rm{CD}}}} = \cfrac{1}{{120}} \approx  - 0.00833\ {\rm{ m}}}\\
{\Delta {L_{{\rm{DE}}}} = \cfrac{1}{{120}} \approx 0.00833 \ {\rm{ m}}}\\
{\Delta {L_{{\rm{AD}}}} = 0.018 - 0.0016{B_{\rm{h}}} \ {\rm{ m}}}\\
{\Delta {L_{{\rm{DB}}}} = 0.006 - 0.0016{B_{\rm{h}}} \ {\rm{ m}}}
\end{array}$$

::::


:::::{exercise}
:label: vakwerk_1_5
:nonumber: true

Om de verplaatsingen te vinden van de knopen kijken we afzonderlijk naar de invloed van de horizontale kracht $B_{\rm{h}}$ en van de belasting van $20 \ \rm{kN}$. Hiermee worden de Williot-diagrammetjes iets simpeler

We beginnen met de de belasting van $20 \ \rm{kN}$. Daarvoor reken we dus enkel met de volgende verkortingen/verlengingen:

$$\begin{array}{c}
{\Delta {L_{{\rm{AC}}}} =  - 0.025 \ {\rm{ m}}}\\
{\Delta {L_{{\rm{CE}}}} =  - 0.012\ {\rm{ m}}}\\
{\Delta {L_{\rm{BE}}} = \cfrac{1}{{120}} \approx  - 0.00833\ {\rm{ m}}}\\
{\Delta {L_{{\rm{CD}}}} = \cfrac{1}{{120}} \approx  - 0.00833\ {\rm{ m}}}\\
{\Delta {L_{{\rm{DE}}}} = \cfrac{1}{{120}} \approx 0.00833 \ {\rm{ m}}}\\
{\Delta {L_{{\rm{AD}}}} = 0.018 \ {\rm{ m}}}\\
{\Delta {L_{{\rm{DB}}}} = 0.006 \ {\rm{ m}}}
\end{array}$$

De verlengingen/verkortingen ten gevolge van de $20 \ \rm{kN}$ zijn deels gegeven:

| Scharnier | Verplaatsing in horizontale richting → (mm)| Verplaatsing in verticale richting ↓ (mm)|
| :-:|:-:|:-:|
|$\rm{A}$|$0$|$0$|
|$\rm{B}$|?|?|
|$\rm{C}$|$21$|$47$|
|$\rm{D}$|$18$|$\cfrac{233}{6} \approx 39$|
|$\rm{E}$|$9$|$\cfrac{65}{3} \approx 22$|

```{figure} lesoefeningen_2_data/displaced_incomplete.svg
:align: center

Deel van vervormde constructie statisch bepaalde constructie ten gevolge van 20 kN.
```

Bepaal de ontbrekende verplaatsing. Het beginnetje van het williot-diagram is gemaakt:

```{figure} lesoefeningen_2_data/incomplete_williot.svg
:align: center

Incompleet Williot diagram
```

```{h5p} https://tudelft.h5p.com/content/1292635136895634107/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} lesoefeningen_2_data/williot3.svg
:align: center

Williot diagram
```

::::



:::::{exercise}
:label: vakwerk_1_6
:nonumber: true

Nu gaan we het williot-diagram teken ten gevolge van $B_{\rm{h}}$. Daarvoor reken we dus enkel met de volgende verkortingen/verlengingen:

$$\begin{array}{c}
{\Delta {L_{{\rm{AC}}}} =  \Delta {L_{{\rm{CE}}}} = \Delta {L_{\rm{BE}}} = \Delta {L_{{\rm{CD}}}} = \Delta {L_{{\rm{DE}}}} = 0}\\
{\Delta {L_{{\rm{AD}}}} = - 0.0016{B_{\rm{h}}} \ {\rm{ m}}}\\
{\Delta {L_{{\rm{DB}}}} = - 0.0016{B_{\rm{h}}} \ {\rm{ m}}}
\end{array}$$

Bepaal op basis van deze verlengingen en verkortingen alle verplaatsingen met een apart williot-diagram. Neem daarvoor een zelf gekozen lengte aan voor $B_{\rm{h}}$ (bijvoorbeeld $4$ hokjes komt overeen met $1.6{B_{\rm{h}}}$). Houd daarnaast eerst $\rm{AD}$ in de horizontale oriëntatie zodat je die daarna kan terugdraaien.

```{h5p} https://tudelft.h5p.com/content/1292635148099409217/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

```{figure} lesoefeningen_2_data/williot2.svg
:align: center

Williot diagram
```

| Scharnier | Verplaatsing in horizontale richting → (mm)| Verplaatsing in verticale richting ↓ (mm)|
| :-:|:-:|:-:|
|$\rm{A}$|$0$|$0$|
|$\rm{C}$|$-0.8{B_{\rm{h}}}$|$-0.6{B_{\rm{h}}}$|
|$\rm{D}$|$-1.6{B_{\rm{h}}}$|$0$|
|$\rm{E}$|$-0.8{B_{\rm{h}}}$|$0.6{B_{\rm{h}}}$|
|$\rm{B}$|$-3.2{B_{\rm{h}}}$|$2.4{B_{\rm{h}}}$|

::::

:::::{exercise}
:label: vakwerk_1_6b
:nonumber: true

Als het goed is heb je gevonden dat $\rm{B}$ $2.4 B_{\rm{h}}$ verticaal naar beneden verplaatst. Draai onze vastgehouden $\rm{AD}$ nu zo terug dat $\rm{B}$ niet meer verticaal verplaatst.

```{h5p} https://tudelft.h5p.com/content/1292635150038900187/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

$\theta = \cfrac{2.4{B_{\rm{h}}}}{{12000}} = 0.0002{B_{\rm{h}}}{\rm{ rad}}$ ⟲, dit geeft:

| Scharnier | Verplaatsing in horizontale richting ten gevolge van rotatie → (mm)| Verplaatsing in verticale richting ten gevolge van rotatie ↓ (mm)|
| :-:|:-:|:-:|
|$\rm{A}$|$0$|$0$|
|$\rm{C}$|$-0.8 B_\rm{h}$|$-0.6 B_\rm{h}$|
|$\rm{D}$|$0$|$-1.2B_\rm{h}$|
|$\rm{E}$|$-0.8 B_\rm{h}$|$-1.8B_\rm{h}$|
|$\rm{B}$|$0$|$-2.4 B_\rm{h}$|

Resulteert in:

| Scharnier | Verplaatsing in horizontale richting → (mm)| Verplaatsing in verticale richting ↓ (mm)|
| :-:|:-:|:-:|
|$\rm{A}$|$0$|$0$|
|$\rm{C}$|$-1.6B_\rm{h}$|$-1.2B_\rm{h}$|
|$\rm{D}$|$-1.6{B_{\rm{h}}}$|$-1.2B_\rm{h}$|
|$\rm{E}$|$-1.6B_\rm{h}$|$-1.2B_\rm{h}$|
|$\rm{B}$|$-3.2B_\rm{h}$|$0$|

```{figure} lesoefeningen_2_data/displaced2.svg
:align: center

Constructie in verplaatste stand
```


::::



:::::{exercise}
:label: vakwerk_1_7
:nonumber: true


```{h5p} https://tudelft.h5p.com/content/1292635153881798987/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

$${w_{{\rm{B,h}}}} = 0 \to 24 - 3.2{B_{\rm{h}}} = 0 \to {B_{\rm{h}}} =  7.5{\rm{ kN}}$$

::::




:::::{exercise}
:label: vakwerk_1_8
:nonumber: true

Gebruik je resultaat om de normaalkrachten in alle staven te vinden.

```{h5p} https://tudelft.h5p.com/content/1292635156869126557/embed
```

:::::

::::{admonition} Solution
:class: solution, dropdown

| Element | Normaalkracht (kN)|
| :-:|:-:|
|$\rm{AC}$|-18.75|
|$\rm{CE}$|-7.5|
|$\rm{BE}$|-6.25|
|$\rm{CD}$|-6.25|
|$\rm{DE}$|6.25|
|$\rm{AD}$|3.75|
|$\rm{DB}$|-3.75|

```{figure} lesoefeningen_2_data/N-line.svg
:align: center

Normaalkrachtenlijn
```

::::




Als je alles goed hebt gedaan zou je op de volgende verplaatsingen uit moeten komen

| Scharnier | Verplaatsing in horizontale richting → (mm)| Verplaatsing in verticale richting ↓ (mm)|
| :-:|:-:|:-:|
|$\rm{A}$|$0$|$0$|
|$\rm{C}$|$9$|$38$|
|$\rm{D}$|$6$|$29.833$|
|$\rm{E}$|$-3$|$12.66$|
|$\rm{B}$|$0$|$0$|

```{figure} lesoefeningen_2_data/displaced3.svg
:align: center

Vervormde constructie
```
