#!/usr/bin/env python
# climagicp - Simple parser for climagic.org latest commands

import sys
import urllib2
try:
    from bs4 import BeautifulSoup
except ImportError:
    print "BeatifulSoup is not installed in your system, try: emerge -av dev-python/beautifulsoup"
    sys.exit(1)

page = urllib2.urlopen('http://climagic.org')
soup = BeautifulSoup(page)
command_desc = soup.find(id="commanddescription")
command = soup.find(id="command").find('tt')
print "Description: " + command_desc.string.extract()
print "Command: " + command.string.extract()
