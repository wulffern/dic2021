(TeX-add-style-hook
 "memo"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("IEEEtran" "technote" "10pt" "a4paper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("graphicx" "final")))
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
   (LaTeX-add-bibitems
    "wheat"
    "oww"))
 :latex)

