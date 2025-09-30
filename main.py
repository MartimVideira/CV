import yaml
import marko

path = "./experience.yaml"

data = None

with open(path,"r") as file:
    data = yaml.safe_load(file)

print(data)

def prelude():
    with open("prelude.tex","r")  as f:
        return f.read()
        
    

def m(name,args):
    if type(args) is str:
        args = [args]
    
    r = "\\" + name 
    for arg in args:
        r += "{" + arg  + "}"

    return r
def about_me(data):

    r = r"\begin{center}"
    r += r"\textbf{\Huge \scshape " + data["prefered_name"] + r"} \\ \vspace{1pt}" + "\n"

    r +=r"\vspace{5 pt} \normalsize"
    t = lambda x : m("href",[x[0], m("underline",x[1])])
    contents = [
                t([f'mailto:{data["email"]}',data["email"]]),
            
                t([data["linkedin"]["link"],data["linkedin"]["display"]]),
                t([data["github"]["link"],data["github"]["display"]])
                ]

    r += "$|$\n".join(contents)
    r +=r"\end{center}"
    return r


def subheading(a):
    return m("resumeSubheading",a)
    
def item(a):
    return m("resumeItem",a) + r"\\" + "\n"

def bold(a):
    return m("textbf",a)

def education(e):
    x = r"\section{Education}\resumeSubHeadingListStart"
    x +=  subheading([e["university"],"",e["degree"],""])
    x += r"\resumeItemListStart"
    x+=  item(bold("GPA: ") + e["gpa"])
    x+=  item(bold("Coursework: ") + e["coursework"]) 
    x +=r"\resumeItemListEnd \resumeSubHeadingListEnd"
    return x

    
def build_experience(e):
    r = subheading([e["position"],e["from"]["begin"] + " -- " + e["from"]["end"],"",""])
    r+= visit(marko.parse(e["description"]))
    return r

def experience(experiences):
    r = "\n"
    r += r"\section{Experience}"
    r += "\n"
    r+= r"\resumeSubHeadingListStart"
    r += "\n"
    for e in experiences:
        r += build_experience(e) + "\n"
    r += r"\resumeSubHeadingListEnd"
    r += "\n"
    return r

def publications(publications): 
    if publications  == []:
        return ""
    return ""

def visit(child):
    r = ""
    if child.get_type() == "List":
        r += r"\resumeItemListStart" + "\n"
        for child in child.children:
            r+= visit(child)
        r += r"\resumeItemListEnd" + "\n"
    elif child.get_type() == "ListItem":
        r = item(" ".join(visit(c) for c in child.children))
    
    elif child.get_type() == "Document":
        r = "".join(visit(c) for c in child.children)
    elif child.get_type() == "RawText":
        r = child.children
    
    elif child.get_type() == "Paragraph":
        r = " ".join(visit(c) for c in child.children)

    elif child.get_type() == "StrongEmphasis":
        if False:
            r = bold(" ".join(visit(c) for c in child.children))
        else:
            r = " ".join(visit(c) for c in child.children)
    else:
        print("ERROR NO visitor for: ", child.get_type())


    return r


    
def build_project(e):
    r =m("resumeProjectHeading",[bold(e["name"]) + " $|$ " + m("emph",", ".join(e["technologies"]))])
    # Crucial god knows why
    r +="\n\n"
    r += visit(marko.parse(e["description"]))
    return r


def projects(projects):
    r = r"\section{Projects}"
    r+= r"\resumeSubHeadingListStart"
    for p in projects:
        r += build_project(p)
    r += r"\resumeSubHeadingListEnd"
    return r
    
def languages(langs):
    r = r"""\section{Languages}
        \begin{itemize}"""
    for l in langs:
        r += r"\item \textbf{" + l["l"] + "}: " + l["level"] + "\n"
    r += r"\end{itemize}"
    return r

def technologies(data): 
    r = r"\section{Technologies}"
    r +=r"\textbf{Programming Languages: }"
    r += ", ".join(data["programming_languages"]) + "."
    r += r"\\" + "\n"
    tech = set(data["technologies"])
    for p in data["projects"]:
        for t in p["technologies"]:
            if t not in data["programming_languages"]:
                tech.add(t)

    r +=r"\textbf{Technologies: }"
    r += ", ".join(tech) + "."
    return r



def main():
    r = ""
    r += prelude()
    r += "\n"
    r += r"\begin{document}"
    r += about_me(data)
    r += education(data["education"])
    r += publications([])
    r += experience(data["experience"])
    r += projects(data["projects"])
    r += technologies(data)
    r += languages(data["languages"])
    r += r"\end{document}"

    with open("out.tex", "w") as f:
        f.write(r)

main()