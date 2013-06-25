#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Copyright © 2013 Joe Blaylock <jrbl@jrbl.org>
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# the file COPYING or http://www.wtfpl.net/ for more details.
r"""XEP-0106 JID escaping library for Python.

XEP-0106 is a specification for escaping illegal characters in XMPP
(jabber) node names so that they can be processed by standards-compliant
servers, and for unescaping them so that they can be displayed sensibly.

This library is probably most useful if you're going to glue bits of
Jabber infrastructure together with bits of Python code. For example,
if you're going to embed candy.js into a Django site, and you have a
lot of users who are registered for your service using their email
address as their username, and you implement single sign-on against your
Jabber service.

>>> import xep0106
>>> username = 'alice@example.com'
>>> username_escaped = xep0106.escape(username)
>>> username_escaped
'alice\\40example.com'

# Unimplemented cases:
#>>> xep0106.unescape(username_escaped)
#'alice@example.com'

This library is distributed in the hope that it will be useful. If you
find this library useful, I'd love to hear from you. Complaints can be
piped straight to /dev/null."""


__forward = {' ': r'\20', '"': r'\22', '&': r'\26', "'": r'\27', '/': r'\2f',
             ':': r'\3a', '<': r'\3c', '>': r'\3e', '@': r'\40', '\\': r'\5c'}
__reverse = dict(((v, k) for k, v in list(__forward.items())))


def escape(unescaped_string):
    r"""Escape a string according to the rules specified in XEP-0106.

    Only escape the node portion of the JID. That is, in the example
    c:\5commas@example.com, the node portion is c:\5commas, and the
    @example.com specifies the jabber hostname. Illegal characters in the
    hostname are specified to be unescapable.

    Note that strings may *look* wrong even if they aren't actually wrong,
    because Python auto-escapes \ in all interactive cases, including tests.

    >>> [s == escape(s) for s in (r'\2plus\2is\4', r'foo\bar', r'foob\41r')]
    [True, True, True]
    >>> escape(r"d'artagnan")
    'd\\27artagnan'
    >>> escape(r'/.fanboy')
    '\\2f.fanboy'
    >>> escape(r'::foo::')
    '\\3a\\3afoo\\3a\\3a'
    >>> escape(r'<foo>')
    '\\3cfoo\\3e'
    >>> escape(r'user@host')
    'user\\40host'
    >>> escape(r'c:\net')
    'c\\3a\\net'
    >>> escape(r'c:\\net')
    'c\\3a\\\\net'
    >>> escape(r'c:\5commas')
    'c\\3a\\5c5commas'
    >>> escape('space cadet')
    'space\\20cadet'
    >>> escape('call me "ishmael"')
    'call\\20me\\20\\22ishmael\\22'
    >>> escape('at&t guy')
    'at\\26t\\20guy'
    >>> escape('c:\cool stuff')
    'c\\3a\\cool\\20stuff'
    """
    chars = unescaped_string.strip()
    new_chars = [''] * len(chars)
    for i in range(len(chars)):
        C = chars[i]
        if C == '\\':
            if ''.join(chars[i:i + 3]) in __reverse:
                new_chars[i] = __forward[C]
            else:
                new_chars[i] = C
        else:
            new_chars[i] = __forward[C] if C != '\\' and C in __forward else C
    return ''.join(new_chars)


def unescape(escaped_string):
    r"""Retrieve display string according to rules in XEP-0106.

    >>> [s == unescape(s) for s in (r'\2ps\2is\4', r'foo\bar', r'fob\41r')]
    [True, True, True]
    >>> unescape('d\\27artagnan')
    "d'artagnan"
    >>> unescape('\\2f.fanboy')
    '/.fanboy'
    >>> unescape('\\3a\\3afoo\\3a\\3a')
    '::foo::'
    >>> unescape('\\3cfoo\\3e')
    '<foo>'
    >>> unescape('user\\40host')
    'user@host'
    >>> unescape('c\\3a\\5c5commas')
    'c:\\5commas'
    >>> unescape('c\\3a\\net')
    'c:\\net'
    >>> unescape('c\\3a\\\\net')
    'c:\\\\net'
    >>> unescape('space\\20cadet')
    'space cadet'
    >>> unescape('call\\20me\\20\\22ishmael\\22')
    'call me "ishmael"'
    >>> unescape('at\\26t\\20guy')
    'at&t guy'
    >>> unescape('c\\3a\\cool\\20stuff')
    'c:\\cool stuff'
    """
    chars = escaped_string.strip()

    new_chars = ''
    i = 0
    while i < len(chars):
        C = chars[i]
        if C == '\\':
            if chars[i:i + 3] in __reverse:
                new_chars += __reverse[chars[i:i + 3]]
                i += 3
                continue
            else:
                new_chars += C
        else:
            new_chars += C
        i += 1

    return ''.join(new_chars)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
