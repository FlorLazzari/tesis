%-----------------------------------------------------%
% @author: Tony Beltramelli - www.tonybeltramelli.com %
%       IT University of Copenhagen - www.itu.dk      %
%       creation date: 2015/06/11, version: 0.1       %
%       last update: 2015/12/05, version: 0.2         %
%-----------------------------------------------------%

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{masterthesis}[2015/06/11 v0.1 Master's thesis]
\LoadClass[12pt, oneside, a4paper]{book}
\RequirePackage[left=2.5cm,textwidth=16cm,top=3cm,bottom=3cm]{geometry}

\RequirePackage[spanish]{babel}
\RequirePackage[utf8]{inputenc}
\RequirePackage{amsmath}
\RequirePackage{amsfonts}
\RequirePackage{amssymb}
\RequirePackage{graphicx}
\RequirePackage{float}
\RequirePackage{verbatim}
\RequirePackage{subcaption}
\RequirePackage{caption}
\RequirePackage{listings}
\RequirePackage{url}
\RequirePackage{comment}
\RequirePackage[toc,page]{appendix}
\RequirePackage{multicol}
\RequirePackage{color}
\definecolor{special}{rgb}{0.3, 0.3, 0.3}
\RequirePackage{lineno}

\RequirePackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\lhead{\slshape\nouppercase{\leftmark}}
\cfoot{\thepage}

\RequirePackage{afterpage}

\RequirePackage{hyperref}
\hypersetup{
	linktocpage,
    colorlinks,
    citecolor=special,
    filecolor=black,
    linkcolor=black,
    urlcolor=special,
}

\expandafter\def\expandafter\normalsize\expandafter{%
    \normalsize
    \setlength\abovedisplayskip{0pt}
    \setlength\belowdisplayskip{3pt}
    \setlength\abovedisplayshortskip{0pt}
    \setlength\belowdisplayshortskip{3pt}
}

\renewcommand\bibname{References}

\RequirePackage{pdfsync}
\synctex=1

\RequirePackage[times]{quotchap}
\definecolor{chaptergrey}{rgb}{0.5,0.5,0.5}

\RequirePackage{setspace} 
\onehalfspacing

\RequirePackage{multirow}

\parindent 12pt
\parskip 1em

\setcounter{secnumdepth}{3}
\setcounter{tocdepth}{3}

\newcommand{\HRule}{\rule{\linewidth}{0.5mm}}   %Para las HRule


\newcommand{\declaration}{
	\newpage
	\setlength{\columnsep}{1cm} 
	\chapter*{ }
	\input{frontmatter/declaration}

}

\newcommand{\abstractpage}{
	\newpage
	\chapter*{Resumen}
	\input{frontmatter/abstract}
	\addcontentsline{toc}{chapter}{\numberline{}Resumen}
}

\newcommand{\acknowledgments}{
    \newpage
	\chapter*{Agradecimientos}
	\input{frontmatter/acknowledgments}
	\addcontentsline{toc}{chapter}{\numberline{}Agradecimientos}
}

\newcommand{\contents}{
    \newpage
    \addcontentsline{toc}{chapter}{\numberline{}Índice }
    \setlength{\parskip}{0pt}
    \tableofcontents
}

\newcommand{\listfigures}{
    \newpage
    \addcontentsline{toc}{chapter}{\numberline{}List of figures}
    \listoffigures
}

\newcommand{\listtables}{
    \newpage
    \addcontentsline{toc}{chapter}{\numberline{}List of tables}
    \setlength{\parskip}{1em}
    \listoftables
}

\newcommand{\chapterheadline}[1]{
    \renewcommand\chapterheadstartvskip{\vspace*{#1\baselineskip}}
}

\newcommand{\makebibliography}{
    \newpage
    \chapterheadline{-4}
    
    \addcontentsline{toc}{chapter}{\numberline{}Bibliography}
    \bibliography{references}
    \bibliographystyle{ieeetr}
    
    \chapterheadline{-8}
}

\newcommand{\makefrontmatter}{
    \setcounter{page}{1}
    \pagenumbering{roman}
    
    \chapterheadline{-4}
    \declaration
    \abstractpage
    \acknowledgments
    \contents
    %\listfigures
    %\listtables
    
    \clearpage
    
    \setcounter{page}{1}
    \pagenumbering{arabic}
    
    \chapterheadline{-8}
}

\def\degree#1{\gdef\@degree{#1}}
%\def\university#1{\gdef\@university{#1}}
%\def\location#1{\gdef\@location{#1}}
\def\supervisor#1{\gdef\@supervisor{#1}}

\renewcommand{\maketitle}{
    \begin{titlepage}
        \begin{center}
            \setlength{\parskip}{0pt}
            
            \vbox{}
            \vbox{}
            
            {\huge {\bfseries \@title} \par}
            
            \vspace*{20mm}
            
            {\large { \@author} \par}
            {\large {\textit{Director:} \@supervisor} \par}
            
            \vspace*{3.5cm}
            
            \begin{center}
                \includegraphics[width=3cm]{images/logo}
            \end{center}
            
            \vspace*{5mm}
            {\large\it {\@degree} \par}
            
            {\large Facultad de Ciencias Exactas y Naturales \\ \textsc{Universidad de Buenos Aires} \par}
            
            \vspace*{5mm}
            
            {\large \@date \par}
        
        \end{center}
    \end{titlepage}
}


\newcommand\blankpage{%
    \null
    \thispagestyle{empty}%
    \addtocounter{page}{-1}%
    \newpage}
