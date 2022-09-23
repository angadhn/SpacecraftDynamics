---
title: 'Introductory Symbolic Computational Dynamics'
tags:
  - Python
  - engineering mechanics
  - classical dynamics
  - vector algebra
  - vector calculus
authors:
  - name: Angadh Nanjangud
    orcid: 0000-0002-1785-9140
    corresponding: true # (This is how to denote the corresponding author)
    equal-contrib: false
    affiliation: 1 # (Multiple affiliations must be quoted)
  - name: Mughees Asif 
    equal-contrib: false # (This is how you can denote equal contributions between multiple authors)
    affiliation: 1
  - name: Simone Asci
    equal-contrib: false
    affiliation: 1
affiliations:
 - name: Queen Mary University of London, London, UK
   index: 1
 - name: Institution Name, Country
   index: 2
 - name: Independent Researcher, Country
   index: 3
date: 5 September 2022
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
#aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary

# Statement of need
Testing refs [@gede2013constrained]

# Mathematics

Single dollars ($) are required for inline mathematics e.g. $f(x) = e^{\pi/x}$

Double dollars make self-standing equations:

$$\Theta(x) = \left\{\begin{array}{l}
0\textrm{ if } x < 0\cr
1\textrm{ else}
\end{array}\right.$$

You can also use plain \LaTeX for equations
\begin{equation}\label{eq:fourier}
\hat f(\omega) = \int_{-\infty}^{\infty} f(x) e^{i\omega x} dx
\end{equation}
and refer to \autoref{eq:fourier} from text.

# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

# Acknowledgements

# References
