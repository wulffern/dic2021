(TeX-add-style-hook
 "project_report"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("IEEEtran" "paper" "10pt" "a4paper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("graphicx" "final")))
   (add-to-list 'LaTeX-verbatim-environments-local "lstlisting")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "lstinline")
   (TeX-run-style-hooks
    "latex2e"
    "IEEEtran"
    "IEEEtran10"
    "graphicx"
    "wrapfig"
    "upgreek"
    "amssymb"
    "amsmath"
    "cite"
    "verbatim"
    "listings"
    "xcolor"
    "flafter"
    "booktabs"
    "url"
    "hyperref"
    "textcomp"
    "dirtytalk"
    "tabulary")
   (TeX-add-symbols
    '("url" 1)
    '("qt" 1)
    '("eqnr" 2)
    '("eqn" 1)
    '("req" 1)
    '("moved" 1)
    '("deleted" 1)
    '("secedit" 1)
    '("edit" 1)
    '("missing" 1))
   (LaTeX-add-labels
    "eqn:#2"
    "tbl:check")
   (LaTeX-add-bibitems
    "klein01")
   (LaTeX-add-xcolor-definecolors
    "armygreen"))
 :latex)

