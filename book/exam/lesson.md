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

Provide three valid variants to make this structure statical determinate for the purpose of the force method. Don't make the same change to a node ($\rm{A}$, $\rm{B}$, $\rm{C}$ and $\rm{D}$) or element ($\rm{AD}$, $\rm{CD}$ and $\rm{BC}$) twice; make sure you never have the same unknown statically determinate force twice. So, making an identical change at two points in the same element is not allowed either.

For each of the variants:

- Provide the necessary compatibility equations to determine the statically indeterminate forces
- Explain why your variants are not mechanisms based on drawings of the deformed shapes.

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

Solve the statically indeterminate force using the force method using a statical determinate structure of your own choice.

:::::

:::::{exercise}
:nonumber: true

Due to which restriction(s), for the matrix method as taught in this course, is it not possible to apply the matrix method to this structure. For your information, the matrix method in this course was based on this single stiffness matrix:

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
