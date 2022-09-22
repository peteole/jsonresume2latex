import json
import sys
filename="/home/olep/Documents/software/portfolio/util/resume.json"
if len(sys.argv) > 1:
    filename=sys.argv[1]
variables={}
with open(filename, 'r') as my_file:
    variables=json.load(my_file)

#print(variables)

from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)
cv_template = env.get_template("cv.tex.j2")
#print(cv_template.render(variables))
with open("cv.tex", "w") as text_file:
    text_file.write(cv_template.render(variables))