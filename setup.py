#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Copyright © 2013 Joe Blaylock <jrbl@jrbl.org>
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# the file COPYING or http://www.wtfpl.net/ for more details.

from distutils.core import setup

setup(
        # Required args
        name = 'xep0106',
        version = 1.0,
        author = 'Joe Blaylock',
        author_email = 'jrbl@jrbl.org',
        url = 'https://github.com/jrbl/xep0106',
        py_modules = ['xep0106', ],

        # optional args
        description = 'XEP-0106 JID escaping library for Python.',
        long_description = \
"""XEP-0106 is a specification for escaping illegal characters in XMPP
(jabber) node names so that they can be processed by standards-compliant
servers, and for unescaping them so that they can be displayed sensibly.

This library is probably most useful if you're going to glue bits of
Jabber infrastructure together with bits of Python code. For example,
if you're going to embed candy.js into a Django site, and you have a
lot of users who are registered for your service using their email
address as their username, and you implement single sign-on against your
Jabber service.""",

        classifiers = ["Programming Language :: Python",
                       "License :: Public Domain",
                       "Operating System :: OS Independent",
                       "Natural Language :: English",
                       "Development Status :: 5 - Production/Stable",
                       "Intended Audience :: Developers",
                       "Topic :: Communications :: Chat",
                       "Topic :: Software Development :: Pre-processors",
                       "Topic :: Internet :: Proxy Servers",
                       "Topic :: Text Processing :: Filters",
                       "Topic :: Utilities",
                      ],
     )
