# COZ opgave 5.3

::::::{note}

Deze opgave kan in [ANS](https://ans.app/universities/1/courses/712480/assignments/1909417/go_to) gemaakt worden.

Als je nog geen toegang hebt tot deze toets, registreer je dan via [deze link](https://ans.app/accept/invitations/07b7bc5a-d334-43d7-9532-a1434730f6d7).

:::::: 

% https://ans.app/repo_questions/67089557/generator

Gegeven is de volgende constructie:


:::{fetch} {numref}`constructie_matrix_verplaats`
:::

::::{admonition} Opgave
:class: exercise

Bepaal de rotatie van $\rm{D}$ met behulp van de verplaatsingenmethode en teken de momentenlijn.

::::

% solution_start

::::{admonition} Antwoord
:class: solution, dropdown

De verplaatsingen kunnen beschreven worden met de rotatie van $\rm{D}$.

```{figure} intro_data/phi_D.svg
:align: center
:number:
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1
```

Voor $\rm{AB}$, kan een vergeet-me-nietje gebruikt worden:

```{figure} intro_data/AD.svg
:align: center
:number:
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1
```

$$
\varphi_{\rm{D}} = \cfrac{M_{\rm{D}}^{\rm{AD}} \cdot 5}{4 \cdot 120000} = \cfrac{M_{\rm{D}}^{\rm{AD}}}{96000}
$$

Omschrijven van deze relatie geeft:

$$
M_{\rm{D}}^{\rm{AD}} = 96000 \cdot \varphi_{\rm{D}}
$$

Ook voor $\rm{CD}$ kan een vergeet-me-nietje gebruikt worden:

```{figure} intro_data/CD2.svg
:align: center
:number:
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1
```

$$
\varphi_{\rm{D}} = -\cfrac{M_{\rm{D}}^{\rm{CD}} \cdot 5}{3 \cdot 120000} = -\cfrac{M_{\rm{D}}^{\rm{CD}}}{72000}
$$

Dit geeft:

$$
M_{\rm{D}}^{\rm{CD}} = -72000 \cdot \varphi_{\rm{D}}
$$

Tot slot geldt hetzelfde vergeet-me-nietje voor $\rm{BD}$

```{figure} intro_data/BD2.svg
:align: center
:number:
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1
```

$$
\varphi_{\rm{D}} = - \cfrac{M_{\rm{D}}^{\rm{BD}} \cdot 2}{3 \cdot 120000} - \cfrac{29 \cdot 2}{6 \cdot 120000} = -\cfrac{M_{\rm{D}}^{\rm{BD}}}{180000} - \cfrac{29}{360000}
$$

Dit geeft.

$$
M_{\rm{D}}^{\rm{BD}} = -180000 \cdot \varphi_{\rm{D}} - 14.5
$$

Nu kan het evenwicht van knoop $\rm{D}$ bekeken worden.

```{figure} intro_data/D.svg
:align: center
:number:
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1
```

$$
\begin{align*}
M_{\rm{D}}^{\rm{AD}} - M_{\rm{D}}^{\rm{CD}} - M_{\rm{D}}^{\rm{BD}} + 29 &= 0 \\
\varphi_{\rm{D}} &= \cfrac{-1}{8000} \approx -1.25 \cdot 10^{-4} \ \rm{rad}
\end{align*}
$$

De momentenlijn volgt uit bovenstaande:

```{figure} intro_data/Mline.svg
:align: center
:number:
:source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1
```

::::

% solution_end

