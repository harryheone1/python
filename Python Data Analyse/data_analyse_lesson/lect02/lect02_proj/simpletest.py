""" Sessionization
session.py To iteratively discover sessions in the timestamps and hold active
session information to apply to new timestamps coming.

Author: Peng Wang <peng.wang@guavus.com>
"""
import numpy as np


class Sessionizer(object):

    def sessionize(self, name):
        print("Hello, " + name)
        return self