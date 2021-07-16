# Minimal educational HTTP server in Python

This is a minimal HTTP server for educational purposes, written in Python.

## What it does

It serves the following URLs:

* `/`: A static page
* `/favicon.ico`: A static file, `www/favicon.png`
* `/served`: A simple page counter

## What it does not do

It is not a general-purpose (or production-ready) web server, serving arbitrary
files.

## Concepts

This can be used to convey the following concepts:

### General

* What is an HTTP server and how does it work?
* What is an HTML page?
* What are important HTTP headers?
* What are MIME (aka Content) Types and what are they used for?
* Can be used as a basis to talk about CSS and Javascript
* Can be used to talk about client-side (Javascript) and server-side (in this
  case, Python) computation

### Python

* Basic syntax
* Classes and inheritance (can be left abstract, but can also be used a basis
  to advance to the next level)
* Functions and methods, `self`
* Named parameters
* Reading files
* Global variables (and whether they are good or bad)
* Assertions
* Exceptions (i.e., if the image file is removed, an exception is raised and printed)
* Multi-line strings
* Format strings
* Difference between strings and bytes, introduction to Unicode (and UTF-8)

### Security

* When extending to serve arbitrary files based on the URL, care should be taken that
  the URLs (after the initial `/`) should not start with `.` nor contain `/` or
  `\`. Directory traversal could be shown.
* When extending to return user input as part of the contents (e.g., include the
  URL in the `404` error message or provide a simple server-side computation,
  e.g., °C → °F conversion), escaping should be used. Cross-Site-Scripting
  (XSS) could be demonstrated.
