# 3 november: Tentamenopdracht

Het tentamen is nog in ontwikkeling.

```{figure} ./lesson_data/constructie1.svg
:align: center
:figclass: sticky-margin
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```


:::::{exercise}
:nonumber: true

Show that this structure is internally statically indeterminate to the second degree.

:::::

:::::{exercise}
:nonumber: true

Provide three valid variants to make this structure statically determinate for the purpose of the force method. Provide three different variants: for each variant, you cannot adapt the same node ($\rm{A}$, $\rm{B}$, $\rm{C}$ or $\rm{D}$) or element ($\rm{AD}$, $\rm{CD}$ and $\rm{BC}$) as in the other variants.

For each of the variants, provide:

- The necessary compatibility equations to determine the statically indeterminate forces
- For each variant, draw the deformed shape of the structure for all of the the statically determinate and existing loads individually.
- Explain why your variants are not a mechanism based on your drawings of the deformed shapes.

:::::

Given the following structure. Note that the vertical roller support at $\rm{C}$ is removed.

```{figure-start} ./lesson_data/constructie2.svg
:align: center
:figclass: sticky-margin
:number:
:source: https://github.com/Structural-Mechanics-CEG/mechanics-figures-source/tree/main/exam_stat_onb
```

- $EA_{\rm{BC}} = 14.4 \, \rm{MN}$
- $EI_{\rm{CDA}} = 62720 \, \rm{kNm}^2$
- $EA_{\rm{CDA}} \gg EI_{\rm{CDA}} $

```{figure-end}
```

:::::{exercise}
:nonumber: true

Solve the statically indeterminate force using the force method using a statically determinate structure of your own choice.

:::::

:::::{exercise}
:nonumber: true

Give as many arguments as possible to explain why you cannot apply the matrix method to this structure when you keep to the restricted application of the matrix matrix as taught in this course. For you information, the matrix method in this course was based on this single stiffness matrix:

$$
\mathbf{K^{\rm{(e)}}} &= \begin{bmatrix} \cfrac{4 EI}{L} & \cfrac{2 EI}{L} \\ \cfrac{2 EI}{L} & \cfrac{4 EI}{L} \end{bmatrix}
$$

:::::

::::{admonition} Solution
:class: solution, dropdown

- Moveable nodes
- Hinges
- Loads on elements

::::
