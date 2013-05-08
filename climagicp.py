#!/usr/bin/env python
# climagicp - Simple parser for climagic.org latest commands

import urllib2
from bs4 import BeautifulSoup

page = urllib2.urlopen('http://climagic.org')
soup = BeautifulSoup(page)
command_desc = soup.find(id="commanddescription")
command = soup.find(id="command").find('tt')
print "Description: " + command_desc.string.extract()
print "Command: " + command.string.extract()
