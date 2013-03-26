#!/bin/bash
# Copyright © 2013 Joe Blaylock <jrbl@jrbl.org>
# 
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# the file COPYING or http://www.wtfpl.net/ for more details.
           
# package maintainer convenience script
rm -f *~ *.orig *.pyc 2>/dev/null
rm -rf dist
rm -f MANIFEST

pep8 *.py
pyflakes *.py
2to3 *.py

# build dist package with
# python setup.py sdist
