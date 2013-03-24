#/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Copyright © 2013 Joe Blaylock <jrbl@jrbl.org>
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# the file COPYING or http://www.wtfpl.net/ for more details.
"""XEP-0106 JID escaping library for Python.

XEP-0106 is a specification for escaping illegal characters in XMPP (jabber)
node names so that they can be processed by standards-compliant servers, and
for unescaping them so that they can be displayed sensibly.

This library is probably most useful if you're going to glue bits of Jabber
infrastructure together with bits of Python code. For example, if you're going
to embed candy.js into a Django site, and you have a lot of users who are
registered for your service using their email address as their username, and
you implement single sign-on against your Jabber service.

>>> import xep0106
>>> username = 'alice@example.com'
>>> username_escaped = xep0106.escape(username)
>>> username_escaped
'alice\40example.com'
>>> xep-0106.unescape(username_escaped)
'alice@example.com'

This library is distributed in the hope that it will be useful. If you find
this library useful, I'd love to hear from you. Complaints can be piped
straight to /dev/null."""


import re


def escape(unescaped_string):
    """Escape a string according to the rules specified in XEP-0106.

    >>> escape(r'\2plus\2is\4')
    r'\2plus\2is\4'
    >>> escape(r'foo\bar')
    r'foo\bar'
    >>> escape(r'foob\41r')
    r'foob\41r'
    """
    return unescaped_string

def unescape(escaped_string):
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()


