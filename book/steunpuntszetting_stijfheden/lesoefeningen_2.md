````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze oefening is aangepast van https://github.com/TUDelft-books/CT1000 versie CTB2210-2025.
```
````

# Begeleide oefening 2

Gegeven is de volgende constructie:

```{figure} ./lesoefeningen_data/structure.svg
:align: center

Constructie
```

:::::{exercise}
:label: steun_2_1
:nonumber: true

Wat is de graad van statisch onbepaaldheid?

```{h5p} https://tudelft.h5p.com/content/1292654698994250327/embed
```

:::::

::::{solution} steun_2_1
:class: dropdown

De constructie is 2e graads inwendig statisch onbepaald. 

::::

:::::{exercise}
:label: steun_2_2
:nonumber: true

Voor het geval dat $nEI \to 0$, bepaal de krachtsverdeling en verplaatsingen:

```{h5p} https://tudelft.h5p.com/content/1292654700974801967/embed
```

:::::

::::{solution} steun_2_2
:class: dropdown

Als deel $\rm{BC}$ geen buigstijfheid meer heeft ontstaan er feitelijk twee losse liggertjes waarvan de linker 25 $\rm{mm}$ zakt. Dit levert de onderstaande krachten en verplaatsingen:

$$A_{\rm{v}} \left( nEI \to 0 \right) = 0 \rm{kN}$$
$$B_{\rm{v}} \left( nEI \to 0 \right) = 0 \rm{kN}$$
$$C_{\rm{v}} \left( nEI \to 0 \right) = 0 \rm{kN}$$
$$D_{\rm{v}} \left( nEI \to 0 \right) = 0 \rm{kN}$$
$$M_{\rm{B}} \left( nEI \to 0 \right) = 0 \rm{kNm}$$
$$M_{\rm{D}} \left( nEI \to 0 \right) = 0 \rm{kNm}$$
$$w_{\rm{halverwege} \ \rm{AB}} \left( nEI \to 0 \right) = 25 \rm{mm}$$
$$w_{\rm{halverwege} \ \rm{CD}} \left( nEI \to 0 \right) = 0 \rm{mm}$$

::::

:::::{exercise}
:label: steun_2_3
:nonumber: true

Voor het geval dat $nEI \to \infty$, kies zelf een statisch bepaald systeem met vormveranderingsvoorwaardes en bepaal de krachtsverdeling:

```{h5p} https://tudelft.h5p.com/content/1292654703279142367/embed
```

:::::

::::{solution} steun_2_3
:class: dropdown

Er wordt gekozen voor het onderstaande statisch bepaalde systeem, waarbij scharnieren en onbekende momentenparen zijn toegevoegd in $\rm{B}$ en $\rm{C}$. 

```{figure} ./lesoefeningen_data/SB_systeem1.svg
:align: center

