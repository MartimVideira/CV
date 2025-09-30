import yaml
import marko

path = "./experience.yaml"

data = None

with open(path,"r") as file:
    data = yaml.safe_load(file)

print(data)


def prelude():
    x = r"""\documentclass[10pt, letterpaper]{article}

    % Packages:
    \usepackage[
        ignoreheadfoot, % set margins without considering header and footer
        top=2 cm, % seperation between body and page edge from the top
        bottom=2 cm, % seperation between body and page edge from the bottom
        left=2 cm, % seperation between body and page edge from the left
        right=2 cm, % seperation between body and page edge from the right
        footskip=1.0 cm, % seperation between body and footer
        % showframe % for debugging 
    ]{geometry} % for adjusting page geometry
    \usepackage{titlesec} % for customizing section titles
    \usepackage{tabularx} % for making tables with fixed width columns
    \usepackage{array} % tabularx requires this
    \usepackage[dvipsnames]{xcolor} % for coloring text
    \definecolor{primaryColor}{RGB}{0, 0, 0} % define primary color
    \usepackage{enumitem} % for customizing lists
    \usepackage{fontawesome5} % for using icons
    \usepackage{amsmath} % for math
    \usepackage[
        pdftitle={John Doe's CV},
        pdfauthor={John Doe},
        pdfcreator={LaTeX with RenderCV},
        colorlinks=true,
        urlcolor=primaryColor
    ]{hyperref} % for links, metadata and bookmarks
    \usepackage[pscoord]{eso-pic} % for floating text on the page
    \usepackage{calc} % for calculating lengths
    \usepackage{bookmark} % for bookmarks
    \usepackage{lastpage} % for getting the total number of pages
    \usepackage{changepage} % for one column entries (adjustwidth environment)
    \usepackage{paracol} % for two and three column entries
    \usepackage{ifthen} % for conditional statements
    \usepackage{needspace} % for avoiding page brake right after the section title
    \usepackage{iftex} % check if engine is pdflatex, xetex or luatex

    % Ensure that generate pdf is machine readable/ATS parsable:
    \ifPDFTeX
        \input{glyphtounicode}
        \pdfgentounicode=1
        \usepackage[T1]{fontenc}
        \usepackage[utf8]{inputenc}
        \usepackage{lmodern}
    \fi

    \usepackage{charter}

    % Some settings:
    \raggedright
    \AtBeginEnvironment{adjustwidth}{\partopsep0pt} % remove space before adjustwidth environment
    \pagestyle{empty} % no header or footer
    \setcounter{secnumdepth}{0} % no section numbering
    \setlength{\parindent}{0pt} % no indentation
    \setlength{\topskip}{0pt} % no top skip
    \setlength{\columnsep}{0.15cm} % set column seperation
    \pagenumbering{gobble} % no page numbering

    \titleformat{\section}{\needspace{4\baselineskip}\bfseries\large}{}{0pt}{}[\vspace{1pt}\titlerule]

    \titlespacing{\section}{
        % left space:
        -1pt
    }{
        % top space:
        0.3 cm
    }{
        % bottom space:
        0.2 cm
    } % section title spacing

    \renewcommand\labelitemi{$\vcenter{\hbox{\small$\bullet$}}$} % custom bullet points
    \newenvironment{highlights}{
        \begin{itemize}[
            topsep=0.10 cm,
            parsep=0.10 cm,
            partopsep=0pt,
            itemsep=0pt,
            leftmargin=0 cm + 10pt
        ]
    }{
        \end{itemize}
    } % new environment for highlights


    \newenvironment{highlightsforbulletentries}{
        \begin{itemize}[
            topsep=0.10 cm,
            parsep=0.10 cm,
            partopsep=0pt,
            itemsep=0pt,
            leftmargin=10pt
        ]
    }{
        \end{itemize}
    } % new environment for highlights for bullet entries

    \newenvironment{onecolentry}{
        \begin{adjustwidth}{
            0 cm + 0.00001 cm
        }{
            0 cm + 0.00001 cm
        }
    }{
        \end{adjustwidth}
    } % new environment for one column entries

    \newenvironment{twocolentry}[2][]{
        \onecolentry
        \def\secondColumn{#2}
        \setcolumnwidth{\fill, 6.5cm}
        \begin{paracol}{2}
    }{
        \switchcolumn \raggedleft \secondColumn
        \end{paracol}
        \endonecolentry
    } % new environment for two column entries

    \newenvironment{threecolentry}[3][]{
        \onecolentry
        \def\thirdColumn{#3}
        \setcolumnwidth{, \fill, 4.5 cm}
        \begin{paracol}{3}
        {\raggedright #2} \switchcolumn
    }{
        \switchcolumn \raggedleft \thirdColumn
        \end{paracol}
        \endonecolentry
    } % new environment for three column entries

    \newenvironment{header}{
        \setlength{\topsep}{0pt}\par\kern\topsep\centering\linespread{1.5}
    }{
        \par\kern\topsep
    } % new environment for the header

    \newcommand{\placelastupdatedtext}{% \placetextbox{<horizontal pos>}{<vertical pos>}{<stuff>}
    \AddToShipoutPictureFG*{% Add <stuff> to current page foreground
        \put(
            \LenToUnit{\paperwidth-2 cm-0 cm+0.05cm},
            \LenToUnit{\paperheight-1.0 cm}
        ){\vtop{{\null}\makebox[0pt][c]{
            \small\color{gray}\textit{Last updated in September 2024}\hspace{\widthof{Last updated in September 2024}}
        }}}%
    }%
    }%

    % save the original href command in a new command:
    \let\hrefWithoutArrow\href

    % new command for external links:
    """
    return x

