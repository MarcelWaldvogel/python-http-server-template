# Minimal educational HTTP server in Python

This is a minimal HTTP server for educational purposes, written in Python.

## What it does

It serves the following URLs on `http://localhost:8000`:

* `/`: A static page
* `/favicon.ico`: A static file, `www/favicon.png`
* `/served`: A simple page counter
* Everything else will receive `404 Not Found`

## What it does not do

It is not a general-purpose (or production-ready) web server, serving arbitrary
files.

## Concepts

This can be used to convey the following concepts:

### General

* [What is an HTTP server and how does it work?](https://whatis.techtarget.com/definition/Web-server)
* [What is an HTML page?](https://en.wikipedia.org/wiki/HTML#Markup)
* [What are important HTTP headers?](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_messages)
* [What are MIME (aka Content) Types and what are they used for?](https://en.wikipedia.org/wiki/Media_type)
* Can be used as a basis to talk about [CSS](https://en.wikipedia.org/wiki/CSS) and [Javascript](https://en.wikipedia.org/wiki/JavaScript)
* Can be used to talk about client-side (Javascript) and server-side (in this
  case, Python) computation

### Python

* [Basic syntax](https://docs.python.org/3/tutorial/)
* [Classes and inheritance](https://docs.python.org/3/tutorial/classes.html) (can be left abstract, but can also be used a basis
  to advance to the next level)
* [Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) and methods, `self`
* [Named parameters](https://docs.python.org/3/tutorial/controlflow.html#special-parameters)
* Reading files
* Global variables (and whether they are good or bad)
* [Assertions](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)
* [Exceptions](https://docs.python.org/3/tutorial/errors.html) (i.e., if the image file is removed, an exception is raised and printed)
* [Multi-line strings](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)
* [Format strings](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)
* Difference between strings and [bytes](https://docs.python.org/3/library/stdtypes.html#bytes-objects), introduction to [Unicode](https://en.wikipedia.org/wiki/Unicode) (and UTF-8), possibly motivated by [Mojibake](https://de.wikipedia.org/wiki/Zeichensalat#Beispiele)

### Security

* When extending to serve arbitrary files based on the URL, care should be taken that
  the URLs (after the initial `/`) should not start with `.` nor contain `/` or
  `\`. [Directory traversal](https://owasp.org/www-community/attacks/Path_Traversal) could be shown.
* When extending to return user input as part of the contents (e.g., include the
  URL in the `404` error message or provide a simple server-side computation,
  e.g., °C → °F conversion), escaping should be used. [Cross-Site-Scripting
  (XSS)](https://owasp.org/www-project-top-ten/2017/A7_2017-Cross-Site_Scripting_(XSS)) could be demonstrated.
