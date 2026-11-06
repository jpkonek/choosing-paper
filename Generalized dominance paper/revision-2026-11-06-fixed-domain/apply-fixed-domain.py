import sys
C=r'\chg'
def apply(path, reps):
    s=open(path).read()
    for old,new,cnt in reps:
        n=s.count(old)
        if n!=cnt: sys.exit(f"{path}: expected {cnt} got {n}: {old[:70]!r}")
        s=s.replace(old,new)
    open(path,'w').write(s)
M=r'\chg{\M}'
gr=[
(r'\usepackage{tikz}', r'\usepackage{tikz}'+'\n'+r'\usepackage{xcolor}'+'\n'+r'\newcommand{\chg}[1]{{\color{red}#1}}',1),
(r'A \emph{ranking} $L$ consists of a nonempty set $\M_L\subseteq\M$, whose members are the models \emph{evaluable} by $L$, and a family of binary relations $\preceq_\omega$ on $\M_L$, one for each $\omega\in\Omega$.',
 r'\chg{A \emph{ranking} $L=(\preceq_\omega)_{\omega\in\Omega}$ is a family of binary relations on $\M$, one for each $\omega\in\Omega$.}',1),
(r'any models $c,m\in\M_L$,', r'any models $c,m\in'+M+'$,',1),
(r'if no $c\in\M_L$ dominates it. $\U_L$ is the set of models in $\M_L$ undominated', r'if no $c\in'+M+r'$ dominates it. $\U_L$ is the set of models in $'+M+'$ undominated',1),
(r'Let $\Lf$ be a putatively complete class of reasonable rankings.', r'Let $\Lf$ be a \chg{nonempty family of rankings on $\M$: a} putatively complete class of reasonable rankings.',1),
(r'(\forall L\in\Lf)\ \bigl[m\in\M_L\Rightarrow m\notin\U_L\bigr].', r'(\forall L\in\Lf)\ \chg{m\notin\U_L}.',1),
('of reasonable rankings. Firstly, we assume that the reasonable rankings collectively evaluate every model.\n'
 r'\begin{enumerate}[label=\textbf{(E)},leftmargin=*]'+'\n'+r'\item \textbf{Evaluability.} $\M=\bigcup_{L\in\mathfrak L}\M_L$.'+'\n'+r'\end{enumerate}'+'\n',
 'of reasonable rankings.\n',1),
('Next, we assume that there is some class', r'\chg{Firstly}, we assume that there is some class',1),
(r"Thirdly, for each reasonable ranking $L\in\mathfrak L$, we assume that there is a nonempty, maximal class of evaluable ``coherent'' models, $\C_L\subseteq\C\cap\M_L$,",
 r"\chg{Secondly}, for each reasonable ranking $L\in\mathfrak L$, we assume that there is a nonempty, maximal class of ``coherent'' models, $\C_L\subseteq\chg{\C}$,",1),
('Fourthly, the rankings', r'\chg{Thirdly}, the rankings',1),
('Consider, for example, \n','',1),
(r'Let $L$ be a ranking and $x\in\M_L$. \emph{Selection data for $x$} consist of a map $c:\Delta\to\M_L$,',
 r'Let $L$ be a ranking and $x\in'+M+r'$. \emph{Selection data for $x$} consist of a map $c:\Delta\to'+M+'$,',1),
(r'$L$ any ranking and $x\in\M_L$.', r'$L$ any ranking and $x\in'+M+'$.',1),
(r'For $I\subseteq\M_L$, \emph{fixed selection} means that there exists a map $c:\Delta\to\M_L$',
 r'For $I\subseteq'+M+r'$, \emph{fixed selection} means that there exists a map $c:\Delta\to'+M+'$',1),
(r'Let $\Lf$ be a family of rankings and consider:', r'Let $\Lf$ be a \chg{nonempty} family of rankings and consider:',1),
(r'every incoherent $x\in\M_L$, selection data', r'every incoherent $x\in'+M+'$, selection data',1),
(r'there is $L\in\Lf$ with $c\in\M_L$ and $c\in\U_L$;', r'there is $L\in\Lf$ with $c\in\U_L$\chg{.}',1),
(r'\item[(E)] \emph{Evaluability}: $\M=\bigcup_{L\in\Lf}\M_L$.'+'\n','',1),
(r'every ranking in $\Lf$ that evaluates it;', r'every ranking in $\Lf$;',1),
(r'\item Under (X) and (E), every incoherent model is dominated under at least one ranking in $\Lf$.'+'\n','',1),
(r'(a) Let $L\in\Lf$ and $x\in\M_L$ incoherent.', r'(a) Let $L\in\Lf$ and $x\in'+M+'$ incoherent.',1),
('\n'+r'(c) By (E) an incoherent $x$ lies in some $\M_L$, and by (a) it is dominated under $L$.','',1),
(r'\emph{loss} $\ell:\M_L\times\Omega', r'\emph{loss} $\ell:'+M+r'\times\Omega',1),
(r'be a map $\Delta\to\M_L$ such that:', r'be a map $\Delta\to'+M+'$ such that:',1),
(r'for every $m\in\M_L$ and every finitely supported', r'for every $m\in'+M+'$ and every finitely supported',1),
(r'Let $x\in\M_L$, $c(p)\coloneqq c_p$', r'Let $x\in'+M+r'$, $c(p)\coloneqq c_p$',1),
(r'family $\Lf=\{L\}$ with $\M_L=\M$: (X)', r'family $\Lf=\{L\}$: (X)',1),
(r'let $\ell$ be a loss on $\M_L$, and let $p\mapsto c_p$ map $\Delta$ onto $\C\subseteq\M_L$.',
 r'let $\ell$ be a loss on $'+M+r'$, and let $p\mapsto c_p$ map $\Delta$ onto $\C\subseteq'+M+'$.',1),
(r'$\{L\}$ satisfies (X), (A) and (E).', r'$\{L\}$ satisfies \chg{(X) and (A)}.',4),
(r'If $\M_L$ is a singleton', r'If $'+M+'$ is a singleton',1),
(r'Let $m\in\M_L$ and $p\in\Delta$', r'Let $m\in'+M+r'$ and $p\in\Delta$',1),
(r'this is (X). (E) holds with $\M=\M_L$.', r'this is (X).',1),
(r'Let $\Omega$ be arbitrary, $\M_L=[0,1]^{2^\Omega}$ with the product topology, and $\C\coloneqq\Delta$, with the topology inherited from $\M_L$.',
 r'Let $\Omega$ be arbitrary, $'+M+r'=[0,1]^{2^\Omega}$ with the product topology, and $\C\coloneqq\Delta$, with the topology inherited from $'+M+'$.',1),
(r'for all $q\in\C$ and $m\in\M_L$, strictly', r'for all $q\in\C$ and $m\in'+M+'$, strictly',1),
(r'Let $p(F)=1$ for a finite $F$ and $m\in\M_L$.', r'Let $p(F)=1$ for a finite $F$ and $m\in'+M+'$.',1),
(r'Let $\M_L=[0,1]^{\mathcal F}$', r'Let $'+M+r'=[0,1]^{\mathcal F}$',1),
(r'Let $I:\M_L\times W', r'Let $I:'+M+r'\times W',1),
(r'over $\M_L$, and $\theta\mapsto', r'over $'+M+r'$, and $\theta\mapsto',1),
(r'$\M_L=[0,1]^2$', r'$'+M+'=[0,1]^2$',1),
]
dg=[
(r'\usepackage{xr-hyper,needspace}', r'\usepackage{xr-hyper,needspace,xcolor}'+'\n'+r'\newcommand{\chg}[1]{{\color{red}#1}}',1),
(r'A ranking in this paper is a ranking in the sense of \cite[Definition~\ref{GR-def:ranking}]{KonekGR} with $\M_L=\M$: $Y\preceq_\omega X$',
 r'A ranking in this paper is \chg{a family of binary relations on $\M$, as in \cite[\S\ref{GR-sec:framework}]{KonekGR}}: $Y\preceq_\omega X$',1),
(r'and (E) because every ranking evaluates every model and $\Lf$ is nonempty: $\C$ is nonempty',
 r'and \chg{$\Lf$ is nonempty, as that theorem requires}: $\C$ is nonempty',1),
]
apply('general-rankings.tex',gr); apply('desirable-gambles.tex',dg); print("ok")
