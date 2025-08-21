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
:label: raam_2_1
:nonumber: true

```{h5p} https://tudelft.h5p.com/content/1292652260765673357/embed
```


:::::

% solution_start

::::{solution} raam_2_1
:class: dropdown

```{figure} lesoefeningen_data/Onbekenden.svg
---
align: center
---
Er zijn 25 onbekende krachten
```

```{figure} lesoefeningen_data/Vergelijkingen.svg
---
align: center
---
Er zijn 22 evenwichtsvergelijkingen
```

Dus de constructie is 3de graads statisch onbepaald. 

::::

% solution_end

:::::{exercise}
:label: raam_2_2
:nonumber: true

Er zijn een aantal opties gegeven voor mogelijke statisch bepaalde systemen. De vormveranderingsvoorwaarden zijn niet getoond

```{h5p} https://tudelft.h5p.com/content/1292652255908105857/embed
```

:::::

% solution_start

::::{solution} raam_2_2
:class: dropdown

```{figure} lesoefeningen_data/Oplosmethode_optie1.svg
---
align: center
---
Juist
```

```{figure} lesoefeningen_data/Oplosmethode_optie2.svg
---
align: center
---
Onjuist
```

```{figure} lesoefeningen_data/Oplosmethode_optie3.svg
---
align: center
---
Juist
```

```{figure} lesoefeningen_data/Oplosmethode_optie4.svg
---
align: center
---
Juist
```

```{figure} lesoefeningen_data/Oplosmethode_optie5.svg
---
align: center
---
Onjuist
```

::::

% solution_end

:::::{exercise}
:label: raam_2_3
:nonumber: true

Er wordt gekozen voor het volgende statisch bepaalde systeem inclusief vormveranderingsvoorwaarden:

```{figure} ./lesoefeningen_data/structure2.svg
:align: center

Statisch bepaald systeem
```

Er is hier wederom een scharnier in een knoop geplaatst zoals ook in [het statisch bepaalde systeem van oefening 1](statisch_onbepaald_C). Bepaal de rotaties als functie van $M_{\rm{D}}$, $M_{\rm{B}}^{\rm{BD}}$, $M_{\rm{B}}^{\rm{AB}}$ en $M_{\rm{B}}^{\rm{BC}}$.

```{h5p} https://tudelft.h5p.com/content/1292652275086136557/embed
```

:::::

% solution_start

::::{solution} raam_2_3
:class: dropdown

De uitdrukkingen voor de hoekverdraaiingen worden gevonden met behulp van de vergeet-mij-nietjes voor een ligger op twee steunpunten belast door een koppel en door een verdeelde belasting, de positieve richtingen worden genomen zoals in de figuur aangegeven. 

$$ \varphi_{\rm{D}}^{\rm{AD}} \left( M_{\rm{D}}\right) = \cfrac{M_{\rm{D}} \cdot 6}{3 \cdot \cfrac{1000}{3}} = 0.006 \cdot M_{\rm{D}} $$
$$ \varphi_{\rm{D}}^{\rm{BD}} \left( M_{\rm{D}}, M_{\rm{B}}^{\rm{BD}} \right) = - \cfrac{M_{\rm{D}} \cdot 8}{3 \cdot \cfrac{1000}{3}} - \cfrac{M_{\rm{B}}^{\rm{BD}} \cdot 8}{6 \cdot \cfrac{1000}{3}} = -0.008 \cdot  M_{\rm{D}} -0.004 \cdot M_{\rm{B}}^{\rm{BD}} $$
$$ \varphi_{\rm{B}}^{\rm{BD}} \left( M_{\rm{D}}, M_{\rm{B}}^{\rm{BD}} \right) = - \cfrac{M_{\rm{D}} \cdot 8}{6 \cdot \cfrac{1000}{3}} - \cfrac{M_{\rm{B}}^{\rm{BD}} \cdot 8}{3 \cdot \cfrac{1000}{3}} = -0.004 \cdot  M_{\rm{D}} -0.008 \cdot M_{\rm{B}}^{\rm{BD}} $$
$$ \varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{B}}^{\rm{AB}} \right) = \cfrac{M_{\rm{B}}^{\rm{AB}} \cdot 10}{3 \cdot \cfrac{1000}{3}} = 0.01 \cdot M_{\rm{B}}^{\rm{AB}} $$
$$ \varphi_{\rm{B}}^{\rm{BC}} \left( M_{\rm{B}}^{\rm{BC}} \right) = \cfrac{M_{\rm{B}}^{\rm{BC}} \cdot 6}{3 \cdot \cfrac{1000}{3}} + \cfrac{11 \cdot 6^3}{24 \cdot \cfrac{1000}{3}} = 0.006 \cdot M_{\rm{B}}^{\rm{BC}} + 0.297 $$

::::

% solution_end

:::::{exercise}
:label: raam_2_4
:nonumber: true

Er mist nog een vergelijking om de vier onbekenden (waarvan 3 statisch onbepaalden) op te lossen. Wat is die vergelijking?

```{h5p} https://tudelft.h5p.com/content/1292652280843962007/embed
```

:::::

% solution_start

::::{solution} raam_2_4
:class: dropdown

$M_{\rm{B}}^{\rm{BD}} - M_{\rm{B}}^{\rm{AB}} - M_{\rm{B}}^{\rm{BC}}  = 0$

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

::::{solution} raam_2_5
:class: dropdown

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

::::{solution} raam_2_6
:class: dropdown

$$ M_{\rm{A}} = 0 \rm{kNm} $$
$$ M_{\rm{halverwege} \ \rm{BC}} = 34.75 \rm{kNm} (◡) $$ 
$$ N_{\rm{BD}} \approx 0.83  \rm{kN} $$
$$ B_{\rm{v}} \approx 41.60 \rm{kN} $$

::::

% solution_end
