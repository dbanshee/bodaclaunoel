#! /usr/bin/python

import logging
import sys

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/usr/local/ban/bodaclaunoel')

from weeding import app as application
#application.secret_key = 'anything you wish'  

