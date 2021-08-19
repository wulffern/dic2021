(TeX-add-style-hook
 "why_learn_dic"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("IEEEtran" "technote" "10pt" "a4paper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("graphicx" "final")))
   (add-to-list 'LaTeX-verbatim-environments-local "lstlisting")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "url")
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
    "textcomp"
    "dirtytalk")
   (TeX-add-symbols
    '("url" 1)
    '("qt" 1)
    '("eqn" 1)
    '("moved" 1)
    '("deleted" 1)
    '("secedit" 1)
    '("edit" 1)
    '("missing" 1))
   (LaTeX-add-labels
    "fig_qfn")
   (LaTeX-add-bibitems
    "bbs47")
   (LaTeX-add-xcolor-definecolors
    "armygreen"))
 :latex)

