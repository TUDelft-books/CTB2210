````{margin}
```{attributiongrey} Bronvermelding
:class: attribution

Deze pagina is aangepast van https://icozct.tudelft.nl/TUD_CT/CT2031/tentamens/files/2031-3001-2017.pdf, onderdeel 2

% source files on https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/verplaatsingenmethode_vrijheidsgraden_2
```
````

# Begeleide oefening 2

Gegeven is de volgende constructie:

```{figure} lesoefening2_data/structure.svg
:align: center

Constructie, $EI = \infty$
```

::::{question} Opgave
:label: verplaats3_1
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

Wat is de graad van inwendig statisch onbepaaldheid?
---
M[3]
^^^
? De constructie is {gap}ste/de graads inwendig statisch onbepaald. 
---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Het is een open constructie, dus de graad van inwendig statisch onbepaaldheid is gelijk aan de graad van uitwendig statisch onbepaaldheid. Er zijn 6 onbekende oplegreacties en 3 evenwichtsvergelijkingen, daarom is de constructie 3de graads statisch onbepaald.  

::::

% solution_end

De pendelstaven worden vervangen door veren, leidend tot de volgende constructie:

```{figure} lesoefening2_data/springs.svg
:align: center

Constructie met veren, $EI = \infty$
```

::::{question} Opgave
:label: verplaats3_2
:variant: multiple-select
:columns: 1
:admonition:
:class: exercise
:nocaption:
:showanswer:

Welke twee vrijheidsgraden kan je kiezen voor deze constructie?
---
[x] Verplaatsing van $\rm{A}$ verticaal
[x] Verplaatsing van $\rm{B}$ verticaal
[x] Verplaatsing van $\rm{C}$ verticaal
[x] Verplaatsing van $\rm{D}$ verticaal
[x] Verplaatsing van $\rm{E}$ verticaal
[x] Rotatie van staaf $\rm{ABCDE}$
^^^
= Elke combinatie van 2 vrijheidsgraden is goed!
---

::::

::::{question} Opgave
:label: verplaats3_3
:variant: multiple-select
:columns: 1
:admonition:
:class: exercise
:nocaption:
:showanswer:

Wat zijn de voordelen van de verplaatsingenmethode ten opzichte van de krachtenmethode bij het doorrekenen van deze constructie?
---
[x] Er hoeven minder vergelijkingen te worden opgestelt bij de verplaatsingenmethode tov de krachtenmethode.
> Correct, maar dat is toevallig zo voor deze constructie. Voor andere constructies zouden er juist meer vergelijkingen nodig kunnen zijn.
[x] De graad van statisch onbepaaldheid hoeft niet bepaald te worden bij de verplaatsingemethode maar wel bij de krachtenmethode.
[ ] Bij de verplaatsingenmethode hoeven geen krachten te worden bepaald, maar bij de krachtenmethode wel.
> Incorrect, bij de verplaatsingenmethode worden evenwichtsvergelijkingen met krachten opgesteld.
[ ] Bij de verplaatsingenmethode hoeven geen vergeet-me-nietjes te worden teogepast, maar bij de krachtenmethode wel
> Incorrect, voor deze constructie zijn geen vergeet-me-nietjes nodig, voor zowel de krachten- als verplaatsingenmethode
---

::::

Er wordt gekozen voor de volgende vrijheidsgraden: $w_{\rm{A}}$ en $\varphi$:

```{figure} lesoefening2_data/dof.svg
:align: center

Constructie met veren en vrijheidsgraden $w_{\rm{A}}$ en $\varphi$. $EI = \infty$
```

Bepaal de evenwichtsvergelijkingen

::::{question} Opgave
:label: verplaats3_4
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
MAP[-1500 ;1]
MAP[-10500 ;1]
MAP[-2580 ;1]
^^^
? Check je resultaat voor je krachtenevenwicht. Ga uit van kN, m en rad voor je antwoorden.

$ ${gap}$ \cdot w_{\rm{A}} + ${gap}$ \cdot \varphi + ${gap}$ = 0 $
---
:::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

Verticaal krachtenevenwicht:

$$
\begin{align}
\sum  \left. F \right|  _ {\rm{v}} &= 0 \\
- N_{\rm{A}} - N_{\rm{B}} - N_{\rm{C}} - N_{\rm{D}} - N_{\rm{E}} - 2580 &= 0 \\
- 100 \cdot w_{\rm{A}} - 200 \cdot w_{\rm{B}} - 300 \cdot w_{\rm{C}} - 400 \cdot w_{\rm{D}} - 500 \cdot w_{\rm{E}} - 2580 &= 0 \\
- 100 \cdot w_{\rm{A}} - 200 \cdot \left(w_{\rm{A}} + 2 \cdot \varphi \right) - 300 \cdot \left(w_{\rm{A}} + 5 \cdot \varphi \right) - 400 \cdot \left(w_{\rm{A}} + 9 \cdot \varphi \right) - 500 \cdot \left(w_{\rm{A}} + 10 \cdot \varphi \right) - 2580 &= 0 \\
-1500 \cdot w_{\rm{A}} - 10500 \cdot \varphi - 2580 &= 0
\end{align}
$$

::::

% solution_end

::::{question} Opgave
:variant: single-select
:columns: 1
:admonition:
:class: exercise
:nocaption:
:showanswer:

