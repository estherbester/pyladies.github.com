========================
pyladies.com site setup
========================

:date: 2012-05-04 20:38
:tags: website
:category: articles

The actual pyladies.com website, redone using Github static pages so the entire world can see articles and events in progress. If something isn't listed, then submit a contribution.

How to get it running:

.. sourcecode:: bash

    pip install pelican
    git clone git://github.com/pyladies/pyladies.github.com.git

How to push up entries and pages and themes:

.. sourcecode:: bash
    
    pelican . -o . -s settings.py
    git commit -am "Adding content here"
    git push

Results!
========

http://pyladies.github.com

How to submit an article or event
=====================================

* Fork this project on github
* In your local branch, place your article or event in the appropriate directory (``articles`` or ``events``).
* The content must be formatted using RestructuredText or MarkDown.
* Don't submit the rendered HTML.
* Submit a pull request

Why articles and events may get rejected
========================================

There are a number of reasons why this may have occurred:

* Inappropriate content submitted
* Spelling or grammatical errors
* Pull request included the rendered HTML

How to submit a static page
===========================

Simply create a RST or MD file in the Pages directory. It's title will appear in the navigation in TitleCase.