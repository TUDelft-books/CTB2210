````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze oefening is aangepast van https://github.com/TUDelft-books/CT1000 versie CTB2210-2025.
```
````

# Begeleide oefening 1

Gegeven is de volgende constructie:

```{figure} ./lesoefeningen_data/structure2.svg
:align: center

Constructie
```

:::::{exercise}
:label: steun_1_1
:nonumber: true

Gegeven is de volgende uitwerking:

$N_{\rm{BD}} = \cfrac{90}{6000} \cdot 15000 = 225 \ \rm{kN}$

Evenwicht van knoop D levert:
- $ N_{\rm{AD}} = -281.25 \ \rm{kN}$
- $ N_{\rm{CD}} = -168.75 \ \rm{kN}$

Hieruit volgt:
- $\Delta L_{\rm{AD}} = \cfrac{-281.25 \cdot 15000}{10} = -0.140625 \ \rm{m}$
- $\Delta L_{\rm{CD}} = \cfrac{-168.75 \cdot 15000}{6} = - 0.0675 \ \rm{m}$

Met als resultaat:
- Horizontale verplaatsing van $\rm{D}$ van $67.5 \ \rm{mm}$ naar rechts
- Verticale verplaatsing van $\rm{D}$ van $140.625 \cdot \cfrac{4}{5} = 112.5 \ \rm{mm} $ naar beneden

```{h5p} https://tudelft.h5p.com/content/1292653910239346277/embed
```

:::::

::::{solution} steun_1_1
:class: dropdown

- De normaalkracht in \(\rm{BD}\) is niet juist berekend
  - De verlenging van \(\rm{BD}\) is niet enkel afhankelijk van de verplaatsing van knoop \(\rm{B}\)
- De normaalkrachten in \(\rm{AD}\) en \(\rm{CD}\) zijn niet juist berekend
- De verlengingen van de staven \(\rm{AD}\) en \(\rm{CD}\) zijn niet juist berekend
- De verplaatsing van knoop \(\rm{D}\) is niet juist berekend
  - Om de verplaatsing van knoop \(\rm{D}\) te berekenen dient Williot te worden gebruikt

::::

:::::{exercise}
:label: steun_1_2
:nonumber: true

Wat is de graad van statisch onbepaaldheid?

```{h5p} https://tudelft.h5p.com/content/1292653934022070767/embed
```

:::::

::::{solution} steun_1_2
:class: dropdown

```{figure} ./lesoefeningen_data/Onbekenden.svg
:align: center

Er zijn 6 onbekende krachten. 
```

```{figure} ./lesoefeningen_data/Vergelijkingen.svg
:align: center

Er zijn 5 evenwichtsvergelijkingen. 
```

De constructie is 1ste graads inwendig statisch onbepaald. 

::::

:::::{exercise}
:label: steun_1_3
:nonumber: true

Gekozen is het volgende statisch bepaalde systeem met vormveranderingsvoorwaarde:

```{figure} ./lesoefeningen_data/statically_determinate2.svg
:align: center

Constructie
```

Er is gekozen voor dit systeem zodat we de steunpuntszetting in de vormveranderingsvoorwaarde mee kunnen nemen en niet mee hoeven te nemen in bepalen van krachtsverdeling.

Bepaal de krachtsverdeling en vervormingen als functie van $B_{\rm{v}}$. Neem in je Williot-diagram een zelf gekozen lengte aan voor $B_{\rm{v}}$. 

```{h5p} https://tudelft.h5p.com/content/1292653940023500187/embed
```

:::::

::::{solution} steun_1_3
:class: dropdown

De normaalkrachten in de staven AD en CD kunnen met behulp van het knoopevenwicht van $\rm{D}$ worden uitgedrukt in $B_{\rm{v}}$. 

$$ N_{\rm{BD}} = B_{\rm{v}} $$
$$ \sum F_{\rm{v}} = 0 \rightarrow N_{\rm{AD}} = - \cfrac{5}{4} \cdot B_{\rm{v}} $$
$$ \sum F_{\rm{h}} = 0 \rightarrow N_{\rm{CD}} = - \cfrac{3}{4} \cdot B_{\rm{v}} $$

Nu de normaalkrachten in de staven bekend zijn kan de verlenging/verkorting per staaf worden bepaald. De resultaten zijn weergegeven in de onderstaande tabel. 

| Staaf | $N\left(B_{\rm{v}}\right)$ (kN)| $\Delta L \left(B_{\rm{v}}\right)\rm{(mm)}$ |
| :-:|:-:|:-:|
|$\rm{AD}$|$-\cfrac{5}{4} \cdot B_{\rm{v}}$|$-\cfrac{5}{8} \cdot B_{\rm{v}}$|
|$\rm{BD}$|$B_{\rm{v}}$|$\cfrac{2}{5} \cdot B_{\rm{v}}$|
|$\rm{CD}$|$- \cfrac{3}{4} \cdot B_{\rm{v}}$|$-\cfrac{3}{10} \cdot B_{\rm{v}}$|

Met behulp van de berekende verlenging/verkorting kan het williot diagram worden getekend, zie de figuur hieronder. 

```{figure} lesoefeningen_data/williot.svg
---
align: center
---
Williot diagram voor het bepalen van de verplaatsing van $\rm{D}$ en $\rm{B}$.
```
Uit het williot diagram kan worden afgelezen:

$$ w_{D,\rm{h}} = 0.0003 \cdot B_{\rm{v}} \ \rm{m} \left(\rightarrow\right)$$
$$ w_{D,\rm{v}} \approx 0.001 \cdot B_{\rm{v}} \\rm{m} \left(\downarrow\right)$$
$$ w_{B,\rm{h}} = 0 $$
$$ w_{B,\rm{v}} \approx 0.0014 \cdot B_{\rm{v}} \ \rm{m} \left(\downarrow\right)$$

::::

:::::{exercise}
:label: steun_1_4
:nonumber: true

Los met de vormveranderingsvoorwaarde de onbekende $B_{\rm{v}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292654002392449027/embed
```

:::::

::::{solution} steun_1_4
:class: dropdown

De vormveranderingsvoorwaarde is: $w_{B,\rm{v}} = 1.4 \cdot B_{\rm{v}} = 90 \rm{mm}$.

Hieruit volgt: $B_{\rm{v}} = 64 \rm{kN}$

::::

:::::{exercise}
:label: steun_1_5
:nonumber: true

Los de volledige krachtsverdeling en verplaatsingen op.

```{h5p} https://tudelft.h5p.com/content/1292654005235840357/embed
```

:::::

::::{solution} steun_1_5
:class: dropdown

De krachten en verplaatsingen kunnen worden opgelost uit de eerder opgestelde vergelijkingen door daar de berekende waarde voor $B_{\rm{v}}$ in in te vullen.

$$ N_{\rm{BD}}= 64 \rm{kN} $$
$$ N_{\rm{AD}}= -80 \rm{kN} $$
$$ N_{\rm{CD}}= -48 \rm{kN} $$
$$ w_{D,\rm{h}} = 19 \rm{mm} \left(\rightarrow\right)$$
$$ w_{D,\rm{v}} = 64 \rm{mm} \left(\downarrow\right)$$
$$ w_{B,\rm{h}} = 0 \rm{mm} $$
$$ w_{B,\rm{v}} = 90 \rm{mm} \left(\downarrow\right)$$

::::
