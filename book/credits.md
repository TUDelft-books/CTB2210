(credits)=
# Credits and License

You can refer to this book as:

> Tom van Woudenberg from Delft University of Technology (2025) _CTB2210 - Constructiemechancia 3_. https://oit.tudelft.nl/CTB2210. Source files at https://github.com/TUDelft-books/CTB2210. CC BY 4.0.

You can refer to individual chapters or pages within this book as:

> `<Title of Chapter or Page>`. in Tom van Woudenberg from Delft University of Technology (2025) _CTB2210 - Constructiemechancia 3_.`<url to specific page on book website>`. Source files at `<link to specific commit / file in github repo`. CC BY 4.0.

We anticipate that the content of this book will change significantly. Therefore, we recommend using the source code directly with the citation above that refers to the GitHub repository and lists the date and name of the file. Although content will be added over time, chapter titles and URL's in this book are expected to remain relatively static. However, we make no guarantee, so if it is important for you to reference a specific location/commit within the book.

## How the book is made
This website is written in markdown and jupyter notebooks files, which are converted to html using tools from [TeachBooks](https://teachbooks.io/). The files are stored on a [public GitHub repository](https://github.com/TUDelft-books/CTB2210). The website can be viewed at https://oit.tudelft.nl/CTB2210.

To recreate the website you have two options (more information in the [TeachBooks manual](https://teachbooks.io/manual/):
- In the GitHub interface: fork this repository, enable Github Pages from the source GitHub actions (Settings - Code and automation - Pages - Build and deployment - Source - GitHub Actions), enable workflows (Actions - I understand my workflows, go ahead and enable them) and run the call-deploy-book workflow (Actions - call-deploy-book - Run workflow - Run workflow). The website is released on the URL as shown on the workflow summary when the workflow has finished (Actions - call-deploy-book - call-deploy-book - Summary).
- On your own computer: clone this repository, install the required packages (`pip install -r requirements.txt`) and build the book (`teachbooks build book`). The website is stored locally in `book/_build/index.html`.

## License
This book is [CC BY 4.0 licensed](https://creativecommons.org/licenses/by/4.0/) allowing you to share and adapt the material, as long as the source is named. External resources that are reused in this book are listed below.

(external_resources)=
### External resources

Parts of this book are taken from other external resources and reused in various ways. If an author is not listed on a particular page, it is by the Authors, except as follows:

The following pages are included directly from an external resource:
- The following pages includes text from {cite:t}`CEG_mechanics_BSc`. Original content licensed under CC BY 4.0 License:
  - [](./_git/github.com_TUDelft-books_CEG-mechanics-BSc/NL/book/statically_inderminate/determinancy.md)
  - [](./_git/github.com_TUDelft-books_CEG-mechanics-BSc/NL/book/tools/matrixframe.md)


(editor)=
## About the Editors

### Tom van Woudenberg

```{figure} figures/Tom.jpg
:width: 300px
:align: center
:class: dark-light
```

Tom van Woudenberg is a lecturer at Delft University of Technology. Equipped with a dedication to education in structural mechanics, he strives to cultivate a blended learning environment that engages students actively and rewards their efforts.

Tom graduated in 2020 at Delft University of Technology on structural optimisation. From August 2020 to August 2022, Tom worked at Amsterdam University of Applied Sciences as lecturer construction, specialised in structural mechanics. Since September 2022, Tom is working at Delft University of Technology.

Next to courses on structural mechanics, Tom (co)teaches courses on optimisation, numerical methods, data-analysis and statistics. Next to that, Tom supervises BSc- and MSc-students, partly on the research project of [Macaulay's method](https://teachbooks.io/Macaulays_method). Furthermore, Tom is actively involved in cross-faculty collaboration on [PRIMECH](https://www.tudelft.nl/teachingacademy/communities/primech), [TeachBooks](https://teachbooks.io/) and various digital tools for teaching like [ANS](https://ans.app/) and Git.

- {fa}`envelope` T.R.vanWoudenberg@tudelft.nl
- {fa}`envelope` tomvanw@hotmail.com
- {fa}`phone` +31152789739
- {fa}`location-dot` TU Delft – Civil Engineering & Geosciences - Department 3MD – Section Applied Mechanics - Room 6.45
- <i class="fa-brands fa-github"></i> [GitHub profile ](https://github.com/Tom-van-Woudenberg)
- <i class="fa-brands fa-linkedin"></i> [LinkedIn profile](https://www.linkedin.com/in/tom-van-woudenberg/)
- {fa}`building-columns` [Delft University of Technology profile](https://www.tudelft.nl/en/staff/t.r.vanwoudenberg/)

### Acknowledgements
Big thanks to the various colleagues (with Robert Lanzafame in particular) and teaching assistant part of the [TeachBooks](https://teachbooks.io/) for developing tools and providing support to improve this book.
