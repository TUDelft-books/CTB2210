````{margin}
```{attributiongrey} Attribution
:class: attribution

Deze oefeningen zijn aangepast van https://github.com/TUDelft-books/CT1000 versie CTB2210-2025.
```
````

# Begeleid oefenen

Nu gaan we aan de slag met een oefening.

## Oefening 1

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

Equilibrium around node $\rm{D}$ gives:
- $ N_{\rm{AD}} = -281.25 \ \rm{kN}$
- $ N_{\rm{CD}} = -168.75 \ \rm{kN}$

This gives:
- $\Delta L_{\rm{AD}} = \cfrac{-281.25 \cdot 15000}{10} = -0.140625 \ \rm{m}$
- $\Delta L_{\rm{CD}} = \cfrac{-168.75 \cdot 15000}{6} = - 0.0675 \ \rm{m}$

Resulting in a:
- Horizontal displacement of $\rm{D}$ of $67.5 \ \rm{mm}$ to the right
- Vertical displacement of $\rm{D}$ of $140.625 \cdot \cfrac{4}{5} = 112.5 \ \rm{mm} $ downwards

```{h5p} https://tudelft.h5p.com/content/1292653910239346277/embed
```

:::::

:::::{exercise}
:label: steun_1_2
:nonumber: true

Wat is de graad van statisch onbepaaldheid?

```{h5p} https://tudelft.h5p.com/content/1292653934022070767/embed
```

:::::

:::::{exercise}
:label: steun_1_3
:nonumber: true

Gekozen is het volgende statisch bepaalde systeem met vormveranderingsvoorwaarde:

```{figure} ./lesoefeningen_data/statically_determinate2.svg
:align: center

Constructie
```

Er is gekozen voor dit systeem zodat we de steunpuntszetting in de vormveranderingsvoorwaarde mee kunnen nemen en niet mee hoeven te nemen in bepalen van krachtsverdeling.

Bepaal de krachtsverdeling en vervormingen als functie van $B_{\rm{v}}$. Neem in je Williot-diagram eem zelf gekozen lengte aan voor $B_{\rm{v}}$. Je kan de exacte waardes vinden uit de williot diagram.

```{h5p} https://tudelft.h5p.com/content/1292653940023500187/embed
```

:::::

::::{solution} steun_1_3
:class: dropdown

Nog aanvullen

```{figure} lesoefeningen_data/williot.svg
---
align: center
---
Williot diagram voor het bepalen van de verplaatsing van $\rm{D}$ en $\rm{B}$.
```

::::

:::::{exercise}
:label: steun_1_4
:nonumber: true

Los met de vormveranderingsvoorwaarde de onbekende $B_{\rm{v}}$ op.

```{h5p} https://tudelft.h5p.com/content/1292654002392449027/embed
```

:::::

:::::{exercise}
:label: steun_1_5
:nonumber: true

Los de volledige krachtsverdeling en verplaatsingen op.

```{h5p} https://tudelft.h5p.com/content/1292654005235840357/embed
```

:::::

## Oefening 2

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

:::::{exercise}
:label: steun_2_2
:nonumber: true

Voor het geval dat $nEI \to 0$, bepaal de krachtsverdeling en verplaatsingen:

```{h5p} https://tudelft.h5p.com/content/1292654700974801967/embed
```

:::::

:::::{exercise}
:label: steun_2_3
:nonumber: true

Voor het geval dat $nEI \to \infty$, kies zelf een statisch bepaald systeem met vormveranderingsvoorwaardes en bepaal de krachtsverdeling:

```{h5p} https://tudelft.h5p.com/content/1292654703279142367/embed
```

:::::

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

:::::{exercise}
:label: steun_2_5
:nonumber: true

Bepaal de krachtsverdeling en verplaatsingen als $A_{\rm{v}}$ en $D_{\rm{v}}$ gelijk zijn aan 0

```{h5p} https://tudelft.h5p.com/content/1292654762901470137/embed
```

:::::

:::::{exercise}
:label: steun_2_6
:nonumber: true

Bepaal de krachtsverdeling en verplaatsingen als functie van $A_{\rm{v}}$ en $D_{\rm{v}}$.

```{h5p} https://tudelft.h5p.com/content/1292654774240819917/embed
```

:::::

:::::{exercise}
:label: steun_2_7
:nonumber: true

Los met de vormveranderingsvoorwaardes de onbekende $A_{\rm{v}}$ en $D_{\rm{v}}$ op. Let op, dit is een lastige wiskundige exercitie. Je wordt aangeraden gebruik te maken van een tool zoals SymPy.


```{h5p} https://tudelft.h5p.com/content/1292654782286977977/embed
```

:::::

::::{solution} steun_2-7
:class: dropdown

Nog aanvullen

Deze functies kunnen ook geplot worden:

```{figure} lesoefeningen_data/steunpuntszetting.svg
---
align: center
---
Oplegreacties als functie van $n$
```

::::