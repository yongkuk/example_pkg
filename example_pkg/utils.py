__all__ = ['errx','errprint']

import sys

def errx(msg):
    errprint(msg)
    sys.exit(254)

def errprint(msg, end=None):
    print(msg, file=sys.stderr, end=end)
