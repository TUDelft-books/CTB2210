# Instructie

Tot nu toe hebben we statisch onbepaalde constructies behandeld die ofwel op rek ofwel op buiging worden belast. In deze les behandelen we constructies die zowel op rek als op buiging worden belast. We gebruiken de krachtenmethode om de verplaatsingen en inwendige krachten te berekenen. De aanpak voor deze constructies is niet anders, maar de verplaatsingen kunnen wat complexer zijn. We behandelen de toepassing met het volgende voorbeeld.

::::::{prf:example}
:nonumber: true
:label: rek_raam_0

% https://oit.tudelft.nl/CTB2210/2025/TOZ/opgave.html

```{figure-start} ./instructie_data/constructie.svg
---
align: center
figclass: sticky-margin
source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode
number:
---

```

- $EI = 64 \ \rm{MNm^2}$
- $EA = 4 \ \rm{MN}$

```{figure-end}
```

::::::

1. Bepaal de graad van statische bepaaldheid.

    ::::::{prf:example}
    :nonumber: true
    :label: rek_raam_1

    ```{figure} instructie_data/SB1.svg
    :align: center
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode
    :number:
    ```

    Er zijn 7 onbekende oplegreacties en 6 onbekende verbindingskrachten. Dat geeft een uitwendige graad van statisch onbepaaldheid van 1. Omdat deze constructie niet gesloten is, is de inwendige graad van statisch onbepaaldheid ook gelijk aan 1.

    ::::::

