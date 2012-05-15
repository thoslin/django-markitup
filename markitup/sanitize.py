"""
A simple wrapper for bleach, making tags and attributes configurable in here.

Test allowed tags

>>> s = '<a href="www.google.com">Google</a>'
>>> sanitize(s)
u'<a href="www.google.com">Google</a>'


Test disallowed tags

>>> s = '<img src="foo.png">'
>>> sanitize(s)
u'&lt;img src="foo.png"&gt;'
>>> sanitize(s, strip=True)
u''

"""


import bleach
from functools import partial
from django.conf import settings


ALLOWED_TAGS =  getattr(settings, "MARKITUP_ALLOWED_TAGS", bleach.ALLOWED_TAGS)
ALLOWED_ATTRIBUTES =  getattr(settings, "MARKITUP_ALLOWED_ATTRIBUTES", bleach.ALLOWED_ATTRIBUTES)


sanitize_html = partial(bleach.clean, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES)


if __name__ == "__main__":
    import doctest
    doctest.testmod()