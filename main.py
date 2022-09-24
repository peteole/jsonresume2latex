import shutil
import tempfile
import os
from typing import Dict
from bottle import post, run, request, static_file
from urllib import parse
from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)
cv_template = env.get_template("cv.tex")


def template_json_to_tex(json: Dict):
    levels = list(dict.fromkeys([s["level"] for s in json["skills"]]))
    reordered_skills = [
        {'level':l,'names':[s['name'] for s in json["skills"] if s['level']==l]} for l in levels]
    rendered = cv_template.render(
        json | {'reordered_skills': reordered_skills})
    return rendered


@post('/to_tex')
def to_pdf():
    return template_json_to_tex(request.json)


@post('/to_pdf')
def to_pdf():
    rendered = template_json_to_tex(request.json)
    dir = tempfile.mkdtemp()
    shutil.copyfile("tccv.cls", dir+"/tccv.cls")

    with open(dir+"/cv.tex", "w") as text_file:
        text_file.write(rendered)
    os.system("cd "+dir+"; /laton cv.tex tccv.cls")
    return static_file("cv.pdf", root=dir)


run(host='0.0.0.0', port=8080)
