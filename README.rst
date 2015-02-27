Clippy
======

Easy clipboard "copypasta" template tag (see it online on every repo page on github: http://github.com/mojombo/clippy), examples:

Integrating on templates
------------------------

Use this code to integrate it::

    {% load clippy_tags %}
    {{ "hello"|clippy }}

Now the user just have to click the button to copy the text to the clipboard.
