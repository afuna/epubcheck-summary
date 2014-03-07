epubcheck-summary
=================

Summarizes the output of epubcheck

`epubcheck_summary --file=filename` will show a summary of errors grouped by type, with a count of each error and an index you can drill further down into. For example:

```
 1)    1 times   ERROR: value of attribute "href" is invalid; must be a URI
 2)    1 times   ERROR: attribute "id" not allowed here; expected attribute "charset", "defer", "src" or "xml:space"
 3)    2 times   ERROR: element "form" not allowed anywhere; expected the element end-tag, text or element "a", "abbr", "acronym", "address", "applet", "b", "bdo", "big", "blockquote", "br", "cite", "code", "del", "dfn", "div", "dl", "em", "h1", "h2", "h3", "h4", "h5", "h6", "hr", "i", "iframe", "img", "ins", "kbd", "map", "noscript", "ns:svg", "object", "ol", "p", "pre", "q", "samp", "script", "small", "span", "strong", "sub", "sup", "table", "tt", "ul" or "var" (with xmlns:ns="http://www.w3.org/2000/svg")
 4)    2 times   ERROR: attribute "start" not allowed here; expected attribute "dir", "id", "lang", "style", "title" or "xml:lang"
 5)    3 times   ERROR: hyperlink to non-standard resource <...> of type <...>
 6)    3 times   ERROR: element "dc:date" not allowed anywhere; expected the element end-tag or text
 7)    7 times   ERROR: <...>: referenced resource missing in the package.
 8)  678 times   ERROR: value of attribute "id" is invalid; must be an XML name without colons
 9) 2400 times   ERROR: <...>: fragment identifier is not defined in <...>
10)    5 times   HINT: Link attribute with no value
11)    4 times   WARNING: hyperlink to resource outside spine <...>
----
3106 total
```

`epubcheck_summary --file=filename --error=number` shows you the actual error messages. For example (using the same file as above):

```
> python epubcheck_summary --file=filename --error=5
filename1.html(61,87): hyperlink to non-standard resource '_images/triage_process.svg' of type 'image/svg+xml'
filename2.html(77,83): hyperlink to non-standard resource '_images/middleware.svg' of type 'image/svg+xml'
filename3.html(538,106): hyperlink to non-standard resource '_images/unittest_classes_hierarchy.svg' of type 'image/svg+xml'
```