Waarom is er geen uniek antwoord voor de andere evenwichtsvergelijking?
---
[x] Er kan een momentensom rondom elk willekeurig punt worden genomen.
[ ] Er kan een momentensom rondom A of B worden genomen.
> Een momentensom is altijd mogelijk rondom elk willekeurig punt, niet alleen de punten waar het inwendig buigend moment gelijk is aan 0.
[ ] De grootte van $w_{\rm{A}}$ en $\varphi$ zijn onbekend.
> $w_{\rm{A}}$ en $\varphi$ worden juist opgelost met deze evenwichtsvergelijkingen, dus het is de bedoeling dat ze nog onbekend zijn.
---
::::

% solution_start
::::{admonition} Uitwerking
:class: solution, dropdown

Een mogelijkheid, namelijk de momentensom om het punt $\rm{A}$ is hieronder gegeven:

$$
\begin{align}
\sum  \left. T \right|  _ {\rm{A}} &= 0 \\
- 2 \cdot N_{\rm{B}} - 5 \cdot N_{\rm{C}} - 9\cdot N_{\rm{D}} - 10 \cdot N_{\rm{E}} - 8 \cdot 2580 &= 0 \\
- 2 \cdot 200 \cdot w_{\rm{B}} - 5 \cdot 300 \cdot w_{\rm{C}} - 9 \cdot 400 \cdot w_{\rm{D}} - 10 \cdot 500 \cdot w_{\rm{E}} - 8 \cdot 2580 &= 0 \\
- 2 \cdot 200 \cdot \left(w_{\rm{A}} + 2 \cdot \varphi\right) - 5 \cdot 300 \cdot \left(w_{\rm{A}} + 5 \cdot \varphi\right) - 9 \cdot 400 \cdot \left(w_{\rm{A}} + 9 \cdot \varphi\right) - 10 \cdot 500 \cdot \left(w_{\rm{A}} + 10 \cdot \varphi\right) - 8 \cdot 2580 &= 0 \\
-10500 \cdot w_{\rm{A}} - 90700 \cdot \varphi - 20640 &= 0
\end{align}
$$

::::

% solution_end

::::{question} Opgave
:label: verplaats3_5
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
MAP[-67;1]
MAP[-0.15;0.01]
^^^
? Bepaal met evenwicht $w_{\rm{A}}$ en $\varphi$.

$ w_{\rm{A}} = $ {gap} $ \rm{cm} $

$ \varphi = $ {gap} $ \rm{rad} $
---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

De twee evenwichtsvergelijkingen kunnen worden opgelost voor de onbekenden $w_{\rm{A}}$ en $\varphi$. Een mogelijkheid, gebruik makende van het momentenevenwicht om punt $\rm{A}$ is hier gegeven. 

Het stelsel vergelijkingen is:
$$\begin{cases} -1500 \cdot w_{\rm{A}} -10500 \cdot \varphi -2580 &= 0\\ -10500 \cdot w_{\rm{A}} -90700 \cdot \varphi -20640  &= 0 \end{cases}
$$

Vermenigvuldigen van de bovenste vergelijking met -7 en optellen geeft:
$$ 0 \cdot w_{\rm{A}} - 17200 \cdot \varphi - 2580 = 0 \rightarrow \varphi = -0.15 \ \rm{rad} $$

Invullen in de bovenste vergelijking geeft de oplossing voor $w_{\rm{A}}$:
$$ -1500 \cdot w_{\rm{A}} -10500 \cdot -0.15 -2580 = 0 \rightarrow w_{\rm{A}} = -67 \ \rm{cm}$$

::::

% solution_end


::::{question} Opgave
:label: verplaats3_6
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-67]
M[-194]
M[-426]
M[-808]
M[-1085]
^^^
? Wat zijn de krachten in de veren? Ga uit van + voor trek en - voor druk.

- $ N_{\rm{A}}  = $ {gap} $ \rm{kN}$
- $ N_{\rm{B}} = $ {gap} $ \rm{kN}$
- $ N_{\rm{C}} = $ {gap} $ \rm{kN}$
- $ N_{\rm{D}} = $ {gap} $ \rm{kN}$
- $ N_{\rm{E}} = $ {gap} $ \rm{kN}$
---

::::

% solution_start

::::{admonition} Uitwerking
:class: solution, dropdown

$$ N_{\rm{A}} = 100 \cdot w_{\rm{A}} = -67 \ \rm{kN}$$
$$ N_{\rm{B}} = 200 \cdot w_{\rm{B}} = 200 \cdot \left(w_{\rm{A}} + 2 \cdot \varphi\right) =-194 \ \rm{kN}$$
$$ N_{\rm{C}} = 300 \cdot w_{\rm{C}} = 300 \cdot \left(w_{\rm{A}} + 5 \cdot \varphi\right) =-426 \ \rm{kN}$$
$$ N_{\rm{D}} = 400 \cdot w_{\rm{D}} = 400 \cdot \left(w_{\rm{A}} + 9 \cdot \varphi\right) =-808 \ \rm{kN}$$
$$ N_{\rm{E}} = 500 \cdot w_{\rm{E}} = 500 \cdot \left(w_{\rm{A}} + 10 \cdot \varphi\right) =-1085 \ \rm{kN}$$
::::

% solution_end