Statisch bepaald systeem met onbekende momenten.  
```

De bijbehorende vormveranderingsvoorwaarden zijn:

$$\varphi_{\rm{B}}^{\rm{AB}}=\varphi_{\rm{B}}^{\rm{BC}}$$
$$\varphi_{\rm{C}}^{\rm{BC}}=\varphi_{\rm{C}}^{\rm{CD}}$$

Omdat deel $\rm{BC}$ oneindig stijf is geldt: $\varphi_{\rm{B}}^{\rm{BC}}=\varphi_{\rm{C}}^{\rm{BC}}=\cfrac{25}{10000}=0.0025\rm{rad}$

Met behulp van het vergeet-mij-nietje voor een ligger op twee steunpunten belast door een koppel wordt het volgende gevonden: $\varphi_{\rm{B}}^{\rm{AB}}=\cfrac{M_{\rm{B}}\cdot10}{3\cdot\cfrac{250}{3}\cdot1000} \rightarrow M_{\rm{B}}=62.5 \rm{kNm}$

Uit momentenevenwicht van deel $\rm{AB}$ volgt: $\sum \left. T \right| _ {\rm{B}} ^{\rm{AB}} = - A_{\rm{v}} \cdot 10 + 62.5=0 \rightarrow A_{\rm{v}} =6.25 \rm{kN}$

Uit symmetrie volgt: $M_{\rm{C}}=-M_{\rm{B}}=-62.5 \rm{kNm}$ en $D_{\rm{v}}=-A_{\rm{v}}=-6.25 \rm{kN}$

Met momentenevenwicht van de hele constructie kan nu worden bepaald dat $B_{\rm{v}}=-18.75 \rm{kN}$ en $C_{\rm{v}}=18.75 \rm{kN}$.  

De zakkingen in het midden van de delen $\rm{AB}$ en $\rm{CD}$ kunnen worden bepaald uit de superpositie van de vervorming door buiging en de zakking van de opleggingen. 

$$w_{\rm{halverwege} \ \rm{AB}} = 25 + \cfrac{62.5\cdot 10^2}{16\cdot\cfrac{250}{3}}=29.6875 \rm{mm}$$
$$w_{\rm{halverwege} \ \rm{CD}} = - \cfrac{62.5\cdot 10^2}{16\cdot\cfrac{250}{3}}=-4.6875 \rm{mm}$$

::::

:::::{exercise}
:label: steun_2_4
:nonumber: true

Voor het geval van variabele $n$ is het volgende statisch bepaalde systeem:

```{figure} ./lesoefeningen_data/SB.svg
:align: center