2. Transformeer de constructie in een statisch bepaald systeem door opleggingen weg te nemen, de constructie te splitsen bij een pendelstaaf, of scharnieren toe te voegen: voeg onbekende statisch onbepaalde krachten en vervormingsvoorwaardes toe voor elke opleggging die je hebt weggenomen en scharnieren die je hebt toegevoegd. Let op dat je de constructie niet transformeert tot een (gedeeltelijk) mechanisme! Kies een statisch bepaald systeem dat makkelijk is uit te rekenen: Kies een statisch bepaald systeem dat makkelijk is uit te rekenen: elementen verplaatsen bij voorkeur niet als ze ook al roteren en je kan vergeet-me-nietjes herkennen in het statisch bepaalde systeem.

    ::::::{prf:example}
    :nonumber: true
    :label: rek_raam_2

    Er zijn veel opties, waarvan een aantal mogelijke opties:

    `````{tab-set}
    :sync-group: raamwerk

    ````{tab-item} De inklemming bij $\rm{A}$ vervangen door een scharnier
    :sync: keyraamrek_1
    ```{figure-start} ./instructie_data/optie1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    $ \varphi_{\rm{A}} = 0 $

    ```{figure-end}
    ```
    ````
    ````{tab-item} Staaf $\rm{BD}$ splitsen
    :sync: keyraamrek_2
    ```{figure-start} ./instructie_data/optie2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    $ w_{\rm{D}}^{\rm{BD}} = w_{\rm{D}}^{\rm{BD}}$

    ```{figure-end}
    ```

    ````
    ````{tab-item} Staaf $\rm{CG}$ splitsen
    ```{figure} ./instructie_data/optie3.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```
    Deze constructie is een mechanisme dus geen geschikte statisch bepaalde constructie.
    ````
    ````{tab-item} Scharnier toevoegen tussen $\rm{A}$ en $\rm{D}$
    :sync: keyraamrek_4
    ```{figure-start} ./instructie_data/optie4.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    $\varphi_{\rm{S}}^{\rm{AS}} = \varphi_{\rm{S}}^{\rm{SD}}$

    ```{figure-end}
    ```
    ````
    ````{tab-item} Scharnier toevoegen tussen $\rm{D}$ en $\rm{E}$
    ```{figure} ./instructie_data/optie5.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```
    Deze constructie is een mechanisme dus geen geschikte statisch bepaalde constructie.
    ````
    ````{tab-item} Scharnier toevoegen tussen $\rm{E}$ en $\rm{G}$
    ```{figure} ./instructie_data/optie6.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```
    Deze constructie is een mechanisme dus geen geschikte statisch bepaalde constructie.
    ````
    ````{tab-item} Scharnieroplegging bij $\rm{C}$ vervangen door een verticaal rolscharnier 
    ```{figure} ./instructie_data/optie7.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```
    Deze constructie is een mechanisme dus geen geschikte statisch bepaalde constructie.
    ````
    ````{tab-item} Scharnieroplegging bij $\rm{B}$ vervangen door een verticaal rolscharnier 
    :sync: keyraamrek_8
    ```{figure-start} ./instructie_data/optie8.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    $w_{\rm{B}} = 0$

    ```{figure-end}
    ```

    ````
    `````

    Voor elk van de opties die geen mechanisme zijn kunnen we de verplaatsingen schetsen door zowel de statisch onbepaalde kracht en de al aanwezige belasting om een variant te kiezen die een simpel verplaatsingspatroon heeft:

    ```````{tab-set}
    :sync-group: raamwerk

    ``````{tab-item} De inklemming bij $\rm{A}$ vervangen door een scharnier
    :sync: keyraamrek_1

    ```{figure} ./instructie_data/optie1_verplaatsingen_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    Ten gevolge van enkel het moment in $\rm{A}$ is dit een redelijk goed te doen verplaatsingspatroon. Het rechter gedeelte roteert alleen star en heeft geen invloed op de rotatie van $\rm{A}$. De linker ligger kan worden behandeld met het vergeet-me-nietje van een ligger op twee steunpunten met een koppel op ieder uiteinde, die ook nog om het vaste punt $\rm{A}$ een starre rotatie ondergaat. Die drie factoren zorgen alle drie voor een rotatie in $\rm{A}$.

    ```{figure} ./instructie_data/optie1_verplaatsingen_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    Ook ten gevolge van de puntlast zijn de verplaatsingen van het rechter gedeelte niet van invloed op de verplaatsingen van het linker gedeelte. De belasting zorgt wel voor een verlenging van $\rm{BD}$ en kromming in $\rm{AD}$, die allebei bijdragen aan een rotatie in $\rm{A}$.

    ``````

    ``````{tab-item} Staaf $\rm{BD}$ splitsen
    :sync: keyraamrek_2


    ```{figure} ./instructie_data/optie2_verplaatsingen_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    Ten gevolge van enkel het de normaalkracht in de gesplitste pendelstaaf is dit een goed te doen verplaatsingspatroon. $\rm{BD}$ verlengt alleen maar en $\rm{AD}$ kan worden behandeld als een uitkragende ligger met een kracht op het uiteinde $\rm{D}$. Het rechter gedeelte roteert alleen star en heeft geen invloed heeft op de zakking van $\rm{D}$.

    ```{figure} ./instructie_data/optie2_verplaatsingen_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    Ook ten gevolge van de puntlast zijn de verplaatsingen van het rechter gedeelte niet van invloed op de verplaatsingen van het linker gedeelte. De belasting zorgt wel voor een kromming in $\rm{AE}$ en dus verplaatsing in $\rm{D}$.


    ``````

    ``````{tab-item} Scharnier toevoegen tussen $\rm{A}$ en $\rm{D}$
    :sync: keyraamrek_4

    ```{figure} ./instructie_data/optie3_verplaatsingen_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    Dit verplaatsingspatroon is behoorlijk complex, ook als we enkel naar de vervormingen van enkel het momentenpaar kijken. De verticale verplaatsing van het nieuwe scharnier tussen $\rm{A}$ en $\rm{D}$ is van belang voor de rotaties rondom het scharnier,maar vereist ook het berekenen van een dwarskracht in dat nieuwe scharnier. Daarnaast zal $\rm{BD}$ rekken. Vanaf rechts van $\rm{D}$ zijn de staven wel spanningsloos. Het rechter gedeelte roteert alleen star en heeft geen invloed heeft op de rotaties bij het nieuwe scharnier.

    ```{figure} ./instructie_data/optie3_verplaatsingen_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    Het verplaatsingspatroon links van $\rm{E}$ is ook voor enkel de puntlast van $84 \ \rm{kN}$ complex, hoewel iets minder ingewikkeld dan met het statisch onbepaalde momentenpaar. Ook in dit geval zijn de verplaatsingen van het rechter gedeelte niet van invloed op de verplaatsingen van het linker gedeelte, maar zorgt het wel voor een dwarskracht en moment in $\rm{D}$ die vergelijkbare complexe hoekverdraaiingen veroorzaken bij het scharnier.
    ``````

    ``````{tab-item} Scharnieroplegging bij $\rm{B}$ vervangen door een verticaal rolscharnier 
    :sync: keyraamrek_2


    ```{figure} ./instructie_data/optie4_verplaatsingen_1.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    Deze optie is zeer vergelijkbaar met de optie waarbij $\rm{BD}$ wordt gesplitst. De kracht is wel aangenomen de andere kant op, maar de aanpak is hetzelfde: $\rm{AD}$ kan worden behandeld als een uitkragende ligger met een kracht op het uiteinde welke zorgt voor een zakking van $\rm{B}$ als daar de verkorting van $\rm{BD}$ in wordt meegenomen. Als we enkel de statisch onbepaalde kracht $\B_{\rm{v}}$ beschouwen, roteert het rechter gedeelte alleen star en heeft geen invloed heeft op de zakking van $\rm{B}$.

    ```{figure} ./instructie_data/optie4_verplaatsingen_2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/krachtenmethode
    ```

    Ook kijken naar enkel de puntlast van $84 \ \rm{kN}$ zijn de verplaatsingen van het gedeelte rechts van $\rm{D}$ niet van invloed op de verplaatsingen van $\rm{B}$, maar zorgt het wel voor een dwarskracht en moment in $\rm{D}$ die $\rm{B}$ laat zakken.


    ``````

    ```````

    De laatste optie wordt gekozen

    ::::::

3. Los de verplaatsing op in termen van de onbekende onbepaalde krachten zoals je normaal zou doen voor een statisch bepaalde constructie.

    ::::::{prf:example}
    :nonumber: true
    :label: rek_raam_3

    ```{figure-start} ./instructie_data/stat_bepaald.svg
    ---
    align: center
    figclass: sticky-margin
    number:
    source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode
    ---

    ```
    
    - $EA = 4 \ \rm{MN}$
    - $EI = 64 \ \rm{MNm^2}$

    ```{figure-end}
    ```

    Om de verplaatsing van $\rm{B}$ te vinden, moeten we eerst de inwendige krachten in $\rm{D}$ vinden, waaruit de zakking volgt van $\rm{D}$. Daarmee kunnen we de verplaatsing van $\rm{B}$ vinden.

    Allereerst de normaalkracht in $\rm{BD}$ als functie van $B_{\rm{v}}$:

    ```{figure} instructie_data/BD.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode
    ```

    $$
    \begin{align}
    \sum F_{\rm{v}}^{\rm{BD}} &= 0 \\
    B_{\rm{v}} + N_{\rm{BD}}&= 0 \\
    N_{\rm{BD}} &= -B_{\rm{v}}
    \end{align}
    $$

    Ook kunnen we de normaalkracht in $\rm{CG}$ vinden:

    ```{figure} instructie_data/EG.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode
    ```

    $$
    \begin{align}
    \sum \left. T \right|_{\rm{E}}^{\rm{EG}} &= 0 \\
    84 \cdot 4 - N_{\rm{CG}} \cdot 8 &= 0 \\
    N_{\rm{CG}} &= 42 \ \rm{kN}
    \end{align}
    $$

    Daarmee kunnen de de dwarskracht en het moment net links van $\rm{D}$ vinden:

    ```{figure} instructie_data/DG.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode
    ```

    $$
    \begin{align}
    \sum F_{\rm{v}}^{\rm{DG}} &= 0 \\
    V_{\rm{D}}^{\rm{AD}}-B_{\rm{v}} - 84 + 42 &= 0 \\
    V_{\rm{D}}^{\rm{AD}} &= B_{\rm{v}} + 42
    \end{align}
    $$

    $$
    \begin{align}
    \sum \left. T \right|_{\rm{D}}^{\rm{DG}} &= 0 \\
    M_{\rm{D}} + 84 \cdot 8 - 42 \cdot 12 &= 0 \\
    M_{\rm{D}} &= -168 \ \rm{kNm}
    \end{align}
    $$
    
    Nu volgt de verplaatsing in $\rm{D}$ uit een vergeet-me-nietje:

    ```{figure} ./instructie_data/wAD.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode
    ```

    $$
    \begin{align}
    w_{\rm{D}} &= \cfrac{168 \cdot 4^2}{2 \cdot 64000} + \cfrac{\left( B_{\rm{v}} + 42 \right) \cdot 4^3}{3 \cdot 64000} \\
    w_{\rm{D}} &= \cfrac{1}{3000} \cdot B_{\rm{v}} + 0.035 \\
    w_{\rm{D}} & \approx 0.000333 \cdot B_{\rm{v}} + 0.035 \ (\downarrow)
    \end{align}
    $$

    De verplaatsing van $\rm{B}$ kan worden gevonden met de verlenging van een staaf door axiale krachten:

    ```{figure} ./instructie_data/BD2.svg
    :align: center
    :number:
    :source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/krachtenmethode
    ```

    $$
    \begin{align}
    w_{\rm{B}} &= - w_{\rm{D}} + \Delta L_{\rm{BD}} \\
    w_{\rm{B}} &= - w_{\rm{D}} +  \cfrac{-B_{\rm{v}} \cdot 8}{4000} \\
    w_{\rm{B}} &= - \cfrac{7}{3000} \cdot B_{\rm{v}} - 0.035 \\
    w_{\rm{B}} & \approx 0.00233\cdot B_{\rm{v}} - 0.035 \\
    \end{align}
    $$

    ::::::

4. Gebruik je vormveranderingsvoorwaarden om de statisch onbepaalde krachten op te lossen

    ::::::{prf:example}
    :nonumber: true
    :label: rek_raam_4

    De vormveranderingsvoorwaarde geeft:

    $$
    \begin{align}
    w_{\rm{B}} &= 0 \\
    -\cfrac{7}{3000} \cdot B_{\rm{v}} - 0.035 &= 0 \\
    B_{\rm{v}} &= -15 \ \rm{kN}
    \end{align}
    $$

    ::::::

## Zelfde instructies in collegevorm

De opname volgt na het college.

## Extra opgaves in boek

- Opgaves 2.22, 2.25 - 2.28 in hoofdstuk 2.3 van het boek Mechanica, Statisch onbepaalde constructies en bezwijkanalyse {cite:p}`Hartsuijker2016`.

Antwoorden zijn beschikbaar op [deze website](https://icozct.tudelft.nl/TUD_CT/boekantwoorden/vol3/Chapter1-2/).
