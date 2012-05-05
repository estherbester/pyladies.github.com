============
pyladies.com
============

The actual pyladies.com website, redone using Github static pages so the entire world can see articles and events in progress. If something isn't listed, then submit a contribution!

:date: 2012-05-04 20:38
:tags: pyladies, website
:category: website


How to get it running::

    pip install pelican
    git clone git://github.com/pyladies/pyladies.github.com.git

My settings.py file::

    AUTHOR = 'PyLadies from around the world'
    GITHUB_URL = 'https://github.com/pyladies'
    SITEURL = 'http://pydanny.pyladies.com'
    SITENAME = 'pyladies'
    SOCIAL = (('twitter', 'http://twitter.com/pyladies'),
              ('github', 'https://github.com/pyladies'),
    TAG_FEED = 'feeds/%s.atom.xml'
    THEME='notmyidea'
    TWITTER_USERNAME = 'pyladies'

How I push up entries and pages and themes::
    
    pelican . -o . -s settings.py
    git commit -am "Adding content here"
    git push

Results!
========

http://pyladies.github.com

How to submit an article or event
===================================

* Fork this project on github
* In your local branch, place your article or event in the appropriate directory. The content must be formatted using RestructuredText.
* Submit a pull request

Why articles and events may get rejected
========================================

There are a number of reasons why this may have occurred:

* Inappropriate content submitted
* Spelling or grammatical errors