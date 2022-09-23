import requests
from urllib import parse
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import sys
filename = "/home/olep/Documents/software/portfolio/util/resume.json"
if len(sys.argv) > 1:
    filename = sys.argv[1]
variables = {}
with open(filename, 'r') as my_file:
    variables = json.load(my_file)

# print(variables)

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)
cv_template = env.get_template("cv.tex.j2")
rendered = cv_template.render(variables)
# print(cv_template.render(variables))
with open("cv.tex", "w") as text_file:
    text_file.write(rendered)


# parsed = parse.quote(rendered)
# print(parsed)
# resp=requests.get("https://latexonline.cc/compile?text="+parsed)
# print(resp.text)
