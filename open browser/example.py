#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Mon April 12 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================



import webbrowser
import os
from urllib.request import urlopen
page = "https://www.newhaven.edu/"
req = urlopen(page)
with open("foobar.html","w") as file:
	file.write(str(req.read(), encoding='utf8'))
	root = os.path.dirname(os.path.abspath(__file__))
	webbrowser.open('file://' + root + '/foobar.html')