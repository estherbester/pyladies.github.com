
import requests
import subprocess
from BeautifulSoup import RobustInsanelyWackAssHTMLParser


PAGE_URLS = [#'t-shirts', 
             'events',
             'events/pycon2012',
             'events/2012-pyladies-pycon-grant-program-final-results',
             'events/past-events',
             'leadership',
             'resources/slides-from-51511-beginners-workshop',
             'resources/policies',
             'chat',
             'chat/irc-instructions']

SITE_PREFIX = "http://pyladies.com/"


def fetch_content(url):
    """ Get page contents, save to html file, return contents """
    page_content = requests.get(url).content
    hfile = open(page_url.replace('/', '-') + '.html', 'w')
    hfile.write(page_content)
    hfile.close()
    return page_content


def parse_html(html, tag_to_parse, attrs={}):
    """ Parse and clean up the HTML to prep for rst conversion """
    parsed_html = RobustInsanelyWackAssHTMLParser(html).find(tag_to_parse, attrs)
    return str(parsed_html)


def convert_html_to_rst(filename, html):
    ''' Save text to .rst file '''
    rfile = open(filename.replace('/', '-') + ".rst", 'w')
    p = subprocess.Popen(['pandoc', '--from=html', '--to=rst'],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    new_rst = p.communicate(html)[0]
    rfile.write(new_rst)
    rfile.close()


for page_url in PAGE_URLS:
    url = SITE_PREFIX + page_url
    page_content = fetch_content(url)
    content_parsed = parse_html(page_content, 'div', {'id': 'main'})
    convert_html_to_rst(page_url, content_parsed)
print "Finished"
