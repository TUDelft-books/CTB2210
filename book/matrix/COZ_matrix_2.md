# COZ opgave 5.5

::::::{note}

Deze opgave kan in [ANS](https://ans.app/universities/1/courses/712480/assignments/1909417/go_to) gemaakt worden.

Als je nog geen toegang hebt tot deze toets, registreer je dan via [deze link](https://ans.app/accept/invitations/07b7bc5a-d334-43d7-9532-a1434730f6d7).

:::::: 

% https://ans.app/repo_questions/67089916/generator

Gegeven is de volgende constructie:

```{figure-start} ./COZ_matrix_2_data/constructie2.svg
---
align: center
number:
figclass: sticky-margin
source: https://github.com/Tom-van-Woudenberg/mechanics-figures-source/tree/main/verplaatsingenmethode_1
name: constructie_matrix_verplaats
---

```


- $ EI = 120 \, \rm{MNm}^2 $
- $ EA \gg EI $

```{figure-end}
```


::::{admonition} Opgave
:class: exercise

Bepaal de rotaties van $\rm{B}$, $\rm{C}$ en $\rm{D}$ met de matrixmethode.

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Allereerst wordt de relatie $\mathbf{K} \mathbf{u} = \mathbf{f}$ opgesteld:

$$
\begin{bmatrix}
0 & 0 & 0 & 0\\
0 & 0 & 0 & 0\\
0 & 0 & 0 & 0\\
0 & 0 & 0 & 0\\
\end{bmatrix}
\begin{bmatrix}
\varphi_{\rm{A}} \\
\varphi_{\rm{B}} \\
\varphi_{\rm{C}} \\
\varphi_{\rm{D}}
\end{bmatrix}
= 
\begin{bmatrix}
0 \\
0 \\
0 \\
0
\end{bmatrix}
$$

Met alle rotaties en momenten gedefinieerd positief tegen de klok in.

Nu worden de stijfheidsrelaties van de individuele staven bepaald: $\mathbf{K^{\rm{(e)}}} = \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2EI}{L} \\ \cfrac{2EI}{L} & \cfrac{4EI}{L}  \end{bmatrix}$. Dit geeft:

$$
\begin{align*}
\mathbf{K^{\rm{(e)}}_{\rm{AD}}} &= \begin{bmatrix} \cfrac{4 \cdot 120000}{5} & \cfrac{2 \cdot 120000}{5} \\ \cfrac{2 \cdot 120000}{5} & \cfrac{4 \cdot 120000}{5}  \end{bmatrix} = \begin{bmatrix} 96000 & 48000 \\ 48000 & 96000  \end{bmatrix} \\
\mathbf{K^{\rm{(e)}}_{\rm{CD}}} &= \begin{bmatrix} \cfrac{4 \cdot 120000}{5} & \cfrac{2 \cdot 120000}{5} \\ \cfrac{2 \cdot 120000}{5} & \cfrac{4 \cdot 120000}{5}  \end{bmatrix} = \begin{bmatrix} 96000 & 48000 \\ 48000 & 96000  \end{bmatrix} \\
\mathbf{K^{\rm{(e)}}_{\rm{BD}}} &= \begin{bmatrix} \cfrac{4 \cdot 120000}{2} & \cfrac{2 \cdot 120000}{2} \\ \cfrac{2 \cdot 120000}{2} & \cfrac{4 \cdot 120000}{2}  \end{bmatrix} = \begin{bmatrix} 240000 & 120000 \\ 120000 & 240000  \end{bmatrix} \\
\end{align*}
$$

Al deze stijfheden kunnen in de globale stijfheidsmatrix $\mathbf{K}$ worden opgenomen, waarbij de kolommen en rijen aan de juiste vrijheidsgraden worden gekoppeld. We beginnen met element $\rm{AD}$, dat knooppunten $\rm{A}$ en $\rm{D}$ koppelt (rij en kolom 1 en 4):

$$
\mathbf{K} = 
\begin{bmatrix}
96000 & 0 & 0 & 48000\\
0 & 0 & 0 & 0\\
0 & 0 & 0 & 0\\
48000 & 0 & 0 & 96000\\
\end{bmatrix}
$$

Vervolgens, element $\rm{CD}$, die knoop $\rm{C}$ en $\rm{D}$ aan elkaar koppelt (rij en kolom 3 en 4):

$$
\mathbf{K} =
\begin{bmatrix}
96000 & 0 & 0 & 48000\\
0 & 0 & 0 & 0\\
0 & 0 & 96000 & 48000\\
48000 & 0 & 48000 & 192000\\
\end{bmatrix}
$$

Tot slot, ook element $\rm{BD}$, tussen knoop $\rm{B}$ en $\rm{D}$ (rij en kolom 2 en 4):

$$
\mathbf{K} =
\begin{bmatrix}
96000 & 0 & 0 & 48000\\
0 & 240000 & 0 & 120000\\
0 & 0 & 96000 & 48000\\
48000 & 120000 & 48000 & 432000\\
\end{bmatrix}
$$

Nu kan ook de krachtenvector bepaald worden. Met als eerste de externe krachten:

$$
\mathbf{f} =
\begin{bmatrix}
0 \\
29 \\
0 \\
-29
\end{bmatrix}
$$

En de oplegreacties. De rotatie in $\rm{A}$ is nul, leidend tot een oplegreactie:

$$
\begin{bmatrix}
96000 & 0 & 0 & 48000\\
0 & 240000 & 0 & 120000\\
0 & 0 & 96000 & 48000\\
48000 & 120000 & 48000 & 432000\\
\end{bmatrix}
\begin{bmatrix}
0 \\
\varphi_{\rm{B}} \\
\varphi_{\rm{C}} \\
\varphi_{\rm{D}}
\end{bmatrix}
=
\begin{bmatrix}
M_{\rm{A}} \\
29 \\
0 \\
-29
\end{bmatrix}
$$

Om de onbekende rotaties te vinden kunnen de eerste rij en kolom verwijderd worden:

$$
\begin{bmatrix}
240000 & 0 & 120000\\
0 & 96000 & 48000\\
120000 & 48000 & 432000\\
\end{bmatrix}
\begin{bmatrix}
\varphi_{\rm{B}} \\
\varphi_{\rm{C}} \\
\varphi_{\rm{D}}
\end{bmatrix}
=
\begin{bmatrix}
29 \\
0 \\
-29
\end{bmatrix}
$$

Dit geeft

$$
\begin{bmatrix}
\varphi_{\rm{B}} \\
\varphi_{\rm{C}} \\
\varphi_{\rm{D}}
\end{bmatrix}
=
\begin{bmatrix}
\cfrac{7}{19200} \\
\cfrac{1}{16000} \\
\cfrac{-1}{8000}
\end{bmatrix}
\approx
\begin{bmatrix}
3.65 \cdot 10^{-4} \\
6.25 \cdot 10^{-5} \\
-1.25 \cdot 10^{-4}
\end{bmatrix} (↺)
$$

::::

% solution_end
