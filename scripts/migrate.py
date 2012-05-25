"""


1. get rss feed


2. parse, make html

3. extract article

4. convert to RST

5. cleanup

"""

import requests
import subprocess
from BeautifulSoup import RobustInsanelyWackAssHTMLParser
from feedparser import parse

FEED_URL = 'http://pyladies.com/blog/feeds/rss'

feed = requests.get(FEED_URL).content
parsedfeed = parse(feed)
order = len(parsedfeed.entries)

for entry in parsedfeed.entries:
    page_title = entry.title
    description = entry.summary_detail.value
    link = entry.link
    permalink = entry.link.split('/')[4]

    post = requests.get(link).content
    article = RobustInsanelyWackAssHTMLParser(post).article
    html = open(permalink + '.html', 'w')
    html.write(str(article))
    html.close()

    # replace the bold tag with its innards only.
    article('strong')[0].replaceWithChildren()
    # same with italics. messes up the RST.
    article('em')[0].replaceWithChildren()

    rst = open("{0}_{1}.rst".format(order, permalink), 'w')
    p = subprocess.Popen(['pandoc', '--from=html', '--to=rst'],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    new_rst = p.communicate(str(article))[0]
    rst.write(new_rst)
    rst.close()
    order -= 1
