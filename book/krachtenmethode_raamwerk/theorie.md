# Theorie

![alt text](image.png)

De krachtenmethode hebben we eerder al behandeld voor onder andere [constructies belast op rek](krachtenmethode_simpel) en [balken](krachtenmethode_balk). Voor raamwerken is de procedure niet anders, behalve dat we het gedrag van rek en buiging niet altijd kunnen splitsen.

We behandelen de toepassing op raamwerkconstructies met het volgende voorbeeld. 

::::::{prf:example}
:nonumber: true
:label: sd_raam_0

```{figure} ./theorie_data/example.svg
---
align: center
---
Voorbeeldconstructie
```

::::::

1. Bepaal de graad van statische bepaaldheid.

::::::{prf:example}
:nonumber: true
:label: sd_raam_1

Voor ons voorbeeld zijn we geïnteresseerd in de verdeling van inwendige krachten, dus moeten we de graad van inwendige statische onbepaaldheid evalueren.

```{figure} ./theorie_data/onbekenden.svg
---
align: center
---
Er zijn 21 onbekende krachten.
```

```{figure} ./theorie_data/vergelijkingen.svg
---
align: center
---
Er zijn 19 evenwichtsvergelijkingen
```

Deze constructie is dus 2e orde inwendig statisch onbepaald.

::::::

2. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij een pendelstaaf, of scharnieren toe te voegen: voeg onbekende statisch onbepaalde krachten en vervormingsvoorwaardes toe voor elke opleggging die je hebt weggenomen en scharnieren die je hebt toegevoegd. Let op dat je de constructie niet transformeert tot een (gedeeltelijk) mechanisme!

::::::{prf:example}
:nonumber: true
:label: sd_raam_2

Er zijn veel opties, waarvan een aantal mogelijke opties:

`````{tab-set}
````{tab-item} Horizontale oplegging bij $\rm{B}$ loslaten en scharnier toevoegen in $\rm{B}$
```{figure} ./theorie_data/optie1.svg
:align: center
```
````
````{tab-item} Horizontale oplegging bij $\rm{B}$ en $\rm{C}$ loslaten
```{figure} ./theorie_data/optie2.svg
:align: center
```

````
````{tab-item} Horizontale en verticale oplegging bij $\rm{A}$ loslaten
```{figure} ./theorie_data/optie3.svg
:align: center
```
````
````{tab-item} Horizontale oplegging bij $\rm{A}$ loslaten en scharnier toevoegen in $\rm{B}$
```{figure} ./theorie_data/optie4.svg
:align: center
```
````
`````

De derde optie wordt gekozen.

::::::

3. Los de verplaatsing op in termen van de onbekende onbepaalde krachten zoals je normaal zou doen voor een statisch bepaalde constructie.

::::::{prf:example}
:nonumber: true
:label: sd_raam_4

We hebben de volgende statisch bepaalde constructie gekozen met vormveranderingsvoorwaardes $w_{\rm{A,v}}\left( A_{\rm{v}}, A_{\rm{h}} \right) = 0 $ en $w_{\rm{A,h}}\left( A_{\rm{v}}, A_{\rm{h}} \right) = 0 $:

```{figure} ./theorie_data/SB-systeem.svg
---
align: center
---
De statisch bepaalde constructie met vormveranderingsvoorwaarde
```

De krachtsverdeling kan worden gevonden met evenwicht:

- $M_{\rm{C}} = 90 \ \rm{kNm}$ (◠/ᑐ)
- $M_{\rm{B}} = 6A_{\rm{v}}$ (◡/ᑐ)

Met behulp van de vergeet-mij-nietjes kunnen de rotaties nu worden geëvalueerd:

- $\varphi_{\rm{B}} = 0.0012 A_{\rm{v}} - 0.018$
- $w_{\rm{A}} = 0.0216 A_{\rm{v}} - 0.108$

Aangezien $EA = \infty$ is de $w_{\rm{A,h}} = 0$ ... hmmm, dit werkt niet xd

::::::

4. Gebruik je vormveranderingsvoorwaarden om de statisch onbepaalde krachten op te lossen

::::::{prf:example}
:nonumber: true
:label: sd_raam_5

$$
\begin{align*}
\varphi_{\rm{B}}^{\rm{AB}} \left( M_{\rm{B}} \right) &= \varphi_{\rm{B}}^{\rm{BC}} \left( M_{\rm{B}} \right) \\
\cfrac{4M_{\rm{B}}}{3EI} + \cfrac{200}{3EI} &= -\cfrac{2M_{\rm{B}}}{3EI} \\
M_{\rm{B}} &= -20 \ \rm{kNm}
\end{align*}
$$
::::::

## Meer voorbeelden

nog aanpassen....

Het algemene concept van de krachtenmethode wordt behandeld in hoofdstuk 2.1 terwijl de krachtenmethode voor vakwerkconstructies wordt behandeld in hoofdstuk 2.2.1 - 2.2.7 en de meer specifieke 'hoekveranderingsvergelijkingen' in hoofdstuk 3.1 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.

Wanneer het boek de 'momentenvlakstelling' noemt in voorbeeld 2.2.6 en 2.2.7, kun je de verplaatsingen ook vinden met behulp van vergeet-mij-nietjes. De methode met verplaatsbare knopen ('hoekveranderingsvergelijkingen met verplaatsbare knopen') die in het verleden werd onderwezen wordt niet meer behandeld.

## Opdrachten
nog aanpassen

- Opgaven 2.1 - 2.30, 2.42 - 2.48, in hoofdstuk 2.3 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.

Antwoorden zijn beschikbaar op [deze website](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/).