Constructie
```

```{h5p} https://tudelft.h5p.com/content/1292654763617550697/embed
```

:::::

::::{solution} steun_2_4
:class: dropdown

De vormveranderingsvoorwaardes zijn:

$$w_{\rm{A}}=25 \rm{mm}$$
$$w_{\rm{D}}=0 \rm{mm}$$

::::

:::::{exercise}
:label: steun_2_5
:nonumber: true

Bepaal de krachtsverdeling en verplaatsingen als $A_{\rm{v}}$ en $D_{\rm{v}}$ gelijk zijn aan 0

```{h5p} https://tudelft.h5p.com/content/1292654762901470137/embed
```

:::::

::::{solution} steun_2_5
:class: dropdown

Als $A_{\rm{v}}$ en $D_{\rm{v}}$ gelijk zijn aan 0 dan kan de constructie vrij vervormen en onstaat er geen buiging. Hieruit volgt:

$$ M_{\rm{B}} \left( A_{\rm{v}} = D_{\rm{v}} = 0 \right) = 0 \rm{kNm} $$
$$ M_{\rm{C}} \left( A_{\rm{v}} = D_{\rm{v}} = 0 \right) = 0 \rm{kNm} $$
$$ \varphi_{\rm{B}} \left( A_{\rm{v}} = D_{\rm{v}} = 0 \right) = 0.0025 \rm{rad} $$
$$ \varphi_{\rm{C}} \left( A_{\rm{v}} = D_{\rm{v}} = 0 \right) = 0.0025 \rm{rad} $$
$$ w_{\rm{A}} \left( A_{\rm{v}} = D_{\rm{v}} = 0 \right) = 50 \rm{mm} $$
$$ w_{\rm{D}} \left( A_{\rm{v}} = D_{\rm{v}} = 0 \right) = -25 \rm{mm} $$

::::

:::::{exercise}
:label: steun_2_6
:nonumber: true

Bepaal de krachtsverdeling en verplaatsingen als functie van $A_{\rm{v}}$ en $D_{\rm{v}}$.

```{h5p} https://tudelft.h5p.com/content/1292654774240819917/embed
```

:::::

::::{solution} steun_2_6
:class: dropdown

De momenten $M_{\rm{B}}$ en $M_{\rm{C}}$ kunnen worden bepaald door respectievelijk $A_{\rm{v}}$ en $D_{\rm{v}}$ te verplaatsen naar $\rm{B}$ en $\rm{C}$. 

$$M_{\rm{B}} = 10 \cdot A_{\rm{v}}$$
$$M_{\rm{C}} = 10 \cdot D_{\rm{v}}$$

De hoekverdraaiingen in $\rm{B}$ en $\rm{C}$ kunnen worden bepaald uit een superpositie van de vervorming door buiging en de vrije vervorming zoals in de vorige opgave berekend. Voor de vervorming door buiging wordt het vergeet-mij-nietje voor een ligger op twee steunpunten belast door een koppel gebruikt. 

$$ \varphi_{\rm{B}} \left( A_{\rm{v}}, D_{\rm{v}} \right) = -\cfrac{10 \cdot A_{\rm{v}} \cdot 10}{3 \cdot \cfrac{250}{3} \cdot n\cdot 1000} - \cfrac{10 \cdot D_{\rm{v}} \cdot 10}{6 \cdot \cfrac{250}{3} \cdot n\cdot 1000} + 0.0025 = -0.0004 \cdot \cfrac{A_{\rm{v}}}{n} -0.0002 \cdot \cfrac{D_{\rm{v}}}{n} + 0.0025 $$
$$ \varphi_{\rm{C}} \left( A_{\rm{v}}, D_{\rm{v}} \right) = \cfrac{10 \cdot A_{\rm{v}} \cdot 10}{6 \cdot \cfrac{250}{3} \cdot n\cdot 1000} + \cfrac{10 \cdot D_{\rm{v}} \cdot 10}{3 \cdot \cfrac{250}{3} \cdot n\cdot 1000} + 0.0025 = 0.0002 \cdot \cfrac{A_{\rm{v}}}{n} + 0.0004 \cdot \cfrac{D_{\rm{v}}}{n} + 0.0025 $$

De zakkingen in $\rm{A}$ en $\rm{D}$ kunnen worden bepaald uit de superpositie van vrije vervorming van de constructie, vervorming door buiging van deel $\rm{BC}$ en vervorming door buiging van de delen $\rm{AB}$ en $\rm{CD}$. 

$$ w_{\rm{A}} \left( A_{\rm{v}}, D_{\rm{v}} \right) = 0.05 + 10 \cdot \left( -0.0004 \cdot \cfrac{A_{\rm{v}}}{n} -0.0002 \cdot \cfrac{D_{\rm{v}}}{n} \right) - \cfrac{ A_{\rm{v}} \cdot 10^3}{3 \cdot \cfrac{250}{3} \cdot 1000} =-0.004  \cdot A_{\rm{v}} -0.004 \cdot \cfrac{A_{\rm{v}}}{n} -0.002 \cdot \cfrac{D_{\rm{v}}}{n} + 0.05 $$
$$ w_{\rm{D}} \left( A_{\rm{v}}, D_{\rm{v}} \right) = -0.025 - 10 \cdot \left( 0.0002 \cdot \cfrac{A_{\rm{v}}}{n} + 0.0004 \cdot \cfrac{D_{\rm{v}}}{n} \right) - \cfrac{ D_{\rm{v}} \cdot 10^3}{3 \cdot \cfrac{250}{3} \cdot 1000} =-0.002 \cdot \cfrac{A_{\rm{v}}}{n} + -0.004 \cdot D_{\rm{v}} + -0.004\cdot \cfrac{D_{\rm{v}}}{n} -0.025 $$

::::

:::::{exercise}
:label: steun_2_7
:nonumber: true

Los met de vormveranderingsvoorwaardes de onbekende $A_{\rm{v}}$ en $D_{\rm{v}}$ op. Let op, dit is een lastige wiskundige exercitie. Je wordt aangeraden gebruik te maken van een tool zoals SymPy.


```{h5p} https://tudelft.h5p.com/content/1292654782286977977/embed
```

:::::

::::{solution} steun_2_7
:class: dropdown

Oplossen van de vergelijkingen levert:

$$ A_{\rm{v}}= \cfrac{25 \cdot n}{4 \cdot n + 2} $$
$$ D_{\rm{v}}= -\cfrac{25 \cdot n}{4 \cdot n + 2} $$

Deze functies kunnen ook geplot worden:

```{figure} lesoefeningen_data/steunpuntszetting.svg
---
align: center
---
Oplegreacties als functie van $n$
```

::::
