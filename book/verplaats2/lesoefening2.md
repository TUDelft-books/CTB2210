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
M[-1500]
M[-10500]
M[-2580]
^^^
? Check je resultaat voor je krachtenevenwicht. Ga uit van kN, m en rad voor je antwoorden.

$ ${gap}$ \cdot w_{\rm{A}} + ${gap}$ \cdot \varphi + ${gap}$ = 0 $
---
:::::


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


::::{question} Opgave
:label: verplaats3_5
:type: short-answer
:variant: gaps
:admonition:
:class: exercise
:nocaption:
:showanswer:

---
M[-67]
M[-0.15]
^^^
? Bepaal met evenwicht $w_{\rm{A}}$ en $\varphi$.

$ w_{\rm{A}} = $ {gap} $ \rm{cm} $

$ \varphi = $ {gap} $ \rm{rad} $
---

::::



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

