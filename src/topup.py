#!/usr/bin/env python


from __future__ import print_function
import os
import sys
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

# system
from   datetime import datetime, timedelta
from   functools import wraps
import pprint
import random
import re
import sys
import time


# pypi
import argh
def main(balance):

    top_up = 50 - float(balance)

    two_point_five_percent = top_up * .025
    deposit = top_up + two_point_five_percent + 0.35
    print("deposit = {0}".format(deposit))

if __name__ == '__main__':
    argh.dispatch_command(main)
