# Begeleide oefening

% source files on https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/matrix_2

Gegeven is de volgende constructie:

```{figure} lesoefening1_data/constructie.svg
:align: center

Constructie, $EI = 4 \ \rm{MNm}^2, EA >> EI$
```

Gegeven is $\mathbf{u} = \begin{bmatrix} \varphi_{\rm{A}} & \varphi_{\rm{B}} & \varphi_{\rm{C}} & \varphi_{\rm{D}} & \varphi_{\rm{E}} \end{bmatrix}^T$.

:::::{exercise}
:nonumber: true

Bepaal de elementstijfheidsmatrix $\mathbf{K}^{(e)}$ voor een willekeurig element.

```{h5p} https://tudelft.h5p.com/content/1292700774193421697/embed
```

:::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

$$\mathbf{K}^{(e)} = \begin{bmatrix} \cfrac{4EI}{l} & \cfrac{2EI}{l} \\ \cfrac{2EI}{l} & \cfrac{4EI}{l} \end{bmatrix} = \begin{bmatrix} 4000 & 2000 \\ 2000 & 4000 \end{bmatrix}$$

::::

% solution_end

:::::{exercise}
:nonumber: true

Bepaal de globale stijfheidsmatrix $\mathbf{K}$.

```{h5p} https://tudelft.h5p.com/content/1292700781022982687/embed
```

:::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

De globale stijfheidsmatrix kan uit de elementstijfheidsmatrices worden bepaald door de elementen te plaatsen in de rijen en kolommen behorend bij de knopen en op te tellen.

$$\mathbf{K} =
\begin{bmatrix} 
4000 & 2000 & 0 & 0 & 0 \\ 
2000 & 4000+4000+4000 & 2000 & 2000 & 0 \\ 
0 & 2000 & 4000+4000 & 0 & 2000 \\ 
0 & 2000 & 0 & 4000 & 0 \\ 
0 & 0 & 2000 & 0 & 4000 
\end{bmatrix}
=
\begin{bmatrix} 
4000 & 2000 & 0 & 0 & 0 \\ 
2000 & 12000 & 2000 & 2000 & 0 \\ 
0 & 2000 & 8000 & 0 & 2000 \\ 
0 & 2000 & 0 & 4000 & 0 \\ 
0 & 0 & 2000 & 0 & 4000 
\end{bmatrix}$$

::::

% solution_end

:::::{exercise}
:nonumber: true

Bepaal de krachtvector $\mathbf{F}$.

```{h5p} https://tudelft.h5p.com/content/1292700781680029277/embed
```

:::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Alleen knoop $\rm{C}$ is belast met een extern koppel van $73 \rm{kNm}$ rechtsom (dus positief). 

$$\mathbf{F} = \begin{bmatrix} M_{\rm{A}} \\ 0 \\ 73 \\ 0 \\ 0 \end{bmatrix}$$

::::

% solution_end

:::::{exercise}
:nonumber: true

Bepaal de waarde van de vrijheidsgraden $\varphi_{\rm{B}}$, $\varphi_{\rm{C}}$, $\varphi_{\rm{D}}$ en $\varphi_{\rm{E}}$.

```{h5p} https://tudelft.h5p.com/content/1292700784091212317/embed
```

:::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Knoop $\rm{A}$ is ingeklemd, dus daar is de rotatie $\varphi_{\rm{A}}$ gelijk aan 0. 

Het volledige stelsel vergelijkingen is:

$$
\begin{aligned}
\mathbf{K} \mathbf{u} &= \mathbf{F} \\
\begin{bmatrix} 
4000 & 2000 & 0 & 0 & 0 \\ 
2000 & 12000 & 2000 & 2000 & 0 \\ 
0 & 2000 & 8000 & 0 & 2000 \\ 
0 & 2000 & 0 & 4000 & 0 \\ 
0 & 0 & 2000 & 0 & 4000 
\end{bmatrix}
\begin{bmatrix} 
0 \\ 
\varphi_{\rm{B}} \\ 
\varphi_{\rm{C}} \\ 
\varphi_{\rm{D}} \\ 
\varphi_{\rm{E}}
\end{bmatrix}
&=
\begin{bmatrix} M_{\rm{A}} \\ 0 \\ 73 \\ 0 \\ 0 \end{bmatrix}
\end{aligned}
$$

Het gegeven dat $\varphi_{\rm{A}}$ gelijk is aan 0 kan worden gebruikt om de eerste rij en de eerste kolom weg te laten. Dit geeft:

$$
\begin{bmatrix} 
12000 & 2000 & 2000 & 0 \\ 
2000 & 8000 & 0 & 2000 \\ 
2000 & 0 & 4000 & 0 \\ 
0 & 2000 & 0 & 4000 
\end{bmatrix}
\begin{bmatrix} 
\varphi_{\rm{B}} \\ 
\varphi_{\rm{C}} \\ 
\varphi_{\rm{D}} \\ 
\varphi_{\rm{E}}
\end{bmatrix}
&=
\begin{bmatrix} 0 \\ 73 \\ 0 \\ 0 \end{bmatrix}
$$

Het bovenstaande stelsel kan vervolgens worden opgelost voor $\varphi_{\rm{B}}$, $\varphi_{\rm{C}}$, $\varphi_{\rm{D}}$ en $\varphi_{\rm{E}}$. 

$\mathbf{u} = \begin{bmatrix} 0 \\ -\cfrac{1}{500} \\ \cfrac{11}{1000} \\ \cfrac{1}{1000} \\ -\cfrac{11}{2000} \end{bmatrix} \, \rm{rad}$

::::

% solution_end
