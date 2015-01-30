# -*- coding: utf-8 -*-

import mox
import unittest

__author__ = u"Tomas Holub (tomas.holub@olc.cz)"
__credits__ = u"""\
Author: Tomas Holub
Create date: 2014-09-01 13:14
Modification date:  
Description: """


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.mox = mox.Mox()

    def tearDown(self):
        if hasattr(self, u"mox"):
            self.mox.UnsetStubs()