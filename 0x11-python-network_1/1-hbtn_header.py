#!/usr/bin/python3
""" Displays the value of the X-Request-Id in response header"""

from urllib import request
import sys


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
