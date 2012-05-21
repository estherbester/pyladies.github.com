========================
pyladies.com site setup
========================

:date: 2012-05-04 20:38
:tags: Website
:category: Articles

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

* Fork the https://github.com/pyladies/pyladies.com-articles or https://github.com/pyladies/pyladies.com-events projects on github
* In your local branch, place your article or event in its respective project directory.
* The content must be formatted using RestructuredText, MarkDown, or (as a last resort) plain text.
* Don't submit the rendered HTML.
* Submit a pull request
* The maintainers of this site will then review and either publish or reject your article submission.

Why articles and events may get rejected
========================================

There are a number of reasons why this may have occurred:

* Inappropriate content submitted
* Spelling or grammatical errors
* Pull request included the rendered HTML

How to submit a static page
===========================

Simply create a RST or MD file in the Pages directory. Its title will appear in the navigation in TitleCase.
