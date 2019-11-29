#!/usr/bin/python
# -*- coding: utf8 -*-
# author: David Martin Planelles / masterplanelles@gmail.com

# Script per actualitzar el Chromedriver al PC a la ultima versió

import logging
import requests
import re
import urllib.parse as urlparse
import urllib.request
import zipfile
import os, sys, stat

from config import *

print('Getting last version link...')
r = requests.get(CHROMEDRIVER_URL)

# Get last release DL link
m = re.search('<a[^>]* href="https://chromedriver.storage.([^"]*)"', r.text)
version_link = m.group(1)
print('[OK!] Link: %s' % version_link)


# Parse Version
print('Parsing version...')
parsed = urlparse.urlparse(version_link)
chromedriver_version = urlparse.parse_qs(parsed.query)['path'][0].replace('/', "")
print('[OK] Version: %s' % chromedriver_version)

# Download zip
CHROMEDRIVER_PATH = '/tmp/%s_chromedriverlinux64.zip' % chromedriver_version
dl_link = '%s%s/chromedriver_linux64.zip' % (CHROMEDRIVER_DL_URL, chromedriver_version)
print('Download link: %s / Starting download...' % dl_link)
urllib.request.urlretrieve(dl_link, CHROMEDRIVER_PATH)  

# Check DL
if os.path.exists(CHROMEDRIVER_PATH):
	print('[OK] Download OK!')

# RM Actual version
if os.path.exists(os.path.join(CHROMEDRIVER_DEST_PATH, 'chromedriver')):
	os.remove(os.path.join(CHROMEDRIVER_DEST_PATH, 'chromedriver'))

# Extract Chromedriver
zip_ref = zipfile.ZipFile(CHROMEDRIVER_PATH, 'r')
zip_ref.extractall(CHROMEDRIVER_DEST_PATH)
zip_ref.close()

if os.path.exists(CHROMEDRIVER_DEST_PATH):
	print('[OK] Extract OK!')
	# Set permissions
	os.chmod(os.path.join(CHROMEDRIVER_DEST_PATH, 'chromedriver'), 777)
	os.chmod(os.path.join(CHROMEDRIVER_DEST_PATH, 'chromedriver'), 777)
	os.chmod(os.path.join(CHROMEDRIVER_DEST_PATH, 'chromedriver'), 777)


# RM dled file
if os.path.exists(CHROMEDRIVER_PATH):
	os.remove(CHROMEDRIVER_PATH)

# Link file to /usr/bin
if not os.path.exists('/usr/bin/chromedriver'):
	os.symlink(os.path.join(CHROMEDRIVER_DEST_PATH, 'chromedriver'), '/usr/bin/chromedriver')
	print('[OK] Made link to /usr/bin/chromedriver')

print('Done! Now you can execute chromedriver within whole system path!')