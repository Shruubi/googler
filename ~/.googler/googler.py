# usage: python /path/to/file/googler.py "enter_search_string"
# author: Damon Swayn
# date: 3/2/2013
# license: GPL

#!/usr/bin/env python

import webbrowser
import sys

url = "https://www.google.com/search?q=" + sys.argv[1].replace(' ', '+')
webbrowser.open(url)
