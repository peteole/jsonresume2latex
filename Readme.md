# Jsonresume2latex
This project converts a jsonresume to a pdf resume. See [resume.pdf](resume.pdf) for an example output.
It uses the resume template  by 2012  Nicola Fontana <ntd at entidi.it>.

## Usage
Start the conversion server:
```
docker run -p 8080:8080 -d olepetersen/jsonresume2latex:0.2.1
```
Now use the conversion api:
```
curl localhost:8080/to_pdf -H "Content-Type: application/json" -d @resume.json -o resume.pdf
```
where your jsonresume is in `resume.json` and the output will be in `resume.pdf`.
Note that this WILL UPLOAD YOUR RESUME TO https://latexonline.cc/ . You can check the source code to see that this is the case.