XEP-0106 (for python)
=====================

[XEP-0106](http://xmpp.org/extensions/xep-0106.html) is a specification for
escaping illegal characters in XMPP (jabber) node names so that they can be
processed by standards-compliant servers, and for unescaping them so that they
can be displayed sensibly.

This is probably most useful if you're going to glue bits of Jabber
infrastructure together with bits of Python code. For example, if you're going
to embed candy.js into a Django site, and you have a lot of users who are
registered for your service using their email address as their username, and
you implement single sign-on against your Jabber service.

Example Usage
-------------
The relevant portions are the ```escape``` and ```unescape``` methods:

    >>> import xep0106
    >>> username = 'alice@example.com'
    >>> username_escaped = xep0106.escape(username)
    >>> username_escaped
    'alice\40example.com'
    >>> xep-0106.unescape(username_escaped)
    'alice@example.com'

For more details, use the source, luke!

License
---------
Copyright © 2013 Joe Blaylock <jrbl@jrbl.org>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.


