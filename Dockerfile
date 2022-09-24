from python:latest
RUN pip install requests jinja2 bottle
RUN curl -L https://raw.githubusercontent.com/aslushnikov/latex-online/master/util/latexonline > laton && chmod 755 laton
#RUN ls
WORKDIR /home
COPY  tccv.cls tccv.cls
COPY main.py main.py
COPY templates templates
CMD python main.py