def m(name,args):
    if type(args) is str:
        args = [args]
    
    r = "\\" + name 
    for arg in args:
        r += "{" + arg  + "}"

    return r
def about_me(data):
    r = r""" \begin{document}
    \newcommand{\AND}{\unskip
        \cleaders\copy\ANDbox\hskip\wd\ANDbox
        \ignorespaces
    }
    \newsavebox\ANDbox
    \sbox\ANDbox{$|$}

    \begin{header}
        \fontsize{25 pt}{25 pt}\selectfont """ 
    r += data["prefered_name"]  + "\\\\ \n"
    r +=r"\vspace{5 pt} \normalsize"
    t = lambda x : m("hrefWithoutArrow",x)
    contents = [
                t([f'mailto:{data["email"]}',data["email"]]),
            
                t([data["linkedin"]["link"],data["linkedin"]["display"]]),
                t([data["github"]["link"],data["github"]["display"]])
                ]
    for i, content in enumerate(contents):
        r += r"\mbox{" + content+  "}"
        if (i +1) < len(contents):
            r += r""" \kern 5.0 pt%
            \AND%
            \kern 5.0 pt%"""
        r +="\n"
    
    r +=r""" \end{header}"""
    return r

    
def education(e):
    x = r"\section{Education}"
    x += m("begin",["twocolentry",e["from"]["begin"] + "-"+ e["from"]["end"]])
    x +=  "\n"
    x += m("textbf",[e["university"]])
    x += r"\end{twocolentry}"
    x += e["degree"]
    x +=  r"\vspace{0.10 cm} \begin{onecolentry} \begin{highlights}"
    
    x+=  r"\item GPA: " + e["gpa"] + "\n"
    x+=  r"\item \textbf{Coursework:}" + e["coursework"] + "\n"
    x += r"\end{highlights} \end{onecolentry}"
    return x

    
def build_experience(e):

    r= r"\begin{twocolentry}{"f'{e["from"]["begin"]} – {e["from"]["end"]}'+ "}"
    r += "\\textbf{" + e["position"] + r"} \end{twocolentry}"
    r += r"\vspace{0.10 cm}"
    r+= visit(marko.parse(e["description"]))
    r += r"\vspace{0.2 cm}" + "\n"
    return r

def experience(experiences):
    r = r"\section{Experience}"
    print(len(experiences))
    for e in experiences:
        r += build_experience(e)
    return r

def publications(publications): 
    if publications  == []:
        return ""
    x = r"""\section{Publications}
        
        \begin{samepage}
            \begin{twocolentry}{
                Jan 2004
            }
                \textbf{3D Finite Element Analysis of No-Insulation Coils}
            \end{twocolentry}

            \vspace{0.10 cm}
            
            \begin{onecolentry}
                \mbox{Frodo Baggins}, \mbox{\textbf{\textit{John Doe}}}, \mbox{Samwise Gamgee}

                \vspace{0.10 cm}
                
        \href{https://doi.org/10.1109/TASC.2023.3340648}{10.1109/TASC.2023.3340648}
        \end{onecolentry}
        \end{samepage}
    """
    return x

def visit(child):
    r = ""
    if child.get_type() == "List":
        r = r"\begin{onecolentry}\begin{highlights}"  + "\n"
        for child in child.children:
            r+= visit(child)
        r += r"\end{highlights} \end{onecolentry}" + "\n"
    elif child.get_type() == "ListItem":
        r = r"\item " + " ".join(visit(c) for c in child.children) + "\n"
    
    elif child.get_type() == "Document":
        r = "".join(visit(c) for c in child.children)
    elif child.get_type() == "RawText":
        r = child.children
    
    elif child.get_type() == "Paragraph":
        r = " ".join(visit(c) for c in child.children) + "\n"

    elif child.get_type() == "StrongEmphasis":
        r = r"\textbf{" + " ".join(visit(c) for c in child.children) + "}"
    else:
        print("ERROR NO visitor for: ", child.get_type())


    return r


    
def build_project(p):
    r = r"\begin{twocolentry}{"+ (p["url"] if p["url"] else " ") + "}"
    r += "\\textbf{" + p["name"] + r"}\end{twocolentry}"
    r += r"\vspace{0.10 cm}"
    r += visit(marko.parse(p["description"]))

    r += r"\vspace{0.2 cm}" + "\n"
    return r


def projects(projects):
    r = r"\section{Projects}"
    for p in projects:
        r += build_project(p)
    return r
def languages(langs):
    r = r"""\section{Languages}
        \begin{onecolentry}"""
    for l in langs:
        r += r"\item \textbf{" + l["l"] + "}: " + l["level"] + "\n"
    r += r"\end{onecolentry}"
    return r

def technologies(data): 

    r = r"""\section{Technologies}
        \begin{onecolentry}
            \textbf{Programming Languages:}"""

    r += ", ".join(data["programming_languages"])
    r += r"\end{onecolentry}"
    r += r"""\vspace{0.2 cm}
        \begin{onecolentry}
            \textbf{Technologies:}"""
    
    tech = set(data["technologies"])
    for p in data["projects"]:
        for t in p["technologies"]:
            if t not in data["programming_languages"]:
                tech.add(t)
    r += ", ".join(tech)
    r+= r"\end{onecolentry}"
    return r

def end():
    return r"\end{document}"


def main():
    r = ""
    r += prelude()
    r += about_me(data)
    r += education(data["education"])
    r += publications([])
    r += experience(data["experience"])
    r += projects(data["projects"])
    r += technologies(data)
    r += languages(data["languages"])
    r += end()

    with open("out.tex", "w") as f:
        f.write(r)
main()