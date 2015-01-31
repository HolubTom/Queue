# -*- coding: utf-8 -*-

import mox
import unittest

__author__ = u"Tomas Holub"
__email__ = u"tomas.holub@olc.cz"


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.mox = mox.Mox()

    def tearDown(self):
        if hasattr(self, u"mox"):
            self.mox.UnsetStubs()