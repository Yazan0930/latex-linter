# Latex linter

> (La)TeX is a typesetting system that was designed and written by Donald Knuth and first 
released in 1978. TeX is a popular means of typesetting complex mathematical formulae 
and has become the standard for academic publishing. 
While (La)TeX has been noted as one of the most sophisticated digital typographical 
systems, it lacks a fast, modern, configurable linter. A linter is a static code analysis tool 
used to flag programming errors, bugs, stylistic errors and suspicious constructs.

> In this project, we developed a linter for TeX files. The linter ensures common 
stylistic and configurable rules for TeX files and, therefore, eases the discussion on, 
merging, and exchanging of TeX content. Since static code analysis can be a non-trivial task, 
we focus on high code quality, good software engineering, and architecture over more 
features (e.g., new rules).

## Getting Started

You need to have a command-line tool

### Prerequisites

- [Download file to install](https://github.com/Yazan0930/latex-linter/releases/download/v1.0.0/latex_linter-0.0.1-py3-none-any.whl)

### Installing

Installation steps are necessary so go through each step to do so 

```
pip install latex_linter-0.0.1-py3-none-any.whl
```

### Uninstalling

Run:
```
pip uninstall latex_linter-0.0.1-py3-none-any.whl
```

## Running 

### Latex Linter

Here is how you run linting latex-fil

```
latex-linter -h
```

Output
```
usage: latex-linter [-h] [-f FILE] [-b BREAKSENTENCE] [-l LINES]

Linter rols.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File to be linted
  -b BREAKSENTENCE, --breakSentence BREAKSENTENCE
                        Newline after a sentence for better git support. Usage: -b [True/False]
  -l LINES, --lines LINES
                        Blank lines before section, chapter, etc. (number adjustable). Usage: -l [number]
```

### Unit Tests

Must have the code map downloded in the divais
To download use [link](https://github.com/Yazan0930/latex-linter/releases/download/v1.0.0/latex-linter.zip)
Must have pytest installd ```pip3 install pytest```

Here is how you run unit tests :-P 

```
pytest -rP 
```

## License

MIT License it is open sourcing 
