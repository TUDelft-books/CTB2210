````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze oefening is aangepast van de [les van 25 oktober van het vak CTS1000](https://oit.tudelft.nl/CT1000/2025/week_8/session_3/intro.html) van {cite:ts}`CT1000`

```
````

# Begeleide oefening 2

Gegeven is de volgende constructie:

```{figure-start} intro_data/struct.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/temperatuur2
:number:
:figclass: sticky-margin
```

- $EI = 20 \ \rm{MNm^2}$
- $EA = 10 \ \rm{MN}$
- $\Delta T_{\rm{AC}} = 8 \ ^{\circ} \rm{C} (◠)$
- $\Delta T_{\rm{CD}} = 8 \ ^{\circ} \rm{C} (ᑐ)$
- $\Delta T_{\rm{CD}} = 50 \ ^{\circ} \rm{C} (+)$
- $h = 0.4 \ \rm{m}$
- $\alpha = 10^{-5} \ ^{\circ} \rm{C}^{-1}$

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
M[0]
M[0.0005]
M[0.0002]
M[0.0002]
^^^
?
Wat is de kromming ten gevolge van de temperatuurverandering?

- $\epsilon^{\rm{T}}_{\rm{AC}} = $ {gap} $\rm{m}/\rm{m}$
- $\epsilon^{\rm{T}}_{\rm{CD}} = $ {gap} $\rm{m}/\rm{m}$
- $\kappa^{\rm{T}}_{\rm{AC}} = $ {gap} $\rm{m}^{-1}$
- $\kappa^{\rm{T}}_{\rm{CD}} = $ {gap} $\rm{m}^{-1}$

---
::::

Gekozen is het volgende statisch bepaalde systeem met vormveranderingsvoorwaarde. Equivalente krachten voor de temperatuurinvloed zijn nog niet toegevoegd.

```{hide-sticky-margin}
```
```{figure-start} intro_data/SD.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/temperatuur2
:number:
:figclass: sticky-margin
```

- $EI = 20 \ \rm{MNm^2}$
- $EA = 10 \ \rm{MN}$
- $\Delta T_{\rm{AC}} = 8 \ ^{\circ} \rm{C} (◠)$
- $\Delta T_{\rm{CD}} = 8 \ ^{\circ} \rm{C} (ᑐ)$
- $\Delta T_{\rm{CD}} = 50 \ ^{\circ} \rm{C} (+)$
- $h = 0.4 \ \rm{m}$
- $\alpha = 10^{-5} \ ^{\circ} \rm{C}^{-1}$

```{figure-end}
```

::::::{question} Opgave
:type: no-input
:nocaption:
:class: exercise
:admonition:
:showanswer:

Teken de vervormde constructie ten gevolge van afzonderlijk de verdeelde belasting en $N_{\rm{CD}}$.

---
=

:::::{grid}
:class-container: center-grid

::::{grid-item}
:columns: auto

```{figure} intro_data//verplaats_1.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/temperatuur2
```

::::

::::{grid-item}
:columns: auto

```{figure} intro_data/verplaats_2.svg
:align: center
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/temperatuur2
```

::::

:::::

---

::::::

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-6]
M[-144]
M[0.0004]
M[0.0096]
M[-6]
M[-122.4]
M[0.4]
M[0]
^^^
? Wat zijn de krachtverdelingen en verplaatsingen als gevolg van de verdeelde belasting als functie van $N_{\rm{CD}}$ in $\rm{kN}$? Neem dus geen kinematische equivalente krachten als gevolg van de temperatuurinvloed mee.

- $M_{\rm{B}} \left( \rm{N}_{\rm{CD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kNm}}{\rm{kN}}\right) \cdot N_{\rm{CD}} + $ {gap} $\left(\rm{in} \, \rm{kNm}\right)$ (◡)
- $\varphi_{\rm{B}} \left( \rm{N}_{\rm{CD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot N_{\rm{CD}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$ (↻)
- $w_{\rm{C}}^{\rm{BC}} \left( \rm{N}_{\rm{CD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot N_{\rm{CD}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$
- $w_{\rm{C}}^{\rm{CD}} \left( \rm{N}_{\rm{CD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot N_{\rm{CD}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$

---

::::

::::::{question} Opgave
:type: no-input
:nocaption:
:class: exercise
:admonition:
:showanswer:

Teken de vorm van de kromming ten gevolge van de temperatuurverandering.

---
=

```{figure} ./intro_data/kromming.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/temperatuur2
:number:
```

---

::::::

::::::{question} Opgave
:type: no-input
:nocaption:
:class: exercise
:admonition:
:showanswer:

Teken de constructie inclusief kinematisch equivalente krachten als gevolg van de temperatuurinvloed.

---
=

```{figure-start} intro_data/statisch_onbepaald.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/temperatuur2
:number:
```

- $EI = 20 \ \rm{MNm^2}$
- $EA = 10 \ \rm{MN}$

```{figure-end}
```

---

::::::

::::::{question} Opgave
:type: no-input
:nocaption:
:class: exercise
:admonition:
:showanswer:

Teken de vervormingen ten gevolge van de kinematisch equivalente krachten als gevolg van de temperatuurinvloed.

---
=

```{figure} intro_data/verplaats_3.svg
:align: center
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/temperatuur2
:number:
```

---

::::::

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-6]
M[-148]
M[0.0004]
M[0.01]
M[-6]
M[128.4]
M[0.4]
M[2]
^^^
? Wat zijn de krachtverdelingen en verplaatsingen als gevolg van de verdeelde belasting als functie van $N_{\rm{CD}}$ in $\rm{kN}$ én de kinematische equivalente krachten als gevolg van de temperatuurinvloed.

- $M_{\rm{B}} \left( \rm{N}_{\rm{CD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{kNm}}{\rm{kN}}\right) \cdot N_{\rm{CD}} + $ {gap} $\left(\rm{in} \, \rm{kNm}\right)$  (◡)
- $\varphi_{\rm{B}} \left( \rm{N}_{\rm{CD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{rad}}{\rm{kN}}\right) \cdot N_{\rm{CD}} + $ {gap} $\left(\rm{in} \, \rm{rad}\right)$ (↻)
- $w_{\rm{C}}^{\rm{BC}} \left( \rm{N}_{\rm{CD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot N_{\rm{CD}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$
- $w_{\rm{C}}^{\rm{CD}} \left( \rm{N}_{\rm{CD}} \right) = $ {gap} $ \left(\rm{in} \, \cfrac{\rm{mm}}{\rm{kN}}\right) \cdot N_{\rm{CD}} + $ {gap} $\left(\rm{in} \, \rm{mm}\right)$

---

::::

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-20.375]
^^^
? Los de vormveranderingsvoorwaarde op om de statisch onbepaalde kracht te vinden.

$N_{\rm{CD}}= $ {gap} $\rm{kN}$

---

::::

::::{question} Opgave
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-21.75]
M[0]
M[-0.0012875]
M[0.0002]
M[-6.15]
M[0.4]

^^^
? Los nu ook de overige krachtenverdeling en verplaatsingen op.

- $M_{\rm{B}}= $ {gap} $\rm{kNm}$ (◡)
- $M_{\rm{halverwege \ CD}}= $ {gap} $\rm{kNm}$ (ᑐ)
- $\kappa_{\rm{B}} = $ {gap} $\rm{m}^{-1}$ (◡)
- $\kappa_{\rm{halverwege \ CD}} = $ {gap} $\rm{m}^{-1}$ (ᑐ)
- $w_{\rm{C}}= $ {gap} $\rm{mm}$ (↑)
- $w_{\rm{halverwege \ CD}}= $ {gap} $\rm{mm}$ (→)

---

::